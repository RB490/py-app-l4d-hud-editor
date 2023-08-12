"""This module is a sub class of the game class.
functions related to the game folder such as switching between user/dev modes"""
# pylint: disable=broad-exception-caught
import filecmp
import json
import os
import shutil
from enum import Enum, auto
from tkinter import filedialog, messagebox

from classes.vpk import VPKClass
from utils.constants import MODS_DIR, SCRIPT_NAME
from utils.functions import (
    copy_files_in_directory,
    get_dir_size_in_gb,
    get_steam_info,
    load_data,
)
from utils.shared_utils import show_message


class InvalidIDError(Exception):
    "Custom exception for invalid ID file"


class DirModeError(Exception):
    "Custom exception for invalid DirectoryMode parameter"


class DirectoryMode(Enum):
    """Enumeration representing directory modes"""

    USER = auto()
    DEVELOPER = auto()


class InstallationState(Enum):
    """Enumeration representing installation states"""

    UNKNOWN = auto()  # currently used by setting directory manually
    NOT_STARTED = auto()
    IN_PROGRESS = auto()
    PAUSED = auto()
    COMPLETED = auto()
    CANCELLED = auto()


class GameManager:
    """Sub class of the game class

    Everything related to the game folder such as
        - installing, updating and repairing dev mode and switching between user & dev modes
        - retrieving game folder paths"""

    def __init__(self, persistent_data, game_instance):
        self.persistent_data = persistent_data
        self.steam_info = get_steam_info(self.persistent_data)
        self.valid_modes = ["user", "dev"]
        # avoiding circular import by passing the game instance as a param here
        self.game = game_instance

        self.user_dir_id_file = "user_folder.DoNotDelete"
        self.dev_dir_id_file = "hud_dev_folder.DoNotDelete"

    def validate_mode_parameter(self, mode):
        "Validate mode parameter"
        print("Validating mode parameter (legacy TODO: replace with enum)...")
        if mode not in self.valid_modes:
            raise ValueError("Invalid mode parameter. Mode must be one of: user, dev")
        else:
            # print(f"Valid mode param: {mode}")
            return False

    def get_active_mode(self):
        """Check active game mode. User/Dev"""
        user_id_file_path = os.path.join(self.get_active_dir(), self.get_id_file_name(DirectoryMode.USER))
        dev_id_file_path = os.path.join(self.get_active_dir(), self.get_id_file_name(DirectoryMode.DEVELOPER))

        if os.path.isfile(user_id_file_path):
            print(f"{self.game.get_title()} is in user mode")
            return DirectoryMode.USER
        elif os.path.isfile(dev_id_file_path):
            print(f"{self.game.get_title()} is in dev mode")
            return DirectoryMode.DEVELOPER
        else:
            print(f"Default game folder not found! ({self.get_active_dir()})")
            return None

    def get_cfg_dir(self, dir_mode):
        """Get the full path to the 'cfg' dir"""
        print("Retrieving config directory...")

        try:
            self.validate_mode_parameter_enum(dir_mode)

            main_dir = self.get_main_dir(dir_mode)
            config_dir = os.path.join(main_dir, "cfg")

            if not os.path.exists(config_dir):
                raise FileNotFoundError(f"Config directory '{config_dir}' does not exist.")
            if not os.path.isdir(config_dir):
                raise NotADirectoryError(f"'{config_dir}' is not a directory.")

            print(f"Config directory: '{config_dir}'")
            return config_dir
        except (DirModeError, FileNotFoundError, NotADirectoryError) as err:
            print(f"Failed to retrieve config directory: {err}")
            return None

    def get_main_dir(self, dir_mode):
        """Get the full path to the main dir eg. 'Left 4 Dead 2\\left4dead2"""

        print("Retrieving main directory...")

        try:
            self.validate_mode_parameter_enum(dir_mode)

            root_dir = self.get_dir(dir_mode)
            main_dir_name = self.game.get_title().replace(" ", "")
            main_dir_name = main_dir_name.lower()  # python is case sensitive; convert to Left4Dead2 -> left4dead2
            main_dir = os.path.join(root_dir, main_dir_name)

            if not os.path.exists(main_dir):
                raise FileNotFoundError(f"Main directory '{main_dir}' does not exist.")
            if not os.path.isdir(main_dir):
                raise NotADirectoryError(f"'{main_dir}' is not a directory.")

            print(f"Main directory: '{main_dir}'")
            return main_dir
        except (DirModeError, FileNotFoundError, NotADirectoryError) as err:
            print(f"Failed to retrieve main directory: {err}")
            return None

    def get_active_dir(self):
        """Returns the active game directory regardless of mode"""
        active_dir = os.path.join(self.steam_info["game_dir"], self.game.get_title())
        print(f"Active directory: '{active_dir}'")
        return active_dir

    def validate_mode_parameter_enum(self, dir_mode):
        "Validate the dir_mode parameter"
        if not isinstance(dir_mode, DirectoryMode):
            raise DirModeError("Invalid dir_mode parameter. It should be a DirectoryMode enum value.")

    def get_id_file_name(self, dir_mode):
        "Retrieve ID file name"

        try:
            self.validate_mode_parameter_enum(dir_mode)

            # Map modes to their corresponding ID files using a dictionary
            id_files = {DirectoryMode.USER: self.user_dir_id_file, DirectoryMode.DEVELOPER: self.dev_dir_id_file}
            id_file_name = id_files.get(dir_mode, None)

            if id_file_name is None:
                print(f"No ID file found for {dir_mode.name} mode.")
            else:
                print(f"Retrieved {dir_mode.name} ID file name: {id_file_name}")

            return id_file_name
        except DirModeError as err_info:
            print(f"Failed to retrieve file id name: {err_info}")
            return None

    def write_id_file(self, dir_mode, directory, installation_state=None):
        "Write installation state to ID file"

        # Validate dir_mode
        if not isinstance(dir_mode, DirectoryMode):
            print("Invalid directory mode provided.")
            return False

        # Validate installation_state for DEVELOPER mode
        if dir_mode == DirectoryMode.DEVELOPER and installation_state is None:
            print("For DEVELOPER mode, installation state must be specified.")
            return False

        # Validate installation_state if provided
        if installation_state is not None and not isinstance(installation_state, InstallationState):
            print("Invalid installation state provided.")
            return False

        # Retrieve ID file
        id_file = self.get_id_file_name(dir_mode)  # Use dir_mode.name as part of ID
        if id_file is None:
            print("Cancelled writing ID file. Could not retrieve ID file name")
            return False
        else:
            # Construct installation state data
            state_data = {
                "directory_mode": dir_mode.name,
                "installation_state": installation_state.name if installation_state is not None else None,
                "game_directory": directory,
            }

            # Write to disk
            id_file_path = os.path.join(directory, id_file)
            with open(id_file_path, "w", encoding="utf-8") as file_handle:
                json.dump(state_data, file_handle, indent=4)  # Write state data as JSON
            print(f"Wrote installation state to disk: '{id_file_path}'")
            return True

    def get_dir(self, dir_mode, manually_select_dir=True):
        "Retrieve the installation directory path for the specified mode, prompting manual selection if necessary."

        try:
            self.validate_mode_parameter_enum(dir_mode)

            id_file = self.get_id_file_name(dir_mode)
            if id_file is None:
                raise InvalidIDError("Invalid ID file!")

            steam_games_dir = self.steam_info["game_dir"]

            # Iterate through folders in the Steam games directory
            for folder_name in os.listdir(steam_games_dir):
                folder_path = os.path.join(steam_games_dir, folder_name)
                if os.path.isdir(folder_path):
                    id_path = os.path.join(folder_path, id_file)

                    # Check if the ID file exists in the folder & return it if found
                    if os.path.isfile(id_path):
                        return folder_path

            if not manually_select_dir:
                print(f"Not prompting to manually select {dir_mode} directory")
                return

            # If the ID file is not found, prompt the user to manually select the directory
            try:
                result = self.set_directory_manually(dir_mode)
                print(f"Game directory for {dir_mode}: '{result}'")
                return result
            except Exception as err_info:
                print(f"Failed to retrieve game directory for {dir_mode}. Information: {err_info}")
                return None
        except (DirModeError, InvalidIDError, FileNotFoundError, NotADirectoryError) as err:
            print(f"Failed to retrieve game directory for {dir_mode}: {err}")
            return None

    def set_directory_manually(self, dir_mode) -> str | None:
        "Manually set directory in case ID file is missing"

        # Validate dir_mode
        if not isinstance(dir_mode, DirectoryMode):
            print(f"Invalid directory mode provided for function: {self.set_directory_manually.__name__}")
            return None

        print(f"Manually setting directory for: {dir_mode.name}")

        # prompt user to manually select
        message = (
            f"Could not find ID file for the {dir_mode.name} installation directory.\n\n"
            "Is it installed and do you want to manually select it?\n"
            "If so - Be sure to select the correct directory!"
        )
        result = show_message(message, "yesno", SCRIPT_NAME)
        if not result:
            return None

        # manually select
        selected_dir = filedialog.askdirectory(
            mustexist=True, title=f"Select the {dir_mode.name} directory", initialdir=self.steam_info.get("game_dir")
        )
        if not os.path.isdir(selected_dir):
            raise NotADirectoryError(
                f"Could not find game installation directory for specified installation mode ({dir_mode.name})"
            )

        # prompt user about dev installation state
        if dir_mode == DirectoryMode.DEVELOPER:
            message = f"Is {dir_mode.name} mode fully installed?"
            is_fully_installed = show_message(message, "yesno", SCRIPT_NAME)
            if is_fully_installed:
                install_state = InstallationState.COMPLETED
            else:
                install_state = InstallationState.UNKNOWN

        # write selection
        if dir_mode == DirectoryMode.DEVELOPER:
            self.write_id_file(dir_mode, selected_dir, install_state)
        else:
            self.write_id_file(dir_mode, selected_dir)
        return selected_dir

    def swap_mode_folders(self, source_dir_mode, target_dir_mode):
        """Swap folders for mode activation"""
        try:
            self.validate_mode_parameter_enum(source_dir_mode)
            self.validate_mode_parameter_enum(target_dir_mode)

            os.rename(
                self.get_dir(source_dir_mode),
                os.path.join(
                    self.steam_info.get("game_dir"), f"backup_hud_{source_dir_mode.name}." + self.game.get_title()
                ),
            )
            os.rename(
                self.get_dir(target_dir_mode),
                os.path.join(self.steam_info.get("game_dir"), self.game.get_title()),
            )
        except DirModeError as err:
            print(f"Invalid mode parameter: {err}")
        except Exception as err_info:
            print(f"An error occurred during directory renaming: {err_info}")

    def activate_mode(self, dir_mode):
        """Activate user/dev mode by switching folder names eg. Left 4 Dead 2 & Left 4 Dead 2 User"""

        try:
            self.validate_mode_parameter_enum(dir_mode)

            if not self.is_installed(dir_mode):
                result = self.run_installer(manually_select_dir=False)
                if not result:
                    return False

            # check if mode is already active
            if self.get_active_mode() == dir_mode:
                return True

            # close game
            self.game.close()

            # activate mode
            if dir_mode == DirectoryMode.USER:
                self.swap_mode_folders(DirectoryMode.DEVELOPER, DirectoryMode.USER)
            else:
                self.swap_mode_folders(DirectoryMode.USER, DirectoryMode.DEVELOPER)
            return True
        except DirModeError as dir_err:
            print(f"Invalid mode parameter: {dir_err}")
        except Exception as err:
            print(f"An error occurred during mode activation: {err}")

    def is_installed(self, dir_mode, manually_select_dir=True):
        """Check if mode is installed"""

        try:
            self.validate_mode_parameter_enum(dir_mode)

            # Get the installation directory for the specified mode
            install_dir = self.get_dir(dir_mode, manually_select_dir)

            # Check if the install directory is empty
            if install_dir:
                print(f"{dir_mode.name} mode is installed!")
                return True
            else:
                print(f"{dir_mode.name} mode is not installed!")
                return False
        except DirModeError as dir_err:
            print(f"Invalid mode parameter: {dir_err}")
            return False

    def _prompt_start(self, install_type, message_extra=""):
        install_type = install_type.lower()  # Convert to lowercase

        # verify install type
        valid_modes = ["install", "update", "repair"]
        if install_type not in valid_modes:
            raise ValueError("Invalid mode parameter")

        # create message
        install_type_capitalized = install_type.capitalize()
        title = f"{install_type_capitalized} hud editing for {self.game.get_title()}?"
        disk_space = get_dir_size_in_gb(self.get_dir("user"))
        message = f"{title}\n\n"
        if message_extra:  # Check if the variable is not empty
            message += f"- {message_extra}\n"  # Add the extra line
        message += (
            "- This can take up to ~30 minutes depending on drive and processor speed\n"
            f"- This will use around {disk_space} of disk space (copy of the game folder)\n"
            "- Keep any L4D games closed during this process\n\n"
            "It is possible to cancel the setup at any time by closing the progress window"
        )

        # prompt message
        response = show_message(message, "yesno", title)  # Using "yesno" type for this confirmation

        return response

    def run_update_or_repair(self, update_or_repair):
        """Update or repair dev mode"""
        print(f"Running {update_or_repair}...")
        update_or_repair = update_or_repair.lower()  # lower case
        assert update_or_repair in ["update", "repair"], "Invalid mode parameter"

        # verify dev mode is already installed
        if not self.is_installed("dev"):
            messagebox.showinfo("Error", "Dev mode not installed!")
            return False

        # prompt continue
        if update_or_repair == "repair":
            if not self._prompt_start("repair", "This will re-extract every pak01_dir in the dev folder"):
                return False
        else:
            if not self._prompt_start("update", "Verifies the dev folder and re-extract only outdated pak01_dirs"):
                return False

        # close the game
        self.game.close()

        # activate dev mode
        self.activate_mode("dev")

        # re-enable paks
        self._enable_paks()

        # verify game installation
        if update_or_repair == "update":
            self._prompt_game_verified()

        # extract paks
        if update_or_repair == "repair":
            self._extract_outdated_paks()
        else:
            self._extract_paks()
        self._disable_paks()

        # install mods
        self._install_mods()

        # rebuild audio cache
        self._rebuild_audio()

        print(f"Finished {update_or_repair}!")

    def run_uninstaller(self):
        """Remove dev mode"""
        print("Running uninstaller...")

        # verify dev mode is already installed
        if not self.is_installed("dev"):
            messagebox.showinfo("Error", "Dev mode not installed!")
            return False

        # close the game
        self.game.close()

        # remove dev mode
        shutil.rmtree(self.get_dir("dev"))

        print("Uninstalled!")

    # manually_select_dir toggles manually selecting the folders. this prevents that prompt showing multiple times
    #   for example in this instance it would prompt during is_installed and is_installed is also called in
    #   run_installer
    #
    #       if not self.is_installed(mode):
    #           result = self.run_installer(manually_select_dir=False)
    #           if not result:
    #               return False
    def run_installer(self, manually_select_dir=True):
        """Runs the installer and throws errors on failure"""
        print("Running installer...")

        try:
            result = self._perform_installation(manually_select_dir)

            if result:
                print("Installed!")
                return True
            else:
                print("Not installed!")
                return False
        except Exception as err_info:
            print(f"Install cancelled: {err_info}")
            return False

    def _perform_installation(self, manually_select_dir=True):
        # verify the user installation is available
        if not self.is_installed("user"):
            raise AssertionError("User installation not found. Unable to install")

        # verify dev mode isn't already installed
        if self.is_installed("dev", manually_select_dir):
            messagebox.showinfo("Error", "Already installed!")
            return True

        # delete the dev folder for debugging purposes only
        # if DEBUG_MODE and os.path.isdir(self.get_dir("dev")):
        #     self.activate_mode("user")
        #     shutil.rmtree(self.get_dir("dev"))
        #     print('debug mode: successfully deleted the dev folder')

        # close the game
        self.game.close()

        # confirm install start
        if not self._prompt_start("install"):
            return False

        # 1. create dev folder template (folder & .exe) for detection incase of cancellation for cleanup
        self._create_dev_dir()

        # 2. copy the game files into and activate the dev folder
        self._copy_game_files()
        print("finished copying files")
        self.activate_mode("dev")

        # 3. steam verify = prompt to verify game install through steam to update and restore all game files
        self._prompt_game_verified()

        # 4. extract paks
        self._extract_paks()
        self._disable_paks()

        # 5. install mods
        self._install_mods()

        # 6. rebuild audio cache
        self._rebuild_audio()

        # finish installation
        input("press enter to successfully finish installation")
        return True

    def _create_dev_dir(self):
        print("Creating developer directory")
        game_user_dir = self.get_dir("user")
        game_dev_dir = os.path.join(self.steam_info.get("game_dir"), "backup_hud_dev." + self.game.get_title())
        game_exe_path = os.path.join(game_user_dir, self.game.get_exe())

        os.mkdir(game_dev_dir)
        shutil.copy(game_exe_path, game_dev_dir)
        self.write_id_file("dev", game_dev_dir, InstallationState.NOT_STARTED)

    def _copy_game_files(self):
        print("Copying game files into developer directory")
        copy_files_in_directory(self.get_dir("user"), self.get_dir("dev"), self.user_dir_id_file)

    def _prompt_game_verified(self):
        print("Prompting user to verify game")
        game_title = self.game.get_title()
        title = "Verify game files"

        message = (
            f"Verify game files for {game_title}\n\n"
            f"Steam -> Right-Click {game_title} -> Properties -> Local Files -> 'Verify integrity of game files'\n\n"
            "This will not affect your game installation. Only the copy that was just made\n\n"
            "Are you sure steam has finished verifying AND downloaded any missing files?"
        )

        response = show_message(message, "yesno", title)  # Using "yesno" type for this confirmation

        if response:
            # Ask a second time - are you really sure?
            confirm_message = (
                f"Are you REALLY sure steam has finished verifying AND"
                f" downloaded any missing files for {game_title}?"
            )
            response = show_message(confirm_message, "yesno", title)  # Using "yesno" type for this confirmation

            return response  # Response is already a boolean value
        else:
            return False

    def _find_pak_files(self, game_dir, callback):
        for subdir_name in os.listdir(game_dir):
            subdir_path = os.path.join(game_dir, subdir_name)
            if os.path.isdir(subdir_path):
                for filename in os.listdir(subdir_path):
                    if filename == "pak01_dir.vpk" or filename == "pak01_dir.vpk.disabled":
                        filepath = os.path.join(subdir_path, filename)
                        callback(filepath, subdir_path)

    def _extract_outdated_paks(self):
        """1. Confirm which pak01_dir.vpk files are outdated by checking for differences between the user & dev modes
        2. Extract all files from the outdated pak01_dir.vpk files to their respective root directories"""
        print("Extracting outdated pak01.vpk's")

        # retrieve pak files for user & dev modes
        dev_dir = self.get_dir("dev")
        user_dir = self.get_dir("user")

        user_paks = []
        dev_paks = []

        def get_user_paks_callback(filepath, output_dir):
            # vpk_class.extract(filepath, output_dir)
            print(f"filepath={filepath}\noutput_dir={output_dir}")
            pak_tuple = (filepath, output_dir)
            user_paks.append(pak_tuple)

        def get_dev_paks_callback(filepath, output_dir):
            # vpk_class.extract(filepath, output_dir)
            print(f"filepath={filepath}\noutput_dir={output_dir}")
            pak_tuple = (filepath, output_dir)
            dev_paks.append(pak_tuple)

        self._find_pak_files(user_dir, get_user_paks_callback)
        self._find_pak_files(dev_dir, get_dev_paks_callback)

        # extract any paks that are not identical between the user & dev folders
        i = 0
        for dev_pak in dev_paks:
            user_pak = user_paks[i]

            print(f'comparing "{dev_pak[0]}" to "{user_pak[0]}"')
            if not filecmp.cmp(dev_pak[0], user_pak[0]):
                print(f'pak out of date! extracting "{dev_pak[0]}"')
                vpk_class = VPKClass()
                vpk_class.extract(dev_pak[0], dev_pak[1])

            i += 1

    def _extract_paks(self):
        """Extract all files from the pak01_dir.vpk files located in the specified game directory
        to their respective root directories."""
        print("Extracting pak01.vpk's")
        dev_dir = self.get_dir("dev")

        def extract_callback(filepath, output_dir):
            vpk_class = VPKClass()
            vpk_class.extract(filepath, output_dir)

        self._find_pak_files(dev_dir, extract_callback)

    def _disable_paks(self):
        print("Disabling pak01.vpk's")
        dev_dir = self.get_dir("dev")

        def disable_callback(filepath, subdir_path):
            source_filepath = filepath
            target_filepath = os.path.join(subdir_path, "pak01_dir.vpk.disabled")
            os.rename(source_filepath, target_filepath)

        self._find_pak_files(dev_dir, disable_callback)

    def _enable_paks(self):
        print("Enabling pak01.vpk's")
        dev_dir = self.get_dir("dev")

        def enable_callback(filepath, subdir_path):
            source_filepath = filepath
            target_filepath = os.path.join(subdir_path, "pak01_dir.vpk")
            os.rename(source_filepath, target_filepath)
            print("Renaming file from", source_filepath, "to", target_filepath)

        self._find_pak_files(dev_dir, enable_callback)

    def _install_mods(self):
        print("Installing mods")
        mods_dev_map_dir = os.path.join(MODS_DIR, self.game.get_title(), "export")
        mods_addons_dir = os.path.join(MODS_DIR, "Addons", "Export")
        mods_sourcemod_dir = os.path.join(MODS_DIR, "SourceMod", "Export")
        main_dir = self.get_main_dir("dev")

        copy_files_in_directory(mods_dev_map_dir, main_dir)
        copy_files_in_directory(mods_addons_dir, main_dir)
        copy_files_in_directory(mods_sourcemod_dir, main_dir)

    def _rebuild_audio(self):
        print("Rebuilding audio")

        cfg_dir = self.get_cfg_dir("dev")
        valverc_path = os.path.join(cfg_dir, "valve.rc")

        with open(valverc_path, "w", encoding="utf-8") as file_handle:
            file_handle.write("mat_setvideomode 800 600 1 0; snd_rebuildaudiocache; exit")

        self.game.close()
        self.game.run("dev", "wait on close")
        print("Finished rebuilding audio")
        # Run, % STEAM_INFO.exePath A_Space "-applaunch " this.game.obj.appid " -novid -w 1 -h 1 -x 0 -y 0 -windowed"


# pylint: disable=unused-variable
def debug_installer_class():
    """Debug installer class"""
    os.system("cls")  # clear terminal

    saved_data = load_data()

    # game_manager_instance = Game(saved_data)
    # game_manager_instance.run_installer()

    input("end of class_installer autoexecute")

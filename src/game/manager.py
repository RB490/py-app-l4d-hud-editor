"""This module is a sub class of the game class.
functions related to the game folder such as switching between user/dev modes"""
# pylint: disable=broad-exception-caught
import filecmp
import json
import os
import shutil
from enum import Enum, auto
from tkinter import filedialog, messagebox

from utils.constants import MODS_DIR, SCRIPT_NAME
from utils.functions import (
    copy_files_in_directory,
    get_dir_size_in_gb,
    get_steam_info,
    load_data,
)
from utils.shared_utils import show_message
from utils.vpk import VPKClass


class InvalidIDError(Exception):
    "Custom exception for invalid ID file"


class InstallationError(Exception):
    """Custom exception for indicating installation errors."""


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
    CREATE_DEV_DIR = auto()
    COPYING_FILES = auto()
    VERIFYING_GAME = auto()
    EXTRACTING_PAKS = auto()
    INSTALLING_MODS = auto()
    REBUILDING_AUDIO = auto()
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
        # avoiding circular import by passing the game instance as a param here
        self.game = game_instance
        self.current_state = None  # current installation state

        self.user_dir_id_file = "user_folder.DoNotDelete"
        self.dev_dir_id_file = "hud_dev_folder.DoNotDelete"

    def get_active_mode(self):
        """Check active game mode. User/Dev"""
        try:
            if not self.is_installed(DirectoryMode.USER) and not self.is_installed(DirectoryMode.DEVELOPER):
                raise InstallationError("Application is not installed in any valid mode.")

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
        except InstallationError as err:
            print(f"Failed to determine active game mode: {err}")
            return None

    def get_cfg_dir(self, dir_mode):
        """Get the full path to the 'cfg' dir"""
        print("Retrieving config directory...")

        try:
            if not self.is_installed(dir_mode):
                raise InstallationError("Application is not installed in the specified mode.")

            self.validate_dir_mode(dir_mode)

            main_dir = self.get_main_dir(dir_mode)
            config_dir = os.path.join(main_dir, "cfg")

            if not os.path.exists(config_dir):
                raise FileNotFoundError(f"Config directory '{config_dir}' does not exist.")
            if not os.path.isdir(config_dir):
                raise NotADirectoryError(f"'{config_dir}' is not a directory.")

            print(f"Config directory: '{config_dir}'")
            return config_dir
        except (InstallationError, DirModeError, FileNotFoundError, NotADirectoryError) as err:
            print(f"Failed to retrieve config directory: {err}")
            return None

    def get_main_dir(self, dir_mode):
        """
        Get the full path to the main dir eg. 'Left 4 Dead 2\\left4dead2'

        Parameters:
            dir_mode (DirectoryMode): The directory mode to retrieve the main dir for.

        Returns:
            str or None: The full path to the main dir or None if an error occurs.
        """
        try:
            self.validate_dir_mode(dir_mode)

            # Get the installation directory path using get_dir
            root_dir = self.get_dir(dir_mode)
            if root_dir is None:
                print(f"Failed to retrieve installation directory for mode '{dir_mode}'.")
                return None
            main_dir_name = self.game.get_title().replace(" ", "")
            main_dir_name = main_dir_name.lower()  # python is case sensitive; convert to Left4Dead2 -> left4dead2
            main_dir = os.path.join(root_dir, main_dir_name)

            if not os.path.exists(main_dir):
                print(f"Main directory '{main_dir}' does not exist.")
                return None
            if not os.path.isdir(main_dir):
                print(f"'{main_dir}' is not a directory.")
                return None

            print(f"Main directory: '{main_dir}'")
            return main_dir
        except (DirModeError, FileNotFoundError, NotADirectoryError) as err:
            print(f"Failed to retrieve main directory: {err}")
            return None

    def get_active_dir(self):
        """Returns the active game directory regardless of mode"""
        try:
            if not self.is_installed(DirectoryMode.USER) and not self.is_installed(DirectoryMode.DEVELOPER):
                raise InstallationError("Application is not installed in any valid mode.")

            active_dir = os.path.join(self.steam_info["game_dir"], self.game.get_title())

            if not os.path.exists(active_dir):
                raise FileNotFoundError(f"Active directory '{active_dir}' does not exist.")
            if not os.path.isdir(active_dir):
                raise NotADirectoryError(f"'{active_dir}' is not a directory.")

            print(f"Active directory: '{active_dir}'")
            return active_dir
        except (InstallationError, FileNotFoundError, NotADirectoryError) as err:
            print(f"Failed to retrieve active directory: {err}")
            return None

    def validate_dir_mode(self, dir_mode):
        "Validate the dir_mode parameter"
        if not isinstance(dir_mode, DirectoryMode):
            raise DirModeError("Invalid dir_mode parameter. It should be a DirectoryMode enum value.")

    def get_installation_state(self, dir_mode):
        """
        Get the installation state of the application for the given directory mode.

        Parameters:
            dir_mode (DirectoryMode): The directory mode to retrieve the installation state for.

        Returns:
            InstallationState or None: The installation state or None if an error occurs.
        """
        try:
            # Check if the application is installed in the specified mode
            if not self.is_installed(dir_mode):
                raise InstallationError("Application is not installed in the specified mode.")

            # Get the name of the installation state file
            id_file = self.get_id_file_name(dir_mode)

            if id_file is not None:
                # Construct the path to the installation state file
                id_file_path = os.path.join(self.get_dir(dir_mode), id_file)

                if os.path.exists(id_file_path):
                    try:
                        # Read JSON data from the installation state file
                        with open(id_file_path, "r", encoding="utf-8") as file_handle:
                            state_data = json.load(file_handle)
                            installation_state_str = state_data.get("installation_state")

                            if installation_state_str:
                                # Convert string to InstallationState enum value
                                print(f"Installation state: {installation_state_str}")
                                return InstallationState[installation_state_str]
                    except (json.JSONDecodeError, KeyError):
                        pass

            # Default to UNKNOWN if installation state data is invalid or missing
            print(f"Invalid installation state data format! Defaulting to {InstallationState.UNKNOWN.name}")
            return InstallationState.UNKNOWN
        except (InstallationError, DirModeError) as err:
            # Handle installation and directory mode errors
            print(f"Failed to retrieve installation state: {err}")
            return None

    def get_id_file_name(self, dir_mode):
        "Retrieve ID file name"

        try:
            self.validate_dir_mode(dir_mode)

            # Map modes to their corresponding ID files using a dictionary
            id_files = {DirectoryMode.USER: self.user_dir_id_file, DirectoryMode.DEVELOPER: self.dev_dir_id_file}
            id_file_name = id_files.get(dir_mode, None)

            if id_file_name is None:
                print(f"No ID file found for {dir_mode.name} mode.")
            # else:
            #     print(f"Retrieved {dir_mode.name} ID file name: {id_file_name}")

            return id_file_name
        except DirModeError as err_info:
            print(f"Failed to retrieve file id name: {err_info}")
            return None

    def write_id_file(self, dir_mode, directory, installation_state=None):
        """
        Write installation state to ID file.

        Parameters:
            dir_mode (DirectoryMode): The directory mode to write the ID file for.
            directory (str): The directory where the ID file will be written.
            installation_state (InstallationState, optional): The installation state to be written.

        Returns:
            bool: True if writing was successful, False otherwise.
        """

        try:
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

            # Handle directory being None
            if directory is None:
                print("Directory is None. Cannot write ID file.")
                return False

            # Create directory if it doesn't exist
            if not os.path.exists(directory):
                os.makedirs(directory)
                print(f"Directory '{directory}' was created.")

            # Retrieve ID file
            id_file = self.get_id_file_name(dir_mode)  # Use dir_mode.name as part of ID
            if id_file is None:
                print("Cancelled writing ID file. Could not retrieve ID file name.")
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
                print(f"Wrote installation state ({installation_state.name}) to disk: '{id_file_path}'")
                return True
        except (InstallationError, DirModeError) as err:
            # Handle installation and directory mode errors
            print(f"Failed to write ID file: {err}")
            return False

    def get_dir(self, dir_mode):
        """
        Retrieve the installation directory path for the specified mode.

        Args:
            dir_mode (str): The mode for which the installation directory is being retrieved.

        Returns:
            str or None: The installation directory path if found, or None if not found.
        """
        try:
            # Validate the mode parameter
            self.validate_dir_mode(dir_mode)

            # Get the ID file name associated with the mode
            id_file = self.get_id_file_name(dir_mode)
            if id_file is None:
                raise InvalidIDError("Invalid ID file!")

            # Get the Steam games directory
            steam_games_dir = self.steam_info["game_dir"]

            # Search through folders in the Steam games directory
            for folder_name in os.listdir(steam_games_dir):
                folder_path = os.path.join(steam_games_dir, folder_name)
                if os.path.isdir(folder_path):
                    id_path = os.path.join(folder_path, id_file)
                    if os.path.isfile(id_path):
                        print(f"Found installation directory for mode '{dir_mode}': '{folder_path}'")
                        return folder_path

            print(f"No installation directory found for mode '{dir_mode}'.")
            return None
        except (DirModeError, InvalidIDError, FileNotFoundError, NotADirectoryError) as err_info:
            print(f"An error occurred while retrieving installation directory for mode '{dir_mode}': {err_info}")
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
        """
        Swap folders for mode activation.

        Parameters:
            source_dir_mode (DirectoryMode): The directory mode to swap from.
            target_dir_mode (DirectoryMode): The directory mode to swap to.

        Returns:
            bool: True if swapping was successful, False otherwise.
        """
        try:
            # Validate dir modes
            self.validate_dir_mode(source_dir_mode)
            self.validate_dir_mode(target_dir_mode)

            # Check if the application is installed in the specified modes
            if not self.is_installed(source_dir_mode) or not self.is_installed(target_dir_mode):
                raise InstallationError("Application is not installed in the specified modes.")

            # Rename folders to perform the swap
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
            return True
        except (InstallationError, DirModeError) as err:
            # Handle installation and directory mode errors
            print(f"Failed to swap mode folders: {err}")
            return False
        except Exception as err_info:
            # Handle other exceptions that might occur during renaming
            print(f"An error occurred during directory renaming: {err_info}")
            return False

    def activate_mode(self, dir_mode):
        """
        Activate user/dev mode by switching folder names eg. Left 4 Dead 2 & Left 4 Dead 2 User.

        Parameters:
            dir_mode (DirectoryMode): The directory mode to activate.

        Returns:
            bool: True if activation was successful, False otherwise.
        """
        try:
            # Check if the application is installed in the specified mode
            if not self.is_installed(dir_mode):
                raise InstallationError("Application is not installed in the specified mode.")

            # Validate dir mode
            self.validate_dir_mode(dir_mode)

            # Check if the mode is already active
            if self.get_active_mode() == dir_mode:
                return True

            # Close the game before activation
            self.game.close()

            # Activate the mode by swapping folders
            if dir_mode == DirectoryMode.USER:
                self.swap_mode_folders(DirectoryMode.DEVELOPER, DirectoryMode.USER)
            else:
                self.swap_mode_folders(DirectoryMode.USER, DirectoryMode.DEVELOPER)
            return True
        except (InstallationError, DirModeError) as err:
            # Handle installation and directory mode errors
            print(f"Failed to activate mode: {err}")
            return False
        except Exception as err_info:
            # Handle other exceptions that might occur during activation
            print(f"An error occurred during mode activation: {err_info}")
            return False

    def is_installed(self, dir_mode):
        """Check if mode is installed"""

        try:
            self.validate_dir_mode(dir_mode)

            # Get the installation directory for the specified mode
            install_dir = self.get_dir(dir_mode)

            # Only check main_dir if install_dir was successfully retrieved
            if install_dir:
                self.get_main_dir(dir_mode)  # in case it's the wrong game folder

                # Check if the install directory is empty
                if install_dir:
                    print(f"{dir_mode.name} mode is installed!")
                    return True
                else:
                    print(f"{dir_mode.name} mode is not installed!")
                    return False
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
        disk_space = get_dir_size_in_gb(self.get_dir(DirectoryMode.USER))
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
        if not self.is_installed(DirectoryMode.DEVELOPER):
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
        self.activate_mode(DirectoryMode.DEVELOPER)

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
        if not self.is_installed(DirectoryMode.DEVELOPER):
            messagebox.showinfo("Error", "Dev mode not installed!")
            return False

        # close the game
        self.game.close()

        # remove dev mode
        print("Deleting game directory...")
        shutil.rmtree(self.get_dir(DirectoryMode.DEVELOPER))

        print("Uninstalled!")

    def run_installer(self):
        """Runs the installer and throws errors on failure"""
        print("Running installer...")

        try:
            result = self._perform_installation()

            if result:
                print("Installed!")
                return True
            else:
                print("Not installed!")
                return False
        except Exception as err_info:
            self.write_id_file(
                DirectoryMode.DEVELOPER, self.get_dir(DirectoryMode.DEVELOPER), InstallationState.CANCELLED
            )
            print(f"Install cancelled: {err_info}")
            return False

    def _perform_installation(self):
        self.current_state = self.get_installation_state(DirectoryMode.DEVELOPER)

        if not self.is_installed(DirectoryMode.USER):
            raise AssertionError("User installation not found. Unable to install")

        if self.is_installed(DirectoryMode.DEVELOPER):
            raise AssertionError("Developer installation already installed!")

        self.game.close()
        if not self._prompt_start("install"):
            return False

        self.resume_installation(self.current_state)
        return True

    def resume_installation(self, resume_state):
        "resume"
        installation_steps = [
            InstallationState.CREATE_DEV_DIR,
            InstallationState.COPYING_FILES,
            InstallationState.VERIFYING_GAME,
            InstallationState.EXTRACTING_PAKS,
            InstallationState.INSTALLING_MODS,
            InstallationState.REBUILDING_AUDIO,
        ]

        start_resume = False

        print(f"Resuming installation with state: {resume_state}")

        for state in installation_steps:
            if start_resume or state == resume_state:
                self.perform_installation_step(state)
                start_resume = True

        self.current_state = InstallationState.COMPLETED
        self.write_id_file(DirectoryMode.DEVELOPER, self.get_dir(DirectoryMode.DEVELOPER), InstallationState.COMPLETED)

    def perform_installation_step(self, state):
        "perform"
        print(f"Performing installation step with state: {state}")

        if state == InstallationState.CREATE_DEV_DIR:
            self._create_dev_dir()
        elif state == InstallationState.COPYING_FILES:
            self._copy_game_files()
            self.activate_mode(DirectoryMode.DEVELOPER)
        elif state == InstallationState.VERIFYING_GAME:
            self._prompt_game_verified()
        elif state == InstallationState.EXTRACTING_PAKS:
            self._extract_paks()
            self._disable_paks()
        elif state == InstallationState.INSTALLING_MODS:
            self._install_mods()
        elif state == InstallationState.REBUILDING_AUDIO:
            self._rebuild_audio()

        # Update the current state to the completed state
        self.current_state = state

    def _create_dev_dir(self):
        print("Creating developer directory")

        game_user_dir = self.get_dir(DirectoryMode.USER)
        game_dev_dir = os.path.join(self.steam_info.get("game_dir"), "backup_hud_dev." + self.game.get_title())
        game_exe_path = os.path.join(game_user_dir, self.game.get_exe())

        os.mkdir(game_dev_dir)
        shutil.copy(game_exe_path, game_dev_dir)

        self.write_id_file(DirectoryMode.DEVELOPER, game_dev_dir, InstallationState.CREATE_DEV_DIR)
        return

    def _copy_game_files(self):
        print("Copying game files into developer directory")
        self.write_id_file(
            DirectoryMode.DEVELOPER, self.get_dir(DirectoryMode.DEVELOPER), InstallationState.COPYING_FILES
        )
        copy_files_in_directory(
            self.get_dir(DirectoryMode.USER), self.get_dir(DirectoryMode.DEVELOPER), self.user_dir_id_file
        )

    def _prompt_game_verified(self):
        print("Prompting user to verify game")
        self.write_id_file(
            DirectoryMode.DEVELOPER, self.get_dir(DirectoryMode.DEVELOPER), InstallationState.VERIFYING_GAME
        )
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
        dev_dir = self.get_dir(DirectoryMode.DEVELOPER)
        user_dir = self.get_dir(DirectoryMode.USER)

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
        self.write_id_file(
            DirectoryMode.DEVELOPER, self.get_dir(DirectoryMode.DEVELOPER), InstallationState.EXTRACTING_PAKS
        )

        dev_dir = self.get_dir(DirectoryMode.DEVELOPER)

        def extract_callback(filepath, output_dir):
            vpk_class = VPKClass()
            vpk_class.extract(filepath, output_dir)

        self._find_pak_files(dev_dir, extract_callback)

    def _disable_paks(self):
        print("Disabling pak01.vpk's")
        dev_dir = self.get_dir(DirectoryMode.DEVELOPER)

        def disable_callback(filepath, subdir_path):
            source_filepath = filepath
            target_filepath = os.path.join(subdir_path, "pak01_dir.vpk.disabled")
            os.rename(source_filepath, target_filepath)

        self._find_pak_files(dev_dir, disable_callback)

    def _enable_paks(self):
        print("Enabling pak01.vpk's")
        dev_dir = self.get_dir(DirectoryMode.DEVELOPER)

        def enable_callback(filepath, subdir_path):
            source_filepath = filepath
            target_filepath = os.path.join(subdir_path, "pak01_dir.vpk")
            os.rename(source_filepath, target_filepath)
            print("Renaming file from", source_filepath, "to", target_filepath)

        self._find_pak_files(dev_dir, enable_callback)

    def _install_mods(self):
        print("Installing mods")
        self.write_id_file(
            DirectoryMode.DEVELOPER, self.get_dir(DirectoryMode.DEVELOPER), InstallationState.INSTALLING_MODS
        )

        mods_dev_map_dir = os.path.join(MODS_DIR, self.game.get_title(), "export")
        mods_addons_dir = os.path.join(MODS_DIR, "Addons", "Export")
        mods_sourcemod_dir = os.path.join(MODS_DIR, "SourceMod", "Export")
        main_dir = self.get_main_dir(DirectoryMode.DEVELOPER)

        copy_files_in_directory(mods_dev_map_dir, main_dir)
        copy_files_in_directory(mods_addons_dir, main_dir)
        copy_files_in_directory(mods_sourcemod_dir, main_dir)

    def _rebuild_audio(self):
        print("Rebuilding audio")
        self.write_id_file(
            DirectoryMode.DEVELOPER, self.get_dir(DirectoryMode.DEVELOPER), InstallationState.REBUILDING_AUDIO
        )

        cfg_dir = self.get_cfg_dir(DirectoryMode.DEVELOPER)
        valverc_path = os.path.join(cfg_dir, "valve.rc")

        with open(valverc_path, "w", encoding="utf-8") as file_handle:
            file_handle.write("mat_setvideomode 800 600 1 0; snd_rebuildaudiocache; exit")

        self.game.close()
        self.game.run(DirectoryMode.DEVELOPER, "wait on close")
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

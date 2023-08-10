"""This module is a sub class of the game class.
functions related to the game folder such as switching between user/dev modes"""
import filecmp
import os
import shutil
import sys
from tkinter import filedialog
from tkinter import messagebox
import easygui
from packages.classes.vpk import VPKClass
from packages.utils.constants import DEBUG_MODE, MODS_DIR, SCRIPT_NAME
from packages.utils.functions import copy_directory_contents, get_dir_size_in_gb, get_steam_info, load_data


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

        self.user_dir_id_file = "user_folder.DoNotDelete"
        self.dev_dir_id_file = "hud_dev_folder.DoNotDelete"

    def get_active_mode(self):
        """Check active game mode. User/Dev"""
        user_id_file_path = os.path.join(self.get_active_dir(), self.user_dir_id_file)
        dev_id_file_path = os.path.join(self.get_active_dir(), self.dev_dir_id_file)
        # print(f'user_id_file_path "{user_id_file_path}"')
        # print(f'dev_id_file_path "{dev_id_file_path}"')

        if os.path.isfile(user_id_file_path):
            # print(f"{self.game.get_title()} is in user mode")
            return "user"
        elif os.path.isfile(dev_id_file_path):
            # print(f"{self.game.get_title()} is in dev mode")
            return "dev"
        else:
            print(f"Default game folder not found! ({self.get_active_dir()})")
            # messagebox.showinfo("Error", "Default game folder not found!")

    def get_cfg_dir(self, mode):
        """Get the full path to the 'cfg' dir"""
        main_dir = self.get_main_dir(mode)
        return os.path.join(main_dir, "cfg")

    def get_main_dir(self, mode):
        """Get the full path to the main dir eg. 'Left 4 Dead 2\\left4dead2"""
        root_dir = self.get_dir(mode)
        main_dir_name = self.game.get_title().replace(" ", "")
        main_dir_name = main_dir_name.lower()  # python is case sensitive; convert to Left4Dead2 -> left4dead2
        return os.path.join(root_dir, main_dir_name)

    def get_active_dir(self):
        """Returns the active game directory regardless of mode"""
        return os.path.join(self.steam_info["game_dir"], self.game.get_title())

    def get_dir(self, mode):
        """Get the full path to the specified mode's directory. If not found prompts to manually select"""
        match mode:
            case "user":
                installation_id_file = self.user_dir_id_file
            case "dev":
                installation_id_file = self.dev_dir_id_file
            case _:
                raise ValueError("Invalid mode parameter")

        steam_games_dir = self.steam_info["game_dir"]
        for folder_name in os.listdir(steam_games_dir):
            folder_path = os.path.join(steam_games_dir, folder_name)
            if os.path.isdir(folder_path):
                installation_id_file_path = os.path.join(folder_path, installation_id_file)
                if os.path.isfile(installation_id_file_path):
                    return folder_path

        # could not find the id file for specified mode - prompt to manually select
        message = (
            f"Could not find id file for the {mode} installation directory.\n\n\n\n"
            "Manually select it? If so - Be sure to select the correct directory!"
        )
        choices = ["Yes", "No"]
        response = easygui.buttonbox(message, title=SCRIPT_NAME, choices=choices)
        if response == "No":
            return False
        folder_path = filedialog.askdirectory(
            mustexist=True, title=f"Select the {mode} directory", initialdir=self.steam_info.get("game_dir")
        )
        if not os.path.isdir(folder_path):
            raise NotADirectoryError(
                f"Could not find game installation directory for specified installation mode ({mode})"
            )
        id_file_path = os.path.join(folder_path, installation_id_file)
        with open(id_file_path, "w", encoding="utf-8") as file_handle:
            file_handle.write(id_file_path)
        return folder_path

    def activate_mode(self, mode):
        """Activate user/dev mode by switching folder names eg. Left 4 Dead 2 & Left 4 Dead 2 User"""
        assert self.is_installed(mode), f"Called activate_mode to activate {mode} mode without it being installed"

        # check if mode is already active
        if self.get_active_mode() == mode:
            return

        # close game
        self.game.close()

        # activate mode
        try:
            if mode == "user":
                os.rename(
                    self.get_dir("dev"),
                    os.path.join(self.steam_info.get("game_dir"), "backup_hud_dev." + self.game.get_title()),
                )
                os.rename(self.get_dir("user"), os.path.join(self.steam_info.get("game_dir"), self.game.get_title()))
            elif mode == "dev":
                os.rename(
                    self.get_dir("user"),
                    os.path.join(self.steam_info.get("game_dir"), self.game.get_title() + " User"),
                )
                os.rename(self.get_dir("dev"), os.path.join(self.steam_info.get("game_dir"), self.game.get_title()))
            else:
                raise ValueError("Invalid mode parameter")
        except RuntimeError as err_info:
            print(f"An error occurred during directory renaming: {err_info}")

    def is_installed(self, mode):
        """Check if mode is installed"""
        assert mode in ["user", "dev"], "Invalid mode parameter"

        # confirm this is the correct directory by checking the game's executable
        install_dir = self.get_dir(mode)
        if os.path.isfile(os.path.join(install_dir, self.game.get_exe())):
            return True
        elif mode == "dev":
            # install dev mode if needed
            if self.run_installer() is False:
                raise RuntimeError("Can't continue without dev mode installed!'")
            return True
        else:
            raise RuntimeError(f"Game executable for {mode} mode not found in directory: '{install_dir}'")

    def _prompt_start(self, install_type, message_extra=""):
        install_type = install_type.lower()  # lower case
        assert install_type in ["install", "update", "repair"], "Invalid mode parameter"

        title = f"{install_type} hud editing for {self.game.get_title()}?".capitalize()
        disk_space = get_dir_size_in_gb(self.get_dir("user"))
        message = (
            f"{title}\n\n"
            f"- {message_extra}\n"
            "- This can take up to ~30 minutes depending on drive and processor speed\n"
            f"- This will use around {disk_space} of disk space (copy of the game folder)\n"
            "- Keep any L4D games closed during this process\n\n"
            "It is possible to cancel the setup at any time by closing the progress window"
        )

        choices = ["Yes", "No"]
        response = easygui.buttonbox(message, title=title, choices=choices)
        if response == "Yes":
            return True
        elif response == "No":
            return False
        else:
            return False

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

    def run_installer(self):
        """Runs the installer and throws errors on failure"""
        print("Running installer...")
        if DEBUG_MODE:
            if not self._perform_installation():
                raise RuntimeError("Installation cancelled!")
        else:
            try:
                self._perform_installation()
            except RuntimeError as err_info:
                messagebox.showerror(
                    "Error", str(err_info) + "\n\nInstallation cancelled! Currently unhandled. Closing."
                )
                sys.exit()
        print("Installed!")

    def _perform_installation(self):
        # verify the user installation is available
        if not self.is_installed("user"):
            raise AssertionError("User installation not found. Unable to install")

        # verify dev mode isn't already installed
        if self.is_installed("dev"):
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
        dev_id_file_path = os.path.join(game_dev_dir, self.dev_dir_id_file)

        os.mkdir(game_dev_dir)
        shutil.copy(game_exe_path, game_dev_dir)
        with open(dev_id_file_path, "w", encoding="utf-8") as file_handle:
            file_handle.write(dev_id_file_path)

    def _copy_game_files(self):
        print("Copying game files into developer directory")
        copy_directory_contents(self.get_dir("user"), self.get_dir("dev"), self.user_dir_id_file)

    def _prompt_game_verified(self):
        print("Prompting user to verify game")
        title = f"Verify integrity of games files for {self.game.get_title()} in steam"
        message = (
            f"Verify integrity of games files for {self.game.get_title()} in steam\n\n"
            f"Right-Click {self.game.get_title()} -> Properties -> Local Files -> 'Verify integrity of games files'\n"
            "This will not affect your game installation. Only the copy that was just made\n\n"
            "Are you sure Steam has finished verifying AND downloaded any missing files?"
        )

        choices = ["Yes", "No"]
        response = easygui.buttonbox(message, title=title, choices=choices)
        if response == "Yes":
            pass
        elif response == "No":
            return False
        else:
            return False

        # ask a second time - are you really sure?
        message = (
            f"Are you REALLY sure Steam has finished verifying AND"
            f"downloaded any missing files for {self.game.get_title()}?"
        )
        response = easygui.buttonbox(message, title=title, choices=choices)
        if response == "Yes":
            return True
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

        copy_directory_contents(mods_dev_map_dir, main_dir)
        copy_directory_contents(mods_addons_dir, main_dir)
        copy_directory_contents(mods_sourcemod_dir, main_dir)

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

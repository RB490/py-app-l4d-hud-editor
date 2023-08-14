# pylint: disable=protected-access
import json
import os
from tkinter import filedialog

from game_v2.game_v2 import ID_FILE_NAMES, DirectoryMode, InstallationState
from utils.constants import SCRIPT_NAME
from utils.shared_utils import show_message


class GameV2Dir:
    def __init__(self, game_class):
        self.game = game_class
        self.persistent_data = self.game.persistent_data

        print(self.__class__.__name__)

    def __get_mode_dir(self, dir_mode):
        self.game._validate_dir_mode(dir_mode)
        mode_dir = self.get(dir_mode)

        if mode_dir is None or not os.path.exists(mode_dir):
            print(f"Error: Directory '{mode_dir}' does not exist. Unable to construct path.")
            return None
        return mode_dir

    def set(self, dir_mode):
        # verify mode is installed
        if not self.__get_mode_dir(dir_mode):
            print("Application is not installed in the specified mode.")
            return False

        # close game
        self.game.close()

        # activate mode by swapping folders if needed
        if dir_mode == DirectoryMode.USER:
            self.__swap_mode_folders(DirectoryMode.DEVELOPER, DirectoryMode.USER)
        else:
            self.__swap_mode_folders(DirectoryMode.USER, DirectoryMode.DEVELOPER)
        return True

    def __swap_mode_folders(self, source_dir_mode, target_dir_mode):
        # set variables
        target_dir = os.path.join(self.game.steam.get_games_dir(), self.game.get_title())
        old_target_dir = self.get(target_dir_mode)

        # do we need to swap?
        if old_target_dir is target_dir:
            print(f"{target_dir_mode.name} already active!")
            return

        # swap folders
        os.rename(
            self.get(source_dir_mode),
            os.path.join(
                self.game.steam.get_games_dir(), f"backup_hud_{source_dir_mode.name}." + self.game.get_title()
            ),
        )
        os.rename(
            self.get(target_dir_mode),
            os.path.join(target_dir),
        )

    def __get_active(self):
        active_dir = os.path.join(self.game.steam.get_games_dir(), self.game.get_title())

        if not os.path.isdir(active_dir):
            print(f"Active directory '{active_dir}' does not exist.")
            return None
        else:
            return active_dir

    def get(self, dir_mode):
        # set variables
        self.game._validate_dir_mode(dir_mode)
        id_filename = self.get_id_filename(dir_mode)
        steam_games_dir = self.game.steam.get_games_dir()

        # Search through folders in the Steam games directory
        for folder_name in os.listdir(steam_games_dir):
            folder_path = os.path.join(steam_games_dir, folder_name)
            if os.path.isdir(folder_path):
                id_path = os.path.join(folder_path, id_filename)
                if os.path.isfile(id_path):
                    print(f"Found installation directory for mode '{dir_mode}': '{folder_path}'")
                    return folder_path

        print(f"No installation directory found for mode '{dir_mode}'.")
        return None

    def get_id_filename(self, dir_mode):
        self.game._validate_dir_mode(dir_mode)
        return ID_FILE_NAMES[dir_mode]

    def __get_id_path(self, dir_mode):
        mode_dir = self.__get_mode_dir(dir_mode)
        if mode_dir is None:
            print(f"Error: Directory '{mode_dir}' does not exist. Unable to construct ID path.")

            # prompt user to manually select it
            id_path = self.__set_id_location(dir_mode)
            if id_path is None:
                print(f"Error: Directory '{mode_dir}' does not exist. Unable to construct ID path.")
                return None
        else:
            id_path = os.path.join(mode_dir, self.get_id_filename(dir_mode))

        print("ID Path:", id_path)
        return id_path

    def set_id_content(self, dir_mode, installation_state):
        self.game._validate_dir_mode(dir_mode)

        # get id path
        id_path = self.__get_id_path(dir_mode)
        if id_path is None:
            return None

        self.__write_id_content(dir_mode, self.get(dir_mode), installation_state)

        print(f"result={id_path}")

    def __write_id_content(self, dir_mode, directory, installation_state=None):
        state_data = {
            "directory_mode": dir_mode.name,
            "installation_state": installation_state.name if installation_state is not None else None,
            "game_directory": directory,
        }

        id_file_name = self.get_id_filename(dir_mode)
        id_file_path = os.path.join(directory, id_file_name)
        with open(id_file_path, "w", encoding="utf-8") as file_handle:
            json.dump(state_data, file_handle, indent=4)  # Write state data as JSON

    def __set_id_location(self, dir_mode):
        self.game._validate_dir_mode(dir_mode)

        print(f"Manually setting directory for: {dir_mode.name}")

        # prompt user to manually select
        message = (
            f"Could not find ID file for the {dir_mode.name} installation directory.\n\n"
            "Is it installed and do you want to manually select it?\n"
            "If so - Be sure to select the correct directory!"
        )
        result = show_message(message, "yesno", SCRIPT_NAME)
        if not result:
            print(f"Could not set ID location for {dir_mode.name}")
            return None

        # manually select
        target_dir = filedialog.askdirectory(
            mustexist=True, title=f"Select the {dir_mode.name} directory", initialdir=self.game.steam.get_games_dir
        )
        if not os.path.isdir(target_dir):
            print(f"Could not set ID location for {dir_mode.name}")
            return None

        # prompt user about dev installation state
        if dir_mode == DirectoryMode.DEVELOPER:
            message = f"Is {dir_mode.name} mode fully installed?"
            is_fully_installed = show_message(message, "yesno", SCRIPT_NAME)
            if is_fully_installed:
                install_state = InstallationState.COMPLETED
            else:
                install_state = InstallationState.UNKNOWN
        else:
            install_state = InstallationState.UNKNOWN

        # write selection
        self.__write_id_content(dir_mode, target_dir, install_state)
        return True

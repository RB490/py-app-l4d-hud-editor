# pylint: disable=protected-access
import json
import os
from tkinter import filedialog

from game.game_constants import ID_FILE_NAMES, DirectoryMode, InstallationState
from utils.constants import SCRIPT_NAME
from utils.shared_utils import show_message


class GameIDHandler:
    def __init__(self, game_class):
        self.game = game_class

        print(self.__class__.__name__)

    def set_id_location(self, dir_mode):
        self.game._validate_dir_mode(dir_mode)

        print(f"Manually setting directory for: {dir_mode.name}")

        message = (
            f"Could not find ID file for the {dir_mode.name} installation directory.\n\n"
            "Is it installed and do you want to manually select it?\n"
            "If so - Be sure to select the correct directory!"
        )
        result = show_message(message, "yesno", SCRIPT_NAME)
        if not result:
            print(f"Could not set ID location for {dir_mode.name}")
            return None

        target_dir = filedialog.askdirectory(
            mustexist=True, title=f"Select the {dir_mode.name} directory", initialdir=self.game.steam.get_games_dir
        )
        if not os.path.isdir(target_dir):
            print(f"Could not set ID location for {dir_mode.name}")
            return None

        if dir_mode == DirectoryMode.DEVELOPER:
            message = f"Is {dir_mode.name} mode fully installed?"
            is_fully_installed = show_message(message, "yesno", SCRIPT_NAME)
            if is_fully_installed:
                install_state = InstallationState.COMPLETED
            else:
                install_state = InstallationState.UNKNOWN
        else:
            install_state = InstallationState.COMPLETED

        self.__write_id_content(dir_mode, install_state)
        return True

    def _set_id_content(self, dir_mode, installation_state):
        self.game._validate_dir_mode(dir_mode)

        id_path = self.__get_id_path(dir_mode)
        if id_path is None:
            return None

        state_data = {
            "directory_mode": dir_mode.name,
            "installation_state": installation_state.name if installation_state is not None else None,
            "game_directory": self.game.get(dir_mode),
        }

        self.__write_id_content(id_path, state_data)
        print(f"Wrote content to: '{id_path}'")

    def __get_id_path(self, dir_mode):
        mode_dir = self.game.get(dir_mode)
        if mode_dir is None:
            print(f"Error: Directory '{mode_dir}' does not exist. Unable to construct ID path.")
            return None
        id_path = os.path.join(mode_dir, self._get_id_filename(dir_mode))
        print("ID Path:", id_path)
        return id_path

    def write_installation_state(self, dir_mode, installation_state):
        self.game._validate_dir_mode(dir_mode)

        id_path = self.__get_id_path(dir_mode)
        if id_path is None:
            return None

        state_data = self.__read_id_content(id_path)
        state_data["installation_state"] = installation_state.name if installation_state is not None else None

        self.__write_id_content(id_path, state_data)
        print(f"Updated installation state in ID file: '{id_path}'")

    def write_sync_state(self, dir_mode, sync_state):
        self.game._validate_dir_mode(dir_mode)

        id_path = self.__get_id_path(dir_mode)
        if id_path is None:
            return None

        state_data = self.__read_id_content(id_path)
        state_data["sync_state"] = sync_state

        self.__write_id_content(id_path, state_data)
        print(f"Updated sync state in ID file: '{id_path}'")

    def __read_id_content(self, id_path):
        if os.path.isfile(id_path):
            with open(id_path, "r", encoding="utf-8") as file_handle:
                return json.load(file_handle)
        else:
            return {}

    def __write_id_content(self, id_path, state_data):
        with open(id_path, "w", encoding="utf-8") as file_handle:
            json.dump(state_data, file_handle, indent=4)
        print(f"Written ID content to: {id_path}")

    def _get_id_filename(self, dir_mode):
        self.game._validate_dir_mode(dir_mode)
        return ID_FILE_NAMES[dir_mode]


# Example usage:
# game = YourGameClass()  # Replace with your actual game class instantiation
# id_handler = IDFileHandler(game)
# id_handler.set_id_location(DirectoryMode.DEVELOPER)
# id_handler.write_installation_state(DirectoryMode.DEVELOPER, InstallationState.COMPLETED)
# id_handler.write_sync_state(DirectoryMode.DEVELOPER, "synced")
# etc.


def debug_id_handler(persistent_data):
    # game_class = Game(persistent_data)
    # game_class.dir.id.set_id_location(DirectoryMode.DEVELOPER)
    print(persistent_data)

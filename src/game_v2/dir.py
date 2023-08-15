"Game class directory methods"
# pylint: disable=protected-access
import json
import os
from tkinter import filedialog

from game_v2.game_v2 import ID_FILE_NAMES, DirectoryMode, InstallationState
from utils.constants import SCRIPT_NAME
from utils.functions import generate_random_string, rename_with_timeout
from utils.shared_utils import show_message


class GameV2Dir:
    "Game class directory methods"

    def __init__(self, game_class):
        self.game = game_class
        self.persistent_data = self.game.persistent_data

        print(self.__class__.__name__)

    def set(self, dir_mode):
        "Set directory to mode"
        self.game._validate_dir_mode(dir_mode)
        print(f"Setting mode: {dir_mode.name}")

        # note: retrieving source & target dir with self.get also already checks whether they are installed
        rename_timeout = 3
        # variables - source
        source_mode = DirectoryMode.USER if dir_mode == DirectoryMode.DEVELOPER else DirectoryMode.DEVELOPER
        source_dir = self.get(source_mode)
        random_string = generate_random_string()
        source_dir_backup = os.path.join(
            self.game.steam.get_games_dir(), f"_backup_hud_{source_mode.name}.{self.game.get_title()}_{random_string}"
        )
        # variables - target
        target_mode = dir_mode
        target_dir = self.get(target_mode)
        vanilla_dir = self.__get_vanilla()

        # do we need to swap?
        if os.path.samefile(target_dir, vanilla_dir):
            print(f"{target_mode.name} already active!")
            return True

        # close game
        self.game.close()

        # backup source mode
        print(f"Renaming {source_dir} -> {source_dir_backup}")
        if not rename_with_timeout(source_dir, source_dir_backup, rename_timeout):
            print(f"Failed to rename {source_dir} -> {source_dir_backup}")
            return False

        # activate target mode
        print(f"Renaming {target_dir} -> {vanilla_dir}")
        if not rename_with_timeout(target_dir, vanilla_dir, rename_timeout):
            print(f"Failed to rename {target_dir} -> {vanilla_dir}")
            return False

        print(f"Set mode: {dir_mode.name} successfully!")
        return True

    def set_id_location(self, dir_mode):
        "Set id file location"
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

    def get(self, dir_mode):
        "Get directory"
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
        "Get id filename"
        self.game._validate_dir_mode(dir_mode)
        return ID_FILE_NAMES[dir_mode]

    def __get_vanilla(self):
        """Get the vanilla directory path of the game"""
        print("Getting vanilla directory path...")

        # Get the games directory from the steam object of the game
        games_dir = self.game.steam.get_games_dir()
        # Get the title of the game
        title = self.game.get_title()

        # Construct and return the vanilla directory path
        vanilla_dir = os.path.join(games_dir, title)
        print(f"Vanilla directory path is {vanilla_dir}.")
        return vanilla_dir

    def __get_id_path(self, dir_mode):
        "Get id filename path"
        mode_dir = self.get(dir_mode)
        if mode_dir is None:
            print(f"Error: Directory '{mode_dir}' does not exist. Unable to construct ID path.")
        else:
            id_path = os.path.join(mode_dir, self.get_id_filename(dir_mode))

        print("ID Path:", id_path)
        return id_path

    def _set_id_content(self, dir_mode, installation_state):
        "Set id file content"
        self.game._validate_dir_mode(dir_mode)

        # get id path
        id_path = self.__get_id_path(dir_mode)
        if id_path is None:
            return None

        self.__write_id_content(dir_mode, self.get(dir_mode), installation_state)

        print(f"result={id_path}")

    def __write_id_content(self, dir_mode, directory, installation_state=None):
        """Write id file content.

        This method is needed because it us used by set id location & set id content
        'directory' param is needed because the dir_mode wouldn't be able to be retrieved yet
        when setting id location"""
        state_data = {
            "directory_mode": dir_mode.name,
            "installation_state": installation_state.name if installation_state is not None else None,
            "game_directory": directory,
        }

        id_file_name = self.get_id_filename(dir_mode)
        id_file_path = os.path.join(directory, id_file_name)
        with open(id_file_path, "w", encoding="utf-8") as file_handle:
            json.dump(state_data, file_handle, indent=4)  # Write state data as JSON
        print(f"Written ID content to: {id_file_path}")

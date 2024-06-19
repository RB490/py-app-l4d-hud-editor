"""Handles game ID information for different directory modes."""

# pylint: disable=protected-access, broad-exception-raised, broad-exception-caught, logging-fstring-interpolation
import json
import os
import sys
from collections import defaultdict
from enum import Enum
from tkinter import filedialog

from loguru import logger
from shared_utils.functions import is_subdirectory, show_message

from src.game.constants import DirectoryMode, InstallationState, SyncState
from src.game.game import Game


def call_validate_dir_mode_before_method(func):
    """Decorator to call _validate_dir_mode before a method."""

    def wrapper(self, dir_mode, *args, **kwargs):
        # Call the original method and store its result
        result = func(self, dir_mode, *args, **kwargs)
        # Call _validate_dir_mode after the original method
        self.game._validate_dir_mode(dir_mode)
        return result

    return wrapper


class KeyRetrievalError(Exception):
    """Custom exception for key retrieval errors."""

    pass


class GameIDHandler:
    """Handles game ID information for different directory modes."""

    def __init__(self, game_class):
        """Initialize the GameIDHandler with the associated game class."""
        self.game = game_class

        self.id_file_extension = ".l4d_hud_editor"

        self.id_file_names = {
            DirectoryMode.USER: f"user_dir{self.id_file_extension}",
            DirectoryMode.DEVELOPER: f"dev_dir{self.id_file_extension}",
        }

        self.default_data = {
            "installation_state": InstallationState.UNKNOWN.name,
            "sync_state": SyncState.UNKNOWN.name,
            "sync_changes": {},
        }

    def get_file_extension(self):
        return self.id_file_extension

    @call_validate_dir_mode_before_method
    def get_file_name(self, dir_mode):
        return self.id_file_names[dir_mode]

    @call_validate_dir_mode_before_method
    def __get_path(self, dir_mode):
        """Get the path of the ID file for a specific directory mode."""
        mode_dir = self.game.dir.get(dir_mode)
        if not mode_dir:
            logger.warning(f"Could not retrieve ID path for {dir_mode.name}.")
            return None

        id_path = os.path.join(mode_dir, self.get_file_name(dir_mode))
        logger.debug(f"ID Path: {id_path}")
        return id_path

    @call_validate_dir_mode_before_method
    def set_path(self, dir_mode):
        """Manually set the directory for a given directory mode."""

        logger.info(f"Manually setting directory for: {dir_mode.name}")

        try:
            # prompt - manually select location?
            message = (
                f"Could not find {self.game.get_title()} ID file for the {dir_mode.name} installation directory!\n\n"
                "Is it installed and do you want to manually select it?"
            )
            result = show_message(message, "yesno", "Set ID location")
            if not result:
                raise ValueError("User chose not to select a directory")

            # manually select location
            id_dir = filedialog.askdirectory(
                mustexist=True,
                title=f"Select the {dir_mode.name} directory",
                initialdir=self.game.steam.get_games_dir(),
            )

            # verify location - existence
            if not os.path.isdir(id_dir):
                raise ValueError("Invalid directory specified")

            # verify location - is a steam game
            if not is_subdirectory(self.game.steam.get_games_dir(), id_dir):
                raise ValueError("Directory is not inside the steam games folder")

            # verify location - is the correct steam game
            exe_file = os.path.join(id_dir, self.game.get_exe())
            exe_file = os.path.normpath(exe_file)
            if not os.path.isfile(exe_file):
                raise ValueError(f"{exe_file} is not present in the directory")

            # prompt installation state
            if dir_mode == DirectoryMode.DEVELOPER:
                message = f"Is {dir_mode.name} mode fully installed?"
                is_fully_installed = show_message(message, "yesno", "SCRIPT_NAME")
                install_state = InstallationState.INSTALLED if is_fully_installed else InstallationState.UNKNOWN
            else:
                install_state = InstallationState.INSTALLED

            # write ID file
            initial_data = self.default_data.copy()
            initial_data["installation_state"] = install_state.name

            id_path = os.path.join(id_dir, self.get_file_name(dir_mode))
            self._create_file(id_path)
            self.__write_data(id_path, initial_data)
            return True
        except Exception as err_info:
            raise RuntimeError(f"Could not set {dir_mode.name} ID location! \n\n{err_info}") from err_info

    @call_validate_dir_mode_before_method
    def get_installation_state(self, dir_mode):
        state_name = self.__get_key(dir_mode, "installation_state")
        return InstallationState[state_name]

    @call_validate_dir_mode_before_method
    def set_installation_state(self, dir_mode, installation_state):
        if not isinstance(installation_state, InstallationState):
            raise ValueError("installation_state must be an instance of InstallationState enum")

        self.__set_key(dir_mode, "installation_state", installation_state)

    @call_validate_dir_mode_before_method
    def set_sync_state(self, dir_mode, sync_state):
        if not isinstance(sync_state, SyncState):
            raise ValueError("sync_state must be an instance of SyncState enum")

        self.__set_key(dir_mode, "sync_state", sync_state)

    @call_validate_dir_mode_before_method
    def get_sync_state(self, dir_mode):
        state_name = self.__get_key(dir_mode, "sync_state")
        return SyncState[state_name]

    @call_validate_dir_mode_before_method
    def get_sync_changes(self, dir_mode):
        return self.__get_key(dir_mode, "sync_changes")

    @call_validate_dir_mode_before_method
    def set_sync_changes(self, dir_mode, sync_changes):
        self.__set_key(dir_mode, "sync_changes", sync_changes)

    def __get_key(self, dir_mode, key):
        default_value = self.default_data.get(key)
        if default_value is None:
            raise KeyRetrievalError(f"Default value for key '{key}' is not available.")

        data = self.__get_data(dir_mode)
        return data.get(key, default_value)

    def __set_key(self, dir_mode, key, value):
        id_path = self.__get_path(dir_mode)
        if id_path is None:
            return None

        data = self.__get_data(dir_mode)

        # Handle enums
        if isinstance(value, Enum):
            data[key] = value.name if value is not None else None
        # Handle objects
        else:
            data[key] = value

        self.__write_data(id_path, data)
        logger.debug(f"Updated {key} value to: '{value.name if isinstance(value, Enum) else value}'")

    def __get_data(self, dir_mode):
        id_path = self.__get_path(dir_mode)
        if id_path is None:
            return self.default_data.copy()

        data = self.__read_data(id_path)
        return data

    def __read_data(self, id_path):
        try:
            if os.path.isfile(id_path):
                with open(id_path, "r", encoding="utf-8") as file_handle:
                    return json.load(file_handle)
        except Exception as err:
            logger.error(f"Error reading ID content: {err}")
        return self.default_data.copy()  # Fallback to default values

    def __write_data(self, id_path, data):
        try:
            with open(id_path, "w", encoding="utf-8") as file_handle:
                json.dump(data, file_handle, indent=4)
                logger.debug(f"Set ID content in: {id_path}")
                return True
        except Exception as err_info:
            raise Exception(f"Couldn't write id content! Info: {err_info}") from err_info

    def _create_file(self, id_path):
        try:
            with open(id_path, "w", encoding="utf-8") as file_handle:
                json.dump({}, file_handle, indent=4)
        except Exception as err_info:
            raise Exception(f"Unable to create ID file: {err_info}") from err_info

    def quit_if_invalid_id_file_structure(self):
        """
        Check for invalid ID file structures in the Steam game directory. And quit when invalid

        This method searches for ID files within subdirectories of
        the Steam game directory (one level deep) and performs checks for invalid file structures.

        Raises:
            Exception: If two ID files are found in the same folder.
            Exception: If one kind of ID file (identified by full name & extension) is found in more than one folder.
        """
        steam_game_dir = self.game.steam.get_games_dir()

        # Dictionary to track ID files in each folder
        id_files_in_folders = defaultdict(list)
        # Dictionary to track folders for each kind of ID file
        id_files_in_directories = defaultdict(list)

        try:
            # Iterate over subdirectories in the Steam game directory
            for subdir in os.listdir(steam_game_dir):
                subdir_path = os.path.join(steam_game_dir, subdir)

                if os.path.isdir(subdir_path):
                    # List all files in the subdirectory
                    files = os.listdir(subdir_path)

                    # Find ID files in the current subdirectory
                    id_files = [f for f in files if f.endswith(self.id_file_extension)]

                    # Check if there are multiple ID files in the same folder
                    if len(id_files) > 1:
                        raise Exception(f"Multiple ID files found in directory: {subdir_path}")

                    # Track ID files and their corresponding directories
                    for id_file in id_files:
                        id_files_in_folders[subdir_path].append(id_file)
                        id_files_in_directories[id_file].append(subdir_path)

            # Check if the same kind of ID file is found in more than one folder
            for id_file, directories in id_files_in_directories.items():
                if len(directories) > 1:
                    raise Exception(f"ID file '{id_file}' found in multiple directories: {directories}")

        except Exception as e:
            show_message(
                f"Invalid ID file structure: {e}. \n\nThis is currently unhandled and needs to be fixed.  \n\nClosing..."
            )
            sys.exit(1)
        logger.debug("Verified ID file structure!")


def main():
    "Debug"
    game = Game()

    sync_state = game.dir.id.set_sync_state(DirectoryMode.DEVELOPER, SyncState.SYNCED)

    # my_obj = {"mykey1": "value1", "mykey2": "value2", "mykey3": "value3"}
    my_obj = {}
    game.dir.id.set_path(DirectoryMode.DEVELOPER)
    game.dir.id.set_sync_changes(DirectoryMode.DEVELOPER, my_obj)
    sync_changes = game.dir.id.get_sync_changes(DirectoryMode.DEVELOPER)
    sync_state = game.dir.id.get_sync_state(DirectoryMode.DEVELOPER)
    installation_state = game.dir.id.get_installation_state(DirectoryMode.DEVELOPER)

    logger.debug("finished debug_id_handler")


def test():
    "Test ID handler"
    from shared_utils.functions import loguru_setup_logging_filter

    loguru_setup_logging_filter("DEBUG", "exclude", ["shared_managers.hwnd_manager"])
    game_class = Game()

    game_id_handler = game_class.dir.id
    # game_class.dir.id.set_path(DirectoryMode.DEVELOPER)

    # Set the ID location for developer directory
    dir_mode = DirectoryMode.DEVELOPER
    game_id_handler.set_path(dir_mode)

    # Validate the ID file structure
    game_id_handler.quit_if_invalid_id_file_structure()

    # Set installation state for developer directory
    installation_state = InstallationState.INSTALLED
    game_id_handler.set_installation_state(dir_mode, installation_state)

    # Set sync state for developer directory
    sync_state = SyncState.SYNCED
    game_id_handler.set_sync_state(dir_mode, sync_state)

    # Get installation state for developer directory
    retrieved_installation_state = game_id_handler.get_installation_state(dir_mode)
    if retrieved_installation_state:
        logger.debug(f"Retrieved Installation State: retrieved_installation_state.name")
    else:
        logger.debug("Installation State not found.")

    # Get sync state for developer directory
    retrieved_sync_state = game_id_handler.get_sync_state(dir_mode)
    if retrieved_sync_state:
        logger.debug(f"Retrieved Sync State: {retrieved_sync_state.name}")
    else:
        logger.debug("Sync State not found.")


if __name__ == "__main__":
    test()

"""Handles game ID information for different directory modes."""
# pylint: disable=protected-access, broad-exception-raised, broad-exception-caught, logging-fstring-interpolation
import json
import os
from enum import Enum
from tkinter import filedialog

from loguru import logger

from game.constants import DirectoryMode, InstallationState, SyncState
from shared_utils.shared_utils import is_subdirectory, show_message


def call_validate_dir_mode_before_method(func):
    """Decorator to call _validate_dir_mode before a method."""

    def wrapper(self, dir_mode, *args, **kwargs):
        # Call the original method and store its result
        result = func(self, dir_mode, *args, **kwargs)
        # Call _validate_dir_mode after the original method
        self.game._validate_dir_mode(dir_mode)
        return result

    return wrapper


class GameIDHandler:
    """Handles game ID information for different directory modes."""

    def __init__(self, game_class):
        """Initialize the GameIDHandler with the associated game class."""
        self.game = game_class

        self.id_file_names = {
            DirectoryMode.USER: "_hud_editor_id_file__user_directory.DoNotDelete",
            DirectoryMode.DEVELOPER: "_hud_editor_id_file__dev_directory.DoNotDelete",
        }

    @call_validate_dir_mode_before_method
    def get_filename(self, dir_mode):
        self.game._validate_dir_mode(dir_mode)
        return self.id_file_names[dir_mode]

    def __get_path(self, dir_mode):
        """Get the path of the ID file for a specific directory mode."""
        mode_dir = self.game.dir.get(dir_mode)
        if not mode_dir:
            logger.warning(f"Could not retrieve ID path for {dir_mode.name}.")
            return None

        id_path = os.path.join(mode_dir, self.get_filename(dir_mode))
        logger.debug(f"ID Path: {id_path}")
        return id_path

    @call_validate_dir_mode_before_method
    def set_path(self, dir_mode):
        """Manually set the directory for a given directory mode."""

        logger.info(f"Manually setting directory for: {dir_mode.name}")

        try:
            self.game._validate_dir_mode(dir_mode)

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
                install_state = InstallationState.COMPLETED if is_fully_installed else InstallationState.NOT_INSTALLED
            else:
                install_state = InstallationState.COMPLETED

            # write ID file
            initial_data = {
                "directory_mode": dir_mode.name,
                "installation_state": install_state.name,
                "sync_state": SyncState.UNKNOWN.name,
            }

            id_path = os.path.join(id_dir, self.get_filename(dir_mode))
            self.__create_file(id_path)
            self.__write_data(id_path, initial_data)
            return True
        except Exception as err_info:
            raise RuntimeError(f"Could not set {dir_mode.name} ID location! \n\n{err_info}") from err_info

    @call_validate_dir_mode_before_method
    def get_installation_state(self, dir_mode):
        return self.__get_key(dir_mode, "installation_state", InstallationState.NOT_INSTALLED.name)

    @call_validate_dir_mode_before_method
    def set_installation_state(self, dir_mode, installation_state):
        self.__set_key(dir_mode, "installation_state", installation_state)
        return installation_state

    @call_validate_dir_mode_before_method
    def get_sync_state(self, dir_mode):
        return self.__get_key(dir_mode, "sync_state", SyncState.UNKNOWN.name)

    @call_validate_dir_mode_before_method
    def set_sync_state(self, dir_mode, sync_state):
        self.__set_key(dir_mode, "sync_state", sync_state)
        return sync_state

    @call_validate_dir_mode_before_method
    def set_sync_changes(self, dir_mode, sync_changes):
        self.__set_key(dir_mode, "sync_changes", sync_changes)
        return sync_changes

    @call_validate_dir_mode_before_method
    def get_sync_changes(self, dir_mode):
        return self.__get_key(dir_mode, "sync_changes", {})

    def __get_key(self, dir_mode, key, default_value):
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
            return {}

        data = self.__read_data(id_path)
        return data

    def __read_data(self, id_path):
        try:
            if os.path.isfile(id_path):
                with open(id_path, "r", encoding="utf-8") as file_handle:
                    return json.load(file_handle)
        except Exception as err:
            logger.error(f"Error reading ID content: {err}")
        return {}  # Fallback to empty json

    def __write_data(self, id_path, data):
        try:
            with open(id_path, "w", encoding="utf-8") as file_handle:
                json.dump(data, file_handle, indent=4)
                logger.debug(f"Set ID content in: {id_path}")
                return True
        except Exception as err_info:
            raise Exception(f"Couldn't write id content! Info: {err_info}") from err_info

    def __create_file(self, id_path):
        try:
            with open(id_path, "w", encoding="utf-8") as file_handle:
                json.dump({}, file_handle, indent=4)
        except Exception as err_info:
            raise Exception(f"Unable to create ID file: {err_info}") from err_info

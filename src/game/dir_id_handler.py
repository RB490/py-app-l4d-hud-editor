"""Handles game ID and state information for different directory modes."""
# pylint: disable=protected-access, broad-exception-raised, broad-exception-caught, logging-fstring-interpolation
import json
import os
from tkinter import filedialog

from loguru import logger

from game.constants import DirectoryMode, InstallationState, SyncState
from shared_utils.shared_utils import is_subdirectory, show_message


class GameIDHandler:
    """Handles game ID and state information for different directory modes."""

    def __init__(self, game_class):
        """Initialize the GameIDHandler with the associated game class."""
        self.game = game_class

        self.id_file_names = {
            DirectoryMode.USER: "_hud_editor_id_file__user_directory.DoNotDelete",
            DirectoryMode.DEVELOPER: "_hud_editor_id_file__dev_directory.DoNotDelete",
        }

    def _get_filename(self, dir_mode):
        self.game._validate_dir_mode(dir_mode)
        return self.id_file_names[dir_mode]

    def __get_path(self, dir_mode):
        """Get the path of the ID file for a specific directory mode."""
        mode_dir = self.game.dir.get(dir_mode)
        if not mode_dir:
            logger.debug(f"Could not retrieve ID path for {dir_mode.name}.")
            return None

        id_path = os.path.join(mode_dir, self._get_filename(dir_mode))
        logger.debug(f"ID Path: {id_path}")
        return id_path

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
                mustexist=True, title=f"Select the {dir_mode.name} directory", initialdir=self.game.steam.get_games_dir
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
            initial_state_data = {
                "directory_mode": dir_mode.name,
                "game_directory": id_dir,
                "installation_state": install_state.name,
                "sync_state": SyncState.UNKNOWN.name,
            }

            self.__create_file(dir_mode, id_dir)
            self.__write_content(dir_mode, initial_state_data)
            return True
        except Exception as err_info:
            raise RuntimeError(f"Could not set {dir_mode.name} ID location! \n\n{err_info}") from err_info

    def get_installation_state(self, dir_mode):
        """Get the installation state for a specific directory mode."""
        self.game._validate_dir_mode(dir_mode)
        return InstallationState[
            self.__get_state_value(dir_mode, "installation_state", InstallationState.NOT_INSTALLED.name)
        ]

    def set_installation_state(self, dir_mode, installation_state):
        """Set the installation state for a specific directory mode."""
        self.game._validate_dir_mode(dir_mode)
        self.__set_state(dir_mode, "installation_state", installation_state)
        return installation_state

    def get_sync_state(self, dir_mode):
        """Get the synchronization state for a specific directory mode."""
        self.game._validate_dir_mode(dir_mode)
        return SyncState[self.__get_state_value(dir_mode, "sync_state", SyncState.UNKNOWN.name)]

    def set_sync_state(self, dir_mode, sync_state):
        """Set the synchronization state for a specific directory mode."""
        self.game._validate_dir_mode(dir_mode)
        self.__set_state(dir_mode, "sync_state", sync_state)
        return sync_state

    def __get_state_value(self, dir_mode, state_key, default_value):
        """Get a specific state value from the ID file with a default value if not present."""
        id_path = self.__get_path(dir_mode)

        if id_path is None:
            logger.debug(f"No ID path for {dir_mode.name}. Defaulting '{state_key}' to '{default_value}'")
            return default_value

        state_data = self.__read_content(id_path)
        state_value = state_data.get(state_key)

        if state_value is None:
            logger.debug(f"No '{state_key}' value for {dir_mode.name}. Defaulting to '{default_value}'")
            return default_value

        logger.debug(f"Retrieved {dir_mode.name} '{state_key}' value '{state_value}'")
        return state_value

    def __set_state(self, dir_mode, state_key, state_value):
        """Set a specific state value in the ID file."""
        id_path = self.__get_path(dir_mode)
        if id_path is None:
            return None

        state_data = self.__read_content(id_path)
        state_data[state_key] = state_value.name if state_value is not None else None
        self.__write_content(dir_mode, state_data)
        logger.debug(f"Updated {state_key} state to: '{state_value.name}'")

    def __read_content(self, id_path):
        """Read and return the content of the ID file."""
        try:
            if os.path.isfile(id_path):
                with open(id_path, "r", encoding="utf-8") as file_handle:
                    return json.load(file_handle)
        except Exception as err:
            logger.error(f"Error reading ID content: {err}")
        return {}  # Fallback to empty json

    def __write_content(self, dir_mode, state_data):
        """Write the state data to the ID file."""
        id_path = self.__get_path(dir_mode)

        state_data["directory_mode"] = dir_mode.name
        state_data["game_directory"] = self.game.dir.get(dir_mode)

        try:
            with open(id_path, "w", encoding="utf-8") as file_handle:
                json.dump(state_data, file_handle, indent=4)
                logger.debug(f"Set ID content in: {id_path}")
                return True
        except Exception as err_info:
            raise Exception(f"Couldn't write id content! Info: {err_info}") from err_info

    def __create_file(self, dir_mode, directory):
        """Create an ID file in the specified directory."""

        try:
            id_path = os.path.join(directory, self._get_filename(dir_mode))

            with open(id_path, "w", encoding="utf-8") as file_handle:
                json.dump({}, file_handle, indent=4)
        except Exception as err_info:
            raise Exception(f"Unable to create ID file: {err_info}") from err_info

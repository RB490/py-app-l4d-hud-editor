"Steam info retriever"
import os
import winreg
from tkinter import filedialog

from loguru import logger
from shared_utils.functions import Singleton, loguru_setup_logging_filter

from src.utils.constants import DATA_MANAGER


class SteamPathHandler(metaclass=Singleton):
    """
    A utility class to retrieve Steam directory information.
    """

    DEFAULT_STEAM_DIRECTORIES = [
        "E:\\Games\\Steam",
        "C:\\Program Files (x86)\\Steam",
    ]
    STEAM_EXECUTABLE = "steam.exe"

    def __init__(self):
        """
        Initialize the class.
        """
        self.data_manager = DATA_MANAGER

    def _get_steam_directory_from_registry(self):
        """
        Retrieve the Steam directory path from the Windows Registry.

        Returns:
            str: Path to the Steam directory, or None if not found in the Registry.
        """
        logger.debug("Looking for Steam directory in Windows Registry...")
        try:
            key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, "Software\\Valve\\Steam")
            steam_path = winreg.QueryValueEx(key, "SteamPath")[0]
            if self._verify_directory(steam_path):
                logger.debug(f"Steam directory found in Registry: {steam_path}")
                return steam_path
        except:
            pass
        logger.debug("Steam directory not found in Windows Registry.")
        return None

    def _get_steam_directory_from_default_locations(self):
        """
        Search for a directory containing a specific file in a list of paths.
        """
        paths = self.DEFAULT_STEAM_DIRECTORIES
        logger.debug(f"Looking for directory containing '{self.STEAM_EXECUTABLE}' in default directories...")
        for path in paths:
            if self._verify_directory(path):
                logger.debug(f"Directory found at: {path}")
                return path
        logger.debug(f"'{self.STEAM_EXECUTABLE}' not found in default directories paths.")
        return None

    def _get_steam_directory_from_saved_data(self):
        """
        Get steam directory from saved data
        """
        steam_dir = self.data_manager.get("steam_root_dir")
        logger.debug(f"Saved data Steam root directory: {steam_dir}")
        if self._verify_directory(steam_dir):
            return steam_dir
        else:
            return None

    def _get_steam_directory_from_user(self):
        """
        Ask the user to select the Steam directory.

        Returns:
            str: Path to the selected Steam directory, or raises NotADirectoryError if not valid.
        """
        logger.debug("Asking user for Steam directory...")
        steam_path = filedialog.askdirectory(title="Select Steam directory")
        if self._verify_directory(steam_path):
            logger.debug("User-selected directory contains Steam executable.")
            return steam_path
        else:
            logger.debug("User-selected directory does not contain Steam executable.")
            return None

    def _get_root_dir(self):
        """
        Get the Steam root directory from registry, default paths or persistent data.
        """
        logger.debug("Getting Steam root directory...")

        # get root dir through various methods
        root_dir = (
            self._get_steam_directory_from_saved_data()
            or self._get_steam_directory_from_registry()
            or self._get_steam_directory_from_default_locations()
            or self._get_steam_directory_from_user()
        )

        # verify directory
        if not self._verify_directory(root_dir):
            logger.error("Failed to retrieve and verify the Steam root directory.")
            raise Exception("Could not retrieve steam root directory!")

        # save directory
        self.data_manager.set("steam_root_dir", root_dir)

        logger.debug(f"Steam root directory successfully retrieved and verified: {root_dir}")
        return root_dir

    def _verify_directory(self, steam_directory):
        """
        Verify steam directory by checking if steam.exe is present
        """
        is_valid_dir = os.path.isfile(os.path.join(steam_directory, self.STEAM_EXECUTABLE))

        logger.debug(f"Verify Steam directory '{steam_directory}' result: {is_valid_dir}")
        return is_valid_dir

    def get_executable_path(self):
        """
        Get the Steam executable path.
        """
        logger.debug("Getting Steam executable path...")
        root_dir = self._get_root_dir()
        executable_path = os.path.join(root_dir, "steam.exe")
        logger.debug(f"Retrieved Steam executable path: {executable_path}")
        return executable_path

    def get_games_dir(self):
        """
        Get the Steam games directory.

        Returns:
            str: Path to the Steam games directory.
        """
        logger.debug("Getting Steam games directory...")
        games_dir = os.path.join(self._get_root_dir(), "steamapps", "common")
        games_dir = os.path.normpath(games_dir)  # Normalize the games_dir path
        logger.debug(f"Steam games directory: {games_dir}")
        return games_dir


if __name__ == "__main__":
    # clear console & focus class messages
    os.system("cls")
    loguru_setup_logging_filter("DEBUG", "include", ["__main__"])

    # debugging the class
    steam_path_handler = SteamPathHandler()
    # result = steam_path_handler._get_steam_directory_from_registry()
    # result = steam_path_handler._get_steam_directory_from_default_locations()
    # result = steam_path_handler._get_steam_directory_from_saved_data()
    # result = steam_path_handler._get_steam_directory_from_user()
    # result = steam_path_handler._get_root_dir()
    result = steam_path_handler.get_executable_path()
    logger.debug(f"result = {result}")

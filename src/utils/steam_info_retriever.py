import os
import tkinter as tk
import winreg
from tkinter import filedialog

from utils.shared_utils import Singleton


class SteamInfoRetriever(metaclass=Singleton):
    """
    A utility class to retrieve Steam directory information.
    """

    DEFAULT_STEAM_PATHS = [
        "E:\\Games\\Steam",
        "C:\\Program Files (x86)\\Steam",
    ]
    STEAM_EXECUTABLE = "steam.exe"

    def __init__(self, persistent_data):
        """
        Initialize the SteamInfoRetriever.

        Args:
            persistent_data (dict): A dictionary to store persistent data.
        """
        self.steam_info = {}
        self.persistent_data = persistent_data
        self.print_debug_messages = False

    def __print_if_debug(self, message):
        if self.print_debug_messages:
            print(message)

    def _check_path(self, path, filename):
        """
        Check if a file exists in the given path.

        Args:
            path (str): The directory path.
            filename (str): The name of the file to check.

        Returns:
            bool: True if the file exists, False otherwise.
        """
        self.__print_if_debug(f"Checking path: {path}")
        return os.path.isfile(os.path.join(path, filename))

    def _find_directory_in_paths(self, paths, target_filename):
        """
        Search for a directory containing a specific file in a list of paths.

        Args:
            paths (list): List of directory paths to search in.
            target_filename (str): The name of the file to find.

        Returns:
            str: Path to the directory containing the target file, or None if not found.
        """
        self.__print_if_debug(f"Looking for directory containing '{target_filename}' in specified paths...")
        for path in paths:
            if self._check_path(path, target_filename):
                self.__print_if_debug(f"Directory found at: {path}")
                return path
        self.__print_if_debug(f"Directory containing '{target_filename}' not found in specified paths.")
        return None

    def _find_steam_directory_in_paths(self):
        """
        Find the Steam directory in the specified paths.

        Returns:
            str: Path to the Steam directory, or None if not found.
        """
        return self._find_directory_in_paths(self.DEFAULT_STEAM_PATHS, self.STEAM_EXECUTABLE)

    def _get_steam_directory_from_registry(self):
        """
        Retrieve the Steam directory path from the Windows Registry.

        Returns:
            str: Path to the Steam directory, or None if not found in the Registry.
        """
        self.__print_if_debug("Looking for Steam directory in Windows Registry...")
        try:
            key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, "Software\\Valve\\Steam")
            steam_path = winreg.QueryValueEx(key, "SteamPath")[0]
            if self._check_path(steam_path, self.STEAM_EXECUTABLE):
                self.__print_if_debug(f"Steam directory found in Registry: {steam_path}")
                return steam_path
        except (WindowsError, FileNotFoundError):
            pass
        self.__print_if_debug("Steam directory not found in Windows Registry.")
        return None

    def find_steam_directory(self):
        """
        Find the Steam directory either in specified paths or in the Windows Registry.

        Returns:
            str: Path to the Steam directory, or raises NotADirectoryError if not found.
        """
        self.__print_if_debug("Trying to find Steam directory...")
        steam_path = self._find_steam_directory_in_paths() or self._get_steam_directory_from_registry()

        if steam_path:
            return steam_path

        self.__print_if_debug("Steam directory not found.")
        raise NotADirectoryError("Steam directory not found")

    def ask_for_directory(self):
        """
        Ask the user to select the Steam directory.

        Returns:
            str: Path to the selected Steam directory, or raises NotADirectoryError if not valid.
        """
        self.__print_if_debug("Asking user for Steam directory...")
        root = tk.Tk()
        root.withdraw()
        steam_path = filedialog.askdirectory(title="Select Steam directory")
        if self._check_path(steam_path, self.STEAM_EXECUTABLE):
            self.__print_if_debug("User-selected directory contains Steam executable.")
            return steam_path
        else:
            self.__print_if_debug("User-selected directory does not contain Steam executable.")
            raise NotADirectoryError("Selected directory does not contain Steam executable")

    def _get_or_set_info(self, key, default_value_func):
        """
        Get or set information in the steam_info dictionary.

        Args:
            key (str): Key for the information in the dictionary.
            default_value_func (callable): Function to retrieve the default value if not present.

        Returns:
            The value associated with the key.
        """
        self.__print_if_debug(f"Getting or setting info for key: {key}")
        if key not in self.steam_info:
            self.steam_info[key] = default_value_func()
        return self.steam_info[key]

    def get_info(self, key, default_value_func):
        """
        Get Steam-related information.

        Args:
            key (str): Key for the information in the dictionary.
            default_value_func (callable): Function to retrieve the default value if not present.

        Returns:
            The value associated with the key.
        """
        self.__print_if_debug(f"Getting Steam-related information for key: {key}")
        return self._get_or_set_info(key, default_value_func)

    def get_root_dir(self):
        """
        Get the Steam root directory and save it to persistent_data.

        Returns:
            str: Path to the Steam root directory.
        """
        self.__print_if_debug("Getting Steam root directory...")

        # Check if the root directory is already saved in persistent_data
        if "steam_root_dir" in self.persistent_data:
            saved_root_dir = self.persistent_data["steam_root_dir"]
            saved_root_dir = os.path.normpath(saved_root_dir)
            if self._check_path(saved_root_dir, self.STEAM_EXECUTABLE):
                self.__print_if_debug(f"Using saved Steam root directory: {saved_root_dir}")
                return saved_root_dir
            else:
                self.__print_if_debug("Saved Steam root directory is not valid.")

        # If not saved or saved directory is invalid, proceed to find it
        root_dir = self.get_info("root_dir", self.find_steam_directory)
        root_dir = os.path.normpath(root_dir)  # Normalize the root_dir path
        self.__print_if_debug(f"Steam root directory: {root_dir}")

        # Save the root directory if found
        if root_dir:
            self.__save_root_directory(root_dir)

        return root_dir

    def get_games_dir(self):
        """
        Get the Steam games directory.

        Returns:
            str: Path to the Steam games directory.
        """
        self.__print_if_debug("Getting Steam games directory...")
        games_dir = os.path.join(self.get_root_dir(), "steamapps", "common")
        games_dir = os.path.normpath(games_dir)  # Normalize the games_dir path
        self.__print_if_debug(f"Steam games directory: {games_dir}")
        return games_dir

    def get_exe_path(self):
        """
        Get the Steam executable path.

        Returns:
            str: Path to the Steam executable.
        """
        self.__print_if_debug("Getting Steam executable path...")
        exe_path = os.path.join(self.get_root_dir(), self.STEAM_EXECUTABLE)
        exe_path = os.path.normpath(exe_path)  # Normalize the exe_path path
        self.__print_if_debug(f"Steam executable path: {exe_path}")
        return exe_path

    def __save_root_directory(self, root_dir):
        """
        Save the Steam root directory to persistent_data.

        Args:
            root_dir (str): Path to the Steam root directory.

        Prints:
            The saved Steam root directory.
        """
        self.__print_if_debug("Saving Steam root directory to persistent_data...")
        self.persistent_data["steam_root_dir"] = root_dir
        self.__print_if_debug("Steam root directory saved:", root_dir)
import os
import tkinter as tk
import winreg
from tkinter import filedialog

class SteamInfoRetriever:
    """
    A utility class to retrieve Steam directory information.
    """

    def __init__(self, persistent_data):
        """
        Initialize the SteamInfoRetriever.

        Args:
            persistent_data (dict): A dictionary to store persistent data.
        """
        self.steam_info = {}
        self.persistent_data = persistent_data
        self.default_steam_paths = [
            "C:\\Program Files (x86)\\Steam",
            "E:\\Games\\Steam"
        ]

    def find_steam_directory(self):
        """
        Find the Steam directory by checking default paths and Windows Registry.

        Returns:
            str: Path to the Steam directory.
        
        Raises:
            NotADirectoryError: If the Steam directory is not found.
        """
        # Check default paths
        for path in self.default_steam_paths:
            if os.path.isfile(os.path.join(path, "steam.exe")):
                return path
        
        try:
            # Try to retrieve Steam directory from Windows Registry
            key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, "Software\\Valve\\Steam")
            steam_path = winreg.QueryValueEx(key, "SteamPath")[0]
            if os.path.isfile(os.path.join(steam_path, "steam.exe")):
                return steam_path
        except (WindowsError, FileNotFoundError):
            # If Registry access fails, prompt the user to select the Steam directory
            root = tk.Tk()
            root.withdraw()
            steam_path = filedialog.askdirectory(title="Select Steam directory")
            if os.path.isfile(os.path.join(steam_path, "steam.exe")):
                return steam_path
        
        raise NotADirectoryError("Steam directory not found")

    def get_root_dir(self):
        if "root_dir" not in self.steam_info:
            self.steam_info["root_dir"] = self.find_steam_directory()
        return self.steam_info["root_dir"]

    def get_games_dir(self):
        if "games_dir" not in self.steam_info:
            self.steam_info["games_dir"] = os.path.join(self.get_root_dir(), "steamapps", "common")
        return self.steam_info["games_dir"]

    def get_exe_path(self):
        if "steam_exe" not in self.steam_info:
            self.steam_info["steam_exe"] = os.path.join(self.get_root_dir(), "steam.exe")
        return self.steam_info["steam_exe"]

    def save_root_directory(self):
        self.persistent_data["steam_root_dir"] = self.get_root_dir()

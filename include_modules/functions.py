"""Functions used throughout the program"""
import shutil
import json
import os
import winreg
import tkinter as tk
from tkinter import filedialog
from include_modules.constants import PERSISTENT_DATA_PATH


def start_hud_editing():
    """Perform all the actions needed to start hud editing"""
    print("todo")


def copy_directory_contents(src_dir, dest_dir, ignore_file=None):
    """Copy the contents of src_dir into dest_dir overwriting if needed"""
    # Create the destination directory if it doesn't already exist
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    # Traverse the source directory using os.walk and create a list of all files to be copied
    src_files = []
    for root, _, files in os.walk(src_dir):
        for filename in files:
            if filename != ignore_file:
                src_files.append(os.path.join(root, filename))

    # Iterate over the list of source files and copy each file to the destination directory
    for src_path in src_files:
        relative_path = os.path.relpath(src_path, src_dir)  # Calculate the relative path of the source file
        dest_path = os.path.join(dest_dir, relative_path)

        # Create the destination directory if it doesn't already exist
        relative_dir = os.path.dirname(dest_path)
        if not os.path.exists(relative_dir):
            os.makedirs(relative_dir)

        # Overwrites file in destination
        shutil.copy2(src_path, dest_path)


def get_dir_size(path):
    """Retrieve directory size in bytes"""
    total = 0
    with os.scandir(path) as scandir_result:
        for entry in scandir_result:
            if entry.is_file():
                total += entry.stat().st_size
            elif entry.is_dir():
                total += get_dir_size(entry.path)
    return total


def get_dir_size_in_gb(path):
    """Retrieve directory size in gigaytes"""
    size_in_bytes = get_dir_size(path)
    size_in_gb = round(size_in_bytes / (1024**3), 2)
    output = f"{size_in_gb} GB"
    return output


def get_steam_info(persistent_data=None):
    """Retrieve steam information object"""
    steam_info = {}
    default_steam_path_1 = "C:\\Program Files (x86)\\Steam"
    default_steam_path_2 = "E:\\Games\\Steam"

    # Check if Steam directory exists at default location
    if persistent_data.get("steam_root_dir") and os.path.isfile(
        os.path.join(persistent_data["steam_root_dir"], "steam.exe")
    ):
        steam_info["root_dir"] = persistent_data["steam_root_dir"]
    if os.path.isfile(os.path.join(default_steam_path_1, "steam.exe")):
        steam_info["root_dir"] = default_steam_path_1
    elif os.path.isfile(os.path.join(default_steam_path_2, "steam.exe")):
        steam_info["root_dir"] = default_steam_path_2
    else:
        # Search the registry for Steam installation path
        try:
            key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, "Software\\Valve\\Steam")
            steam_path = winreg.QueryValueEx(key, "SteamPath")[0]
            if os.path.isfile(os.path.join(steam_path, "steam.exe")):
                steam_info["root_dir"] = steam_path
            else:
                raise NotADirectoryError("Steam directory not found")
        except WindowsError as exc:
            # Ask user to specify Steam directory location with file dialog
            root = tk.Tk()
            root.withdraw()
            steam_path = filedialog.askdirectory(title="Select Steam directory")
            if os.path.isfile(os.path.join(steam_path, "steam.exe")):
                steam_info["root_dir"] = steam_path
            else:
                raise NotADirectoryError("Steam directory not found") from exc

    steam_info["game_dir"] = os.path.join(steam_info["root_dir"], "steamapps", "common")
    steam_info["steam_exe"] = os.path.join(steam_info["root_dir"], "steam.exe")

    # save root directory
    persistent_data["steam_root_dir"] = steam_info["root_dir"]
    return steam_info


def load_data():
    """Read persistent data from disk"""
    file_path = PERSISTENT_DATA_PATH
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        # print(f"Error loading data from {file_path}")
        data = {}

    # if needed set default lists so they can be added to
    if "stored_huds" not in data:
        data["stored_huds"] = []

    # print("load_data: {}".format(data))
    return data


def save_data_on_exit(data):
    """Save persistent data to disk on exit"""
    # Save data to a file, database, or other persistent storage
    print("save_data_on_exit")
    save_data(data)


def save_data(data):
    """Save persistent data to disk"""
    print(f"save_data: {data}")
    try:
        with open(PERSISTENT_DATA_PATH, "w", encoding="utf-8") as file:
            json.dump(data, file)
    except (FileNotFoundError, TypeError):
        print(f"Error saving data to {PERSISTENT_DATA_PATH}")

if __name__ == '__main__':
    from .Constants import *
else:
    from Constants import *
import shutil
import json
import os
import winreg
import tkinter as tk
from tkinter import filedialog

def copy_directory_contents(src_dir, dest_dir, ignore_file=None):
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)
    for item in os.listdir(src_dir):
        src_path = os.path.join(src_dir, item)
        dest_path = os.path.join(dest_dir, item)
        if os.path.isdir(src_path):
            copy_directory_contents(src_path, dest_path, ignore_file)
        elif item != ignore_file:
            shutil.copy2(src_path, dest_path)

def get_dir_size(path):
    total = 0
    with os.scandir(path) as it:
        for entry in it:
            if entry.is_file():
                total += entry.stat().st_size
            elif entry.is_dir():
                total += get_dir_size(entry.path)
    return total

def get_dir_size_in_gb(path):
    size_in_bytes = get_dir_size(path)
    size_in_gb = round(size_in_bytes / (1024**3), 2)
    output = f"{size_in_gb} GB"
    return output

def get_steam_info(persistent_data=None):
    steam_info = {}
    default_steam_path_1 = "C:\\Program Files (x86)\\Steam"
    default_steam_path_2 = "E:\Games\Steam"

    # Check if Steam directory exists at default location
    if persistent_data.get("steam_root_dir") and os.path.isfile(os.path.join(persistent_data["steam_root_dir"], "steam.exe")):
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
                raise Exception("Steam directory not found")
        except:
            # Ask user to specify Steam directory location with file dialog
            root = tk.Tk()
            root.withdraw()
            steam_path = filedialog.askdirectory(title="Select Steam directory")
            if os.path.isfile(os.path.join(steam_path, "steam.exe")):
                steam_info["root_dir"] = steam_path
            else:
                raise Exception("Steam directory not found")

    steam_info["game_dir"] = os.path.join(steam_info["root_dir"], "steamapps", "common")
    steam_info["steam_exe"] = os.path.join(steam_info["root_dir"], "steam.exe")

    # save root directory
    persistent_data["steam_root_dir"] = steam_info["root_dir"]
    return steam_info

def load_data():
    file_path = PERSISTENT_DATA_PATH
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        # print(f"Error loading data from {file_path}")
        data = {}
    # print("load_data: {}".format(data))
    return data

def save_data_on_exit(data):
    # Save data to a file, database, or other persistent storage
    print("save_data_on_exit")
    save_data(data)

def save_data(data):
    print("save_data: {}".format(data))
    try:
        with open(PERSISTENT_DATA_PATH, 'w') as file:
            json.dump(data, file)
    except (FileNotFoundError, TypeError):
        print(f"Error saving data to {PERSISTENT_DATA_PATH}")
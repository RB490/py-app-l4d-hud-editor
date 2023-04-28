"""Functions used throughout the program"""
import shutil
import json
import os
import winreg
import time
import tkinter as tk
from tkinter import filedialog
from typing import Dict, List
import win32gui
import win32process
import psutil
from .constants import PERSISTENT_DATA_PATH


def wait_for_process(exe, timeout=None):
    """
    Wait until a process is running based on its executable name.

    :param exe: The executable name of the process.
    :type exe: str
    :param timeout: The maximum time to wait in seconds (optional).
    :type timeout: float or None
    :return: True if the process is found, False if the timeout is reached.
    :rtype: bool
    """
    start_time = time.time()
    while True:
        for process_name in psutil.process_iter():
            if process_name.name() == exe:
                return True
        if timeout is not None and time.time() - start_time > timeout:
            return False
        time.sleep(0.1)


def get_hwnd_for_exe(exe: str) -> int:
    # pylint: disable=c-extension-no-member
    """
    Get the window handle for a process based on its executable name.

    :param exe: The executable name of the process.
    :type exe: str
    :return: The window handle associated with the executable.
    :rtype: int
    :raises Exception: If multiple window handles are found for the given executable.
    """

    def enum_windows_callback(hwnd: int, hwnds: List[int]) -> bool:
        if win32gui.IsWindowVisible(hwnd) and win32gui.IsWindowEnabled(hwnd):
            _, found_pid = win32process.GetWindowThreadProcessId(hwnd)
            if pid_to_name.get(found_pid) == exe:
                hwnds.append(hwnd)
        return True

    pid_to_name: Dict[int, str] = {proc.pid: proc.name() for proc in psutil.process_iter()}
    hwnds: List[int] = []
    win32gui.EnumWindows(enum_windows_callback, hwnds)
    if len(hwnds) > 1:
        raise AssertionError(f"Multiple window handles found for {exe}")
    return hwnds[0] if hwnds else None


def is_process_running(process_name: str) -> bool:
    """
    Check if a process with the specified name is currently running on the system.

    Parameters:
    process_name (str): The name of the process to check for. EG: notepad.exe

    Returns:
    bool: True if the process is running, False otherwise.
    """

    # Get a list of all running processes
    processes = psutil.process_iter()

    # Check if the process is in the list of running processes
    process_running = False
    for process in processes:
        if process.name() == process_name:
            process_running = True
            break

    if process_running:
        print(f"{process_name} is running")
    else:
        print(f"{process_name} is not running")

    return process_running


def is_process_running_from_hwnd(hwnd: int) -> bool:
    # pylint: disable=unpacking-non-sequence
    # pylint: disable=c-extension-no-member
    """
    Check if a process is running based on its window handle.

    :param hwnd: The window handle.
    :type hwnd: int
    :return: True if the process is running, False otherwise.
    :rtype: bool
    """
    try:
        if not win32gui.IsWindow(hwnd):
            print("Invalid window handle")
            return False
        _, pid = win32process.GetWindowThreadProcessId(hwnd)
        process = psutil.Process(pid)
        is_running = psutil.pid_exists(pid)
        print(f"Process {process.name()} is {'running' if is_running else 'not running'}")
        return is_running
    except psutil.NoSuchProcess:
        print("Process not found")
        return False


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

    # print(f"load_data: \n{json.dumps(data, sort_keys=True, indent=4)}")
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
            # json.dump(data, file) # fastest, but doesn't allow formatting - and i use tiny jsons
            pretty_json = json.dumps(data, sort_keys=True, indent=4)
            file.write(pretty_json)
    except (FileNotFoundError, TypeError):
        print(f"Error saving data to {PERSISTENT_DATA_PATH}")

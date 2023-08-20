# pylint: disable=broad-exception-caught
"""Functions used throughout the program"""
import ctypes
import json
import os
import random
import shutil
import string
import sys
import tempfile
import time
import tkinter as tk
import winreg
from tkinter import filedialog

import psutil
import pyautogui
import vdf  # type: ignore
import win32con  # type: ignore
import win32gui
import win32process

from .constants import NEW_HUD_DIR, PERSISTENT_DATA_PATH


def generate_random_string(length=8):
    "Generate random string"
    characters = string.ascii_letters + string.digits
    return "".join(random.choice(characters) for _ in range(length))


def rename_with_timeout(src, dst, timeout=5):
    """Try to rename src to dst within timeout seconds.

    This aims to work around some possible exceptions:
    - A program that's shutting down is still temporary locking them
    - Miscelanious operating system issue where renaming fails once but is fine the next time"""
    start = time.time()

    print(f"Renaming {src} -> {dst} with timeout: {timeout}")

    while True:
        try:
            os.rename(src, dst)
            return True
        except Exception:
            if time.time() - start > timeout:
                print("Failed to rename!")
                return False
            else:
                time.sleep(0.1)


def create_temp_dir_from_input_dir_exclude_files_without_extension(input_dir):
    # pylint: disable=unused-variable
    """
    Creates a temporary directory and copies the contents of the input directory to it,
    excluding any files without a file extension.

    :param input_dir: The path of the input directory.
    :type input_dir: str
    :return: The path of the temporary directory.
    :rtype: str
    """
    temp_dir = tempfile.mkdtemp()
    for root, dirs, files in os.walk(input_dir):
        for file in files:
            if "." in file:
                file_path = os.path.join(root, file)
                temp_path = os.path.join(temp_dir, file)
                shutil.copy2(file_path, temp_path)
    return temp_dir


def focus_hwnd(hwnd):
    # pylint: disable=c-extension-no-member
    """
    Function to focus a window.

    Alternate way to do this:
        # use pywinauto to get around SetForegroundWindow error/limitation: https://stackoverflow.com/a/30314197
        # be aware that pywinauto moves the cursor. which has a side effect of
        # for example moving the camera in source games
        from pywinauto import Application
        game_app = Application().connect(handle=game_hwnd)
        game_app.top_window().set_focus()
    """

    # Check if the window handle is valid
    if not win32gui.IsWindow(hwnd):
        return

    try:
        # Set the window to the foreground
        win32gui.SetForegroundWindow(hwnd)

        # # If the window is minimized, restore it
        if win32gui.IsIconic(hwnd):
            win32gui.ShowWindow(hwnd, win32con.SW_RESTORE)

        # # Bring the window to the top
        win32gui.BringWindowToTop(hwnd)

        # # Set the window's position and size to the foreground
        win32gui.SetWindowPos(hwnd, win32con.HWND_TOPMOST, 0, 0, 0, 0, win32con.SWP_NOMOVE | win32con.SWP_NOSIZE)

        # Set the window to topmost
        win32gui.SetWindowPos(hwnd, win32con.HWND_TOPMOST, 0, 0, 0, 0, win32con.SWP_NOMOVE | win32con.SWP_NOSIZE)

        # Disable topmost
        win32gui.SetWindowPos(hwnd, win32con.HWND_NOTOPMOST, 0, 0, 0, 0, win32con.SWP_NOMOVE | win32con.SWP_NOSIZE)

        # # Activate the window
        win32gui.SetActiveWindow(hwnd)  # <- this works for tkinter gui's in combination with topmost
    except ValueError:
        print("Could not focus window")


def is_valid_window(hwnd):
    "Verify window"
    return ctypes.windll.user32.IsWindow(hwnd)


def prompt_for_folder(title):
    """Prompt user for a folder"""
    root = tk.Tk()
    root.withdraw()
    return filedialog.askdirectory(title=title)


def prompt_add_existing_hud(persistent_data):
    """Prompt user for hud folder to add"""
    folder_path = prompt_for_folder("Add HUD: Select folder")
    if folder_path:
        persistent_data["stored_huds"].append(folder_path)
        print(f'stored_huds: {persistent_data["stored_huds"]}')
        return True
    else:
        return False


def prompt_open_temp_hud(persistent_data):
    """Prompt user for temp hud folder to add"""
    folder_path = prompt_for_folder("Add HUD: Select folder")
    if folder_path:
        persistent_data["stored_temp_huds"].append(folder_path)
        print(f'stored_temp_huds: {persistent_data["stored_temp_huds"]}')
        return True
    else:
        return False


def prompt_create_new_hud(persistent_data):
    """Prompt user for hud folder to create a new hud in"""
    folder_path = prompt_for_folder("New HUD: Select folder")
    if folder_path:
        persistent_data["stored_huds"].append(folder_path)
        copy_directory(NEW_HUD_DIR, folder_path)
        print(f'stored_huds: {persistent_data["stored_huds"]}')
        return True
    else:
        return False


def remove_stored_hud(persistent_data, hud_dir):
    """Remove stored hud"""
    if hud_dir in persistent_data["stored_huds"]:
        persistent_data["stored_huds"].remove(hud_dir)
        print(f"Removed '{hud_dir}'")


def remove_temp_hud(persistent_data, hud_dir):
    """Remove temp hud"""
    if hud_dir in persistent_data["stored_temp_huds"]:
        persistent_data["stored_temp_huds"].remove(hud_dir)
        print(f"Removed '{hud_dir}'")


def retrieve_hud_name_for_dir(hud_dir):
    """Retrieve hud name for a directory. Either directory name or from addoninfo.txt"""
    # verify input
    if not os.path.isdir(hud_dir):
        raise ValueError(f"Invalid hud_dir directory path: '{hud_dir}'")

    # retrieve hud name (from addoninfo.txt if available)
    # hud_name = os.path.basename(os.path.dirname(hud_dir)) # retrieve name from parent folder
    hud_name = os.path.basename(hud_dir)  # retrieve name from root folder
    addoninfo_path = os.path.normpath(os.path.join(hud_dir, "addoninfo.txt"))

    if os.path.exists(addoninfo_path):
        addon_info = vdf.load(open(addoninfo_path, encoding="utf-8"))

        if addon_info.get("AddonInfo", {}).get("addontitle"):
            hud_name = addon_info["AddonInfo"]["addontitle"]
            print(f"Hud name: Retrieved '{hud_name}' @ '{addoninfo_path}'")
        else:
            print(f"Hud name: Addoninfo.txt does not have addontitle set! @ '{addoninfo_path}'")
    else:
        print(f"Hud name: Addoninfo.txt does not exist @ '{addoninfo_path}' setting hud_name to '{hud_name}'")
    return hud_name


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
    print(f"Waiting for {exe} to run")
    start_time = time.time()
    while True:
        for process_name in psutil.process_iter():
            if process_name.name() == exe:
                print(f"Process {exe} running!")
                return True
        if timeout is not None and time.time() - start_time > timeout:
            print("Timeout reached!")
            return False
        time.sleep(0.1)


def wait_for_process_with_ram_threshold(exe, timeout=None):
    """
    Wait until a process is running and consumes a specified amount of RAM.

    :param exe: The executable name of the process.
    :type exe: str
    :param timeout: The maximum time to wait in seconds (optional).
    :type timeout: float or None
    :return: True if the process is found and RAM threshold is reached, False if timeout is reached.
    :rtype: bool
    """
    ram_threshold_mb = 222  # Hardcoded RAM threshold in MB
    print(f"Waiting for {exe} to run and use {ram_threshold_mb} MB of RAM")

    start_time = time.time()
    while True:
        for process in psutil.process_iter(attrs=["name", "pid", "memory_info"]):
            if process.info["name"] == exe:
                # process_pid = process.info['pid']
                process_memory_info = process.info["memory_info"]
                ram_used_mb = process_memory_info.rss / (1024 * 1024)  # Convert bytes to MB

                if ram_used_mb >= ram_threshold_mb:
                    print(f"Process {exe} running and using {ram_used_mb:.2f} MB of RAM.")
                    return True

        if timeout is not None and time.time() - start_time > timeout:
            print("Timeout reached!")
            return False

        time.sleep(0.1)


def wait_process_close(executable, timeout=None):
    "Wait for a process to close (if it exists)"
    print(f"Waiting for {executable} to close")

    # Get the list of processes with the same name as the executable
    processes = [p for p in psutil.process_iter() if p.name() == executable]
    # If no processes are found, return immediately
    if not processes:
        print(f"{executable} to not running!")
        return False
    # Otherwise, wait for the processes to terminate or until timeout is reached
    start = time.time()
    while True:
        # Check if any process is still alive
        alive = any(p.is_running() for p in processes)
        # If not, return
        if not alive:
            print(f"Process {executable} closed!")
            return True
        # Otherwise, check the elapsed time if timeout is provided
        if timeout is not None:
            elapsed = time.time() - start
            # If timeout is reached, raise an exception
            if elapsed >= timeout:
                print(f"Process {executable} did not close after {timeout} seconds")
                return False
        # Sleep for a short interval and repeat
        time.sleep(0.1)


def get_hwnd_for_exe(executable_name):
    # pylint: disable=c-extension-no-member
    """
    Retrieves the window handle for a process based on its executable name.
    """
    for proc in psutil.process_iter(["name"]):
        if proc.info["name"] == executable_name:
            pid = proc.pid
            handle_list = []

            def callback(handle, handle_list):
                handle_list.append(handle)

            win32gui.EnumWindows(callback, handle_list)
            for handle in handle_list:
                if win32process.GetWindowThreadProcessId(handle)[1] == pid:
                    return handle
    return None


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

    # if process_running:
    #     print(f"{process_name} is running")
    # else:
    #     print(f"{process_name} is not running")

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


def copy_directory(src_dir, dest_dir, ignore_file=None):
    "Copy the files in asource directory to a destination directory, overwriting if necessary."
    # pylint: disable=broad-exception-raised, broad-exception-caught

    try:
        # Normalize paths
        src_dir = os.path.normpath(src_dir)
        dest_dir = os.path.normpath(dest_dir)

        # Verify and create destination directory if needed
        if not os.path.exists(dest_dir):
            os.makedirs(dest_dir)
        elif not os.path.isdir(dest_dir):
            raise NotADirectoryError(f"The destination directory {dest_dir} is not valid.")

        # Build a list of source files to be copied
        src_files = [
            os.path.join(root, filename)
            for root, _, files in os.walk(src_dir)
            for filename in files
            if filename != ignore_file
        ]

        # Raise exception if no source files found
        if not src_files:
            raise Exception(f"No files in the source directory: {src_dir}")

        # Copy each source file to the destination
        for src_path in src_files:
            relative_path = os.path.relpath(src_path, src_dir)
            dest_path = os.path.join(dest_dir, relative_path)

            # Create the destination directory if it doesn't exist
            relative_dir = os.path.dirname(dest_path)
            if not os.path.exists(relative_dir):
                os.makedirs(relative_dir)

            # Attempt to copy the file, handle errors
            try:
                shutil.copy2(src_path, dest_path)
                print(f"Copied {src_path} -> {dest_path}")
            except shutil.Error as copy_error:
                print(f"Copy error: {copy_error}")
            except Exception as general_error:
                print(f"An error occurred: {general_error}")

    except Exception as err_info:
        print(f"An error occurred during copy files in directory: {err_info}")
    else:
        print(f"Copied files '{src_dir}' -> '{dest_dir}'")


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


def move_cursor_to(coordinates):
    # pylint: disable=invalid-name
    """
    Moves the mouse cursor to the specified (x, y) coordinate on screen.

    Arguments:
    coordinates -- a tuple with (x, y) values representing the desired cursor position.
    """
    x, y = coordinates[0], coordinates[1]
    pyautogui.moveTo(x, y)


def click_at(coordinates):
    # pylint: disable=invalid-name
    """
    Performs a left mouse click at the specified (x, y) coordinate on screen.

    Arguments:
    coordinates -- a tuple with (x, y) values representing the desired click position.
    """
    x, y = coordinates[0], coordinates[1]
    pyautogui.click(x, y)


def get_mouse_position_on_click(callback):
    """
    Calls the callback function with the x, y coordinates of where the user clicks the mouse on the screen.

    This function creates a fullscreen window that listens for a mouse click event.
    When clicked, it destroys the window and calls the callback function with the (x,y) coordinates of the click.
    If the user cancels the operation or closes the window, the function calls the callback function with (None,None).
    """
    root = tk.Tk()
    root.attributes("-fullscreen", True)  # make window fullscreen
    root.attributes("-topmost", True)  # keep window on top
    root.attributes("-alpha", 0.1)  # set transparency to 0.5 (125/255)
    root.overrideredirect(True)  # remove window decorations

    def on_click(event):
        pos_x, pos_y = event.x_root, event.y_root
        print(f"Mouse clicked at ({pos_x}, {pos_y})")
        root.destroy()  # destroy the window when mouse is clicked
        callback(pos_x, pos_y)

    root.bind("<ButtonPress>", on_click)
    root.mainloop()


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

    # if needed set default lists so they can be added to
    if "stored_temp_huds" not in data:
        data["stored_temp_huds"] = []

    if "game_mute" not in data:
        data["game_mute"] = False

    if "game_insecure" not in data:
        data["game_insecure"] = False

    if "game_pos" not in data:
        data["game_pos"] = "Center"

    if "game_pos_custom_coord" not in data:
        data["game_pos_custom_coord"] = None

    if "game_mode" not in data:
        data["game_mode"] = "Coop"

    if "game_res" not in data:
        data["game_res"] = (1600, 900)

    if "reload_reopen_menu_on_reload" not in data:
        data["reload_reopen_menu_on_reload"] = False

    if "reload_mouse_clicks_enabled" not in data:
        data["reload_mouse_clicks_enabled"] = False

    if "reload_mouse_clicks_coord_1" not in data:
        data["reload_mouse_clicks_coord_1"] = None

    if "reload_mouse_clicks_coord_2" not in data:
        data["reload_mouse_clicks_coord_2"] = None

    if "editor_reload_mode" not in data:
        data["editor_reload_mode"] = "reload_hud"

    # print(f"load_data: \n{json.dumps(data, sort_keys=True, indent=4)}")
    return data


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


def save_and_exit_script(persistent_data):
    """Exit the script"""
    # pylint: disable=import-outside-toplevel # importing outside top level to avoid circular imports
    from hud.hud import Hud

    Hud(persistent_data).finish_editing(open_start_gui=False)
    save_data(persistent_data)
    sys.exit()

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
from tkinter import filedialog

import psutil
import pyautogui
import win32con
import win32gui
import win32process

from utils.persistent_data import PersistentDataManager

from .constants import (
    BACKUP_APPEND_STRING,
    FILE_EXT_FOLDER_ICON,
    FILE_EXT_IMAGES,
    FILE_EXT_WARNING_ICON,
    PERSISTENT_DATA_PATH,
)


def get_backup_path(file_path):
    """Get a backup path by appending 'append backup string' to the input file path"""
    backup_path = file_path + BACKUP_APPEND_STRING
    return backup_path


def get_backup_filename(file_name):
    """Get a backup file name by appending 'append backup string' to the input file path"""
    backup_file_name = file_name + BACKUP_APPEND_STRING
    return backup_file_name


def get_image_for_file_extension(input_path):
    "Retrieve image for file extension"

    # Get the file extension
    file_extension = os.path.splitext(input_path)[1]

    if not file_extension:
        print(f"Retrieved image for directory {input_path} {FILE_EXT_FOLDER_ICON}")
        return FILE_EXT_FOLDER_ICON

    # Define the file types and their corresponding icons
    file_types = {
        ".txt": os.path.join(FILE_EXT_IMAGES, "text.ico"),
        ".res": os.path.join(FILE_EXT_IMAGES, "resource.ico"),
        ".cfg": os.path.join(FILE_EXT_IMAGES, "config.ico"),
        ".jpg": os.path.join(FILE_EXT_IMAGES, "image.ico"),
        ".png": os.path.join(FILE_EXT_IMAGES, "image.ico"),
        ".vmt": os.path.join(FILE_EXT_IMAGES, "resource.ico"),
        ".vtf": os.path.join(FILE_EXT_IMAGES, "image.ico"),
    }

    # Get the corresponding image path or return "warning.png"
    output_image_path = file_types.get(file_extension, FILE_EXT_WARNING_ICON)

    print(f"Retrieved image for {input_path} -> {output_image_path}")
    return output_image_path


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

    # Get the list of processes with the same name as the executable
    processes = [p for p in psutil.process_iter() if p.name() == executable]
    # If no processes are found, return immediately
    if not processes:
        print(f"{executable} is not running!")
        return False

    # Otherwise, wait for the processes to terminate or until timeout is reached
    print(f"Waiting for {executable} to close")
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
    try:
        with open(PERSISTENT_DATA_PATH, "r", encoding="utf-8") as file:
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


def save_and_exit_script():
    """Exit the script"""
    # pylint: disable=import-outside-toplevel # importing outside top level to avoid circular imports
    from hud.hud import Hud

    hud_instance = Hud()
    hud_instance.finish_editing(open_start_gui=False)
    PersistentDataManager().save()
    sys.exit()

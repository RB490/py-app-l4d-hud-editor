"""Functions used throughout the program"""
import shutil
import json
import os
import winreg
import time
import tempfile
import tkinter as tk
from tkinter import filedialog
from typing import Optional
import pyautogui
import win32gui
import win32process
import win32api
import win32con
import psutil
import vdf
from .constants import GAME_POSITIONS, NEW_HUD_DIR, PERSISTENT_DATA_PATH


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
        # note that pywinauto moves the cursor. which has a side effect of
        # for example moving the camera in source games
        from pywinauto import Application
        game_app = Application().connect(handle=game_hwnd)
        game_app.top_window().set_focus()
    """

    # Check if the window handle is valid
    if not win32gui.IsWindow(hwnd):
        return

    # Set the window to the foreground
    win32gui.SetForegroundWindow(hwnd)

    # If the window is minimized, restore it
    if win32gui.IsIconic(hwnd):
        win32gui.ShowWindow(hwnd, win32con.SW_RESTORE)

    # Bring the window to the top
    win32gui.BringWindowToTop(hwnd)

    # Set the window's position and size to the foreground
    win32gui.SetWindowPos(hwnd, win32con.HWND_TOPMOST, 0, 0, 0, 0, win32con.SWP_NOMOVE | win32con.SWP_NOSIZE)

    # Activate the window
    win32gui.SetActiveWindow(hwnd)


def move_hwnd_to_position(hwnd, position):
    # pylint: disable=c-extension-no-member, unsubscriptable-object
    """
    This function moves a window (specified by its hwnd) to the desired position on the screen.
    `position` is a string that can take values from GAME_POSITIONS list.
    """

    # Validate the position argument
    assert position in GAME_POSITIONS, "Invalid position"

    # Save the handle of the currently focused window
    focused_hwnd = win32gui.GetForegroundWindow()

    # Get the current dimensions of the window
    rect = win32gui.GetWindowRect(hwnd)
    win_width = rect[2] - rect[0]
    win_height = rect[3] - rect[1]

    # Position the window according to the selected position argument
    if position == "Center":
        # Move the window to the topmost position and center it on the screen
        win32gui.SetWindowPos(
            hwnd,
            win32con.HWND_TOPMOST,
            0,
            0,
            0,
            0,
            win32con.SWP_NOMOVE | win32con.SWP_NOSIZE | win32con.SWP_SHOWWINDOW,
        )
        # Remove the topmost attribute so that other windows can be on top of this one
        win32gui.SetWindowPos(
            hwnd,
            win32con.HWND_NOTOPMOST,
            0,
            0,
            0,
            0,
            win32con.SWP_NOMOVE | win32con.SWP_NOSIZE | win32con.SWP_SHOWWINDOW,
        )
        # Calculate the new coordinates for the window to be centered on the screen
        win_x = (win32api.GetSystemMetrics(0) - win_width) // 2
        win_y = (win32api.GetSystemMetrics(1) - win_height) // 2
        # Move the window to the calculated coordinates
        win32gui.SetWindowPos(hwnd, None, win_x, win_y, win_width, win_height, win32con.SWP_NOZORDER)

    # Repeat the same process for each possible position on the screen
    elif position == "Top Left":
        win_x = 0
        win_y = 0
        win32gui.SetWindowPos(hwnd, None, win_x, win_y, win_width, win_height, win32con.SWP_NOZORDER)

    elif position == "Top Right":
        win_x = win32api.GetSystemMetrics(0) - win_width
        win_y = 0
        win32gui.SetWindowPos(hwnd, None, win_x, win_y, win_width, win_height, win32con.SWP_NOZORDER)

    elif position == "Bottom Left":
        win_x = 0
        win_y = win32api.GetSystemMetrics(1) - win_height
        win32gui.SetWindowPos(hwnd, None, win_x, win_y, win_width, win_height, win32con.SWP_NOZORDER)

    elif position == "Bottom Right":
        win_x = win32api.GetSystemMetrics(0) - win_width
        win_y = win32api.GetSystemMetrics(1) - win_height
        win32gui.SetWindowPos(hwnd, None, win_x, win_y, win_width, win_height, win32con.SWP_NOZORDER)

    elif position == "Top":
        win_x = (win32api.GetSystemMetrics(0) - win_width) // 2
        win_y = 0
        win32gui.SetWindowPos(hwnd, None, win_x, win_y, win_width, win_height, win32con.SWP_NOZORDER)

    elif position == "Bottom":
        win_x = (win32api.GetSystemMetrics(0) - win_width) // 2
        win_y = win32api.GetSystemMetrics(1) - win_height
        win32gui.SetWindowPos(hwnd, None, win_x, win_y, win_width, win_height, win32con.SWP_NOZORDER)

    elif position == "Left":
        win_x = 0
        win_y = (win32api.GetSystemMetrics(1) - win_height) // 2
        win32gui.SetWindowPos(hwnd, None, win_x, win_y, win_width, win_height, win32con.SWP_NOZORDER)

    elif position == "Right":
        win_x = win32api.GetSystemMetrics(0) - win_width
        win_y = (win32api.GetSystemMetrics(1) - win_height) // 2
        win32gui.SetWindowPos(hwnd, None, win_x, win_y, win_width, win_height, win32con.SWP_NOZORDER)

    # Restore focus to the previously focused window
    focus_hwnd(focused_hwnd)

    # Print information
    _, pid = win32process.GetWindowThreadProcessId(hwnd)
    window_executable = os.path.basename(psutil.Process(pid).exe())
    print(f"Moved '{window_executable}' to '{position}'")


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
        copy_directory_contents(NEW_HUD_DIR, folder_path)
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
    assert os.path.isdir(hud_dir)

    # retrieve hud name (from addoninfo.txt if available)
    # hud_name = os.path.basename(os.path.dirname(hud_dir)) # retrieve name from parent folder
    hud_name = os.path.basename(hud_dir)  # retrieve name from root folder
    addoninfo_path = os.path.normpath(os.path.join(hud_dir, "addoninfo.txt"))

    if os.path.exists(addoninfo_path):
        addon_info = vdf.load(open(addoninfo_path, encoding="utf-8"))
        if addon_info["AddonInfo"]["addontitle"]:
            hud_name = addon_info["AddonInfo"]["addontitle"]
            print(f"Retrieved '{hud_name}' @ '{addoninfo_path}'")
        else:
            print(f"Addoninfo.txt does not have addontitle set! @ '{addoninfo_path}'")
    else:
        print(f"Addoninfo.txt does not exist @ '{addoninfo_path}' setting hud_name to '{hud_name}'")
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
    start_time = time.time()
    while True:
        for process_name in psutil.process_iter():
            if process_name.name() == exe:
                return True
        if timeout is not None and time.time() - start_time > timeout:
            return False
        time.sleep(0.1)


def wait_for_process_and_get_hwnd(executable_name: str, timeout_seconds: Optional[int] = 60) -> int:
    # pylint: disable=c-extension-no-member
    """
    Waits for a process to start and returns its window handle (HWND).

    :param executable_name: The name of the executable to wait for.
    :param timeout_seconds: The maximum time to wait for the process to start, in seconds. If None, waits indefinitely.
    :return: The window handle (HWND) of the process.
    :raises: RuntimeError if no window handle is found for the process or if not found within the timeout.
    """

    start_time = time.time()
    while True:
        for proc in psutil.process_iter():
            if proc.name() == executable_name:
                pid = proc.pid
                break
        else:
            if timeout_seconds is not None and time.time() - start_time > timeout_seconds:
                raise RuntimeError(f"Process '{executable_name}' not found within {timeout_seconds} seconds")
            time.sleep(0.1)
            continue
        break

    start_time = time.time()
    while True:

        def callback(hwnd, hwnds):
            _, found_pid = win32process.GetWindowThreadProcessId(hwnd)
            if found_pid == pid:
                hwnds.append(hwnd)
            return True

        hwnds = []
        win32gui.EnumWindows(callback, hwnds)
        if hwnds:
            return hwnds[0]

        if timeout_seconds is not None and time.time() - start_time > timeout_seconds:
            raise RuntimeError(
                f"No window handle found for process '{executable_name}' within {timeout_seconds} seconds"
            )

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

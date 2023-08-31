"""Module for debugging"""
# pylint: disable=unused-import, unused-variable, unused-argument, undefined-variable, invalid-name


import logging
import os
import sys
import threading
import time

import keyboard

from debug.game import debug_game_class
from debug.gui import (
    debug_browser_gui,
    debug_descriptions_gui,
    debug_popup_gui,
    debug_progress_gui,
    debug_start_gui,
    debug_vdf_gui,
)
from debug.hud import get_hud_debug_instance
from game.constants import DirectoryMode, InstallationState, SyncState
from game.game import Game
from game.installer_prompts import prompt_start
from gui.browser import GuiHudBrowser
from gui.popup import GuiEditorMenuPopup
from gui.start import GuiHudStart
from hud.hud import Hud
from shared_utils.hotkey_manager import HotkeyManager, showcase_hotkey_manager
from shared_utils.hwnd_window_manager import (
    HwndWindowUtils,
    showcase_hwnd_window_manager,
)
from shared_utils.logging_manager import LoggerManager, logging_class_usage_example
from shared_utils.shared_utils import show_message
from shared_utils.splash_gui import splash_gui_example
from tests.test_hud_syncer import unit_test_hud_syncer
from utils.constants import HOTKEY_SYNC_HUD, HOTKEY_TOGGLE_BROWSER, ImageConstants
from utils.functions import (
    get_browser_gui,
    get_mouse_position_on_click,
    preform_checks_to_prepare_program_start,
    prompt_for_folder,
    show_start_gui,
)
from utils.persistent_data_manager import PersistentDataManager
from utils.vpk import VPKClass


def debug_function(*args):
    """Debug"""
    print(f"debug_function args={args}")


def execute_debugging_hotkey_method_in_thread():
    "debug hotkey in main thread incase it takes a bit longer and causes issue with the keyboard module"
    thread = threading.Thread(target=hotkey_debugging_method)
    thread.start()

    print("thread finished!!!")


def hotkey_debugging_method():
    "debug hotkey"
    print("hotkey_debugging_method!")
    debug_popup_gui()


def debug_main():
    "Main debug func"
    os.system("cls")  # clear terminal
    print("Started debugging!")
    # hotkeys
    # hotkey_manager = HotkeyManager()
    # hotkey_manager.add_hotkey("CTRL+S", hotkey_debugging_method, suppress=True)
    # hotkey_manager.add_hotkey("F10", hotkey_debugging_method, suppress=True)
    # hotkey_manager.add_hotkey("F12", debug_unsync_hud_func, suppress=True)
    # hotkey_manager.add_hotkey("CTRL+S", execute_debugging_hotkey_method_in_thread, suppress=True)
    # return
    # unit tests
    # unit_test_hud_syncer()

    # manage_focus_example()

    game_class = Game()
    game_class.dir.id.set_sync_state(
        DirectoryMode.DEVELOPER, SyncState.NOT_SYNCED
    )  # prevent restore_developer_directory from activating
    game_class.dir.id.set_installation_state(
        DirectoryMode.DEVELOPER, InstallationState.COMPLETED
    )  # prevent restore_developer_directory from activating
    # game_class.command.execute("reload_fonts")

    hwnd_utils = HwndWindowUtils()
    result = hwnd_utils.get_hwnd_from_process_name_with_timeout_and_optionally_ram_usage("notepad.exe", 15, 25)
    # result = hwnd_utils.get_hwnd_from_process_name("notepad.exe")
    hwnd_utils.wait_close(result)
    # hwnd_utils.close(result)

    # debug_gui()
    # debug_hud_class()
    # debug_game_class()
    # result = game_class.window.run(DirectoryMode.DEVELOPER, write_config=False)  # don't overwrite valve.rc
    # result = game_class.window.restore_saved_position()
    # vpk_instance = VPKClass()
    # my_file = "E:\\Games\\Steam\\steamapps\\common\\Left 4 Dead 2\\left4dead2_dlc3\\pak01_dir.vpk"
    # output_dir = "D:\\Downloads\\New folder"
    # vpk_instance.extract(my_file, output_dir)

    # save_data()
    print(f"result={result}")

    input("Finished debugging! Press enter to exit...")


def debug_hud_class():
    "debug hud class"
    h = get_hud_debug_instance()
    # result = hud.edit.get_all_files_dict()
    # result = hud.edit.get_files_dict()
    h.edit.start_editing(h.edit.get_dir())
    # h.edit.sync()


def debug_unsync_hud_func():
    "debug"

    hud_ins = Hud()
    hud_ins.edit.syncer.unsync()
    print("finished: debug_unsync_hud_func")


def debug_data_manager():
    "debug data manager"
    data_manager = PersistentDataManager()
    PersistentDataManager().save()
    result = data_manager.data
    result = data_manager.print()
    result = data_manager.get("game_mode")
    print(f"result={result}")


def debug_gui():
    "debug gui"

    # splash
    # splash_gui_example()

    # popup
    # debug_popup_gui()

    # browser
    # debug_browser_gui()
    # browser = get_browser_gui()

    # start
    # debug_start_gui()
    show_start_gui()

    # vdf gui
    # debug_vdf_gui()

    # descriptions
    # debug_descriptions_gui()

    # editor menu gui
    # debug_gui_editor_menu()

    # user input (used to retrieve game command)
    # debug_get_user_input()

    # installer
    # debug_progress_gui()


def debug_id_handler(game_class):
    "Debug"
    game_id_handler = game_class.dir.id
    # game_class.dir.id.set_path(DirectoryMode.DEVELOPER)

    # Set the ID location for developer directory
    dir_mode = DirectoryMode.DEVELOPER
    game_id_handler.set_path(dir_mode)

    # Set installation state for developer directory
    installation_state = InstallationState.COMPLETED
    game_id_handler.set_installation_state(dir_mode, installation_state)

    # Set sync state for developer directory
    sync_state = SyncState.FULLY_SYNCED
    game_id_handler.set_sync_state(dir_mode, sync_state)

    # Get installation state for developer directory
    retrieved_installation_state = game_id_handler.get_installation_state(dir_mode)
    if retrieved_installation_state:
        print("Retrieved Installation State:", retrieved_installation_state.name)
    else:
        print("Installation State not found.")

    # Get sync state for developer directory
    retrieved_sync_state = game_id_handler.get_sync_state(dir_mode)
    if retrieved_sync_state:
        print("Retrieved Sync State:", retrieved_sync_state.name)
    else:
        print("Sync State not found.")

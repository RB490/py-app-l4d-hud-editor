"""Module for debugging"""
# pylint: disable=unused-import, unused-variable, unused-argument, undefined-variable, invalid-name


import logging
import os
import sys

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
from shared_utils.logging_manager import LoggerManager, logging_class_usage_example
from shared_utils.window_focus_manager import manage_focus_example
from tests.test_hud_syncer import unit_test_hud_syncer
from utils.constants import HOTKEY_TOGGLE_BROWSER, ImageConstants
from utils.functions import (
    get_browser_gui,
    preform_checks_to_prepare_program_start,
    show_start_gui,
)
from utils.persistent_data_manager import PersistentDataManager


def debug_unsync_hud_func():
    "debug"
    hud_ins = Hud()
    hud_ins.edit.syncer.unsync()
    print("finished: debug_unsync_hud_func")


def debug_main():
    "Main debug func"
    os.system("cls")  # clear terminal
    print("Started debugging!")

    # hotkeys
    keyboard.add_hotkey("F12", debug_unsync_hud_func, suppress=True)

    # unit tests
    # unit_test_hud_syncer()

    manage_focus_example()

    # game_class = Game()
    # game_class.command.execute("reload_fonts")
    # game_class.window.restore_saved_position()

    # debug_gui()
    # debug_hud_class()

    # save_data()
    # print(f"result={result}")

    input("Finished debugging! Press enter to exit...")


def debug_hud_class():
    "debug hud class"
    h = get_hud_debug_instance()
    # result = hud.edit.get_all_files_dict()
    # result = hud.edit.get_files_dict()
    h.edit.sync()


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

    # popup
    # debug_popup_gui()

    # browser
    debug_browser_gui()
    # browser = get_browser_gui()

    # start
    # debug_start_gui()
    # show_start_gui()

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

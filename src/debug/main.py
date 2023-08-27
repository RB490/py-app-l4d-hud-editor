"""Module for debugging"""
# pylint: disable=unused-import, unused-variable, unused-argument, undefined-variable, invalid-name


import os
import sys

import keyboard

from debug.game import debug_game_class
from debug.gui import debug_browser_gui, debug_popup_gui
from debug.hud import get_hud_debug_instance
from game.game import Game
from game.installer_prompts import prompt_start
from gui.browser import GuiHudBrowser, show_browser_gui
from gui.popup import GuiEditorMenuPopup, get_editor_menu_popup_gui
from gui.start import GuiHudStart, show_start_gui
from tests.test_hud_syncer import unit_test_hud_syncer
from utils.constants import HOTKEY_TOGGLE_BROWSER, ImageConstants
from utils.functions import preform_checks_to_prepare_program_start
from utils.persistent_data_manager import PersistentDataManager


def dummy_func():
    print("dummy_func")


def debug_main():
    "Main debug func"
    os.system("cls")  # clear terminal
    print("Started debugging!")

    # data_manager = PersistentDataManager()
    # PersistentDataManager().save()
    # result = data_manager.data
    # result = data_manager.print()
    # result = data_manager.get("game_mode")

    # unit_test_hud_syncer()

    # h = get_hud_debug_instance()
    # result = h.edit.get_all_files_dict()
    # result = h.desc.get_custom_file_status("scripts\\hudlayout2.res")

    # debug_game_class()
    # print(sys.path)
    # from shared_modules import my_shared_function

    # keyboard.add_hotkey("F2", dummy_func, suppress=True)
    # keyboard.add_hotkey(HOTKEY_TOGGLE_BROWSER, dummy_func, suppress=True)

    # my_shared_function()
    # debug_vdf_class()
    # get_editor_menu_popup_gui()
    debug_gui()
    # result = "Y" if h.desc.get_custom_file_status("scripts\\hudlayout2.res") else "N"
    # custom_prompt_example_usage()
    # data_manager = PersistentDataManager()
    # data_manager.set("game_mute", 0)
    # data_manager.get("stored_huds")

    # show_start_gui()
    # show_browser_gui()

    # hud = get_hud_debug_instance()
    # result = hud.edit.get_all_files_dict()
    # result = hud.edit.get_files_dict()

    # save_data()
    # print(f"result={result}")

    input("Finished debugging! Press enter to exit...")


def debug_gui():
    "debug gui"

    # popup
    # debug_popup_gui()

    # browser
    debug_browser_gui()
    # show_browser_gui()

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

"""Module for debugging"""
# pylint: disable=unused-import, unused-variable, unused-argument, undefined-variable


import os
import sys

from debug.game import debug_game_class
from debug.gui import (
    debug_descriptions_gui,
    debug_get_user_input,
    debug_progress_gui,
    debug_start_gui,
    debug_vdf_gui,
    get_debug_gui_browser_instance,
)
from debug.hud import get_hud_debug_instance
from game.game import Game
from game.installer_prompts import prompt_start
from gui.browser import GuiHudBrowser
from gui.start import GuiHudStart
from tests.test_hud_syncer import unit_test_hud_syncer
from utils.persistent_data_manager import PersistentDataManager


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

    # debug_game_class()
    # debug_vdf_class()
    debug_gui()

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

    # browser
    # browse = get_debug_gui_browser_instance()
    # browse.show()

    # start
    debug_start_gui()

    # vdf gui
    # debug_vdf_gui()

    # descriptions
    # debug_descriptions_gui()

    # editor menu gui
    # my_editor_menu_gui = GuiEditorMenuPopupContextmenu()
    # my_editor_menu_gui.show()
    # my_editor_menu_gui.show()

    # user input (used to retrieve game command)
    # debug_get_user_input()

    # installer
    # debug_progress_gui()

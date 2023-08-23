"""Module for debugging"""
# pylint: disable=unused-import, unused-variable, unused-argument, undefined-variable

import json
import os

import vdf  # type: ignore

from debug.game import debug_game_class
from debug.gui import (
    debug_descriptions_gui,
    debug_get_user_input,
    debug_vdf_gui,
    get_debug_gui_browser_instance,
)
from debug.hud import get_hud_debug_instance
from game.game import Game
from gui import descriptions
from gui.browser import GuiHudBrowser
from gui.popup import GuiEditorMenuPopupContextmenu
from gui.start import GuiHudStart, show_start_gui
from gui.vdf import VDFModifierGUI
from hud.hud import Hud
from utils.constants import DEVELOPMENT_DIR, HUD_DESCRIPTIONS_PATH
from utils.functions import load_data
from utils.persistent_data import PersistentDataManager
from utils.shared_utils import is_subdirectory
from utils.vdf import debug_vdf_class


def debug_main():
    "Main debug func"
    os.system("cls")  # clear terminal
    print("Started debugging!")

    # data_manager = PersistentDataManager()
    # PersistentDataManager().save()
    # result = data_manager.data
    # result = data_manager.print()
    # result = data_manager.get("game_mode")

    # debug_game_class()
    # debug_vdf_class()
    debug_gui()

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

    # descriptions
    # debug_descriptions_gui()

    # start
    # show_start_gui()

    # editor menu gui
    # my_editor_menu_gui = GuiEditorMenuPopupContextmenu()
    # my_editor_menu_gui.show()
    # my_editor_menu_gui.show()

    # vdf gui
    # debug_vdf_gui()

    # user input (used to retrieve game command)
    debug_get_user_input()
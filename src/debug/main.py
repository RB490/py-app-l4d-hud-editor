"""Module for debugging"""
# pylint: disable=unused-import, unused-variable, unused-argument, undefined-variable

import json
import os

import vdf  # type: ignore

from debug.game import debug_game_class
from debug.gui import debug_descriptions_gui, debug_vdf_gui
from debug.hud import get_hud_debug_instance
from game.game import Game
from gui import descriptions
from gui.browser import GuiHudBrowser
from gui.popup import GuiEditorMenuPopupContextmenu
from gui.start import GuiHudStart, show_start_gui
from gui.vdf import VDFModifierGUI
from hud.hud import Hud
from utils.constants import DEVELOPMENT_DIR, HUD_DESCRIPTIONS_PATH
from utils.functions import load_data, save_data
from utils.shared_utils import is_subdirectory
from utils.vdf import debug_vdf_class





def debug_main():
    "Main debug func"
    os.system("cls")  # clear terminal
    print("Started debugging!")
    persistent_data = load_data()


    
    # debug_game_class(persistent_data)
    debug_gui(persistent_data)
    # debug_vdf_class(persistent_data)

    # hud = get_hud_debug_instance(persistent_data)
    # result = hud.get_all_files_dict()
    # result = hud.get_files_dict()

    # print(f"result={result}")

    # save_data(persistent_data)

    input("Finished debugging! Press enter to exit...")


def debug_gui(persistent_data):
    "debug gui"

    # browser
    # browse = get_debug_gui_browser_instance(persistent_data)
    # browse.run()

    # descriptions
    debug_descriptions_gui(persistent_data)

    # start
    # show_start_gui(persistent_data)

    # editor menu gui
    # my_editor_menu_gui = GuiEditorMenuPopupContextmenu(persistent_data)
    # my_editor_menu_gui.run()
    # my_editor_menu_gui.show()

    # vdf gui
    # debug_vdf_gui(persistent_data)

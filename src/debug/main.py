"""Module for debugging"""
# pylint: disable=unused-import, unused-variable, unused-argument

import os

from debug.game import debug_game_class
from debug.hud import get_hud_debug_instance
from gui import descriptions
from gui.browser import GuiHudBrowser
from gui.popup import GuiEditorMenuPopupContextmenu
from gui.start import GuiHudStart, show_start_gui
from hud.hud import Hud
from utils.functions import load_data
from utils.shared_utils import is_subdirectory


def debug_main():
    "Main debug func"
    os.system("cls")  # clear terminal
    print("debug_main")
    persistent_data = load_data()

    # debug_game_class(persistent_data)
    debug_gui(persistent_data)

    input("Finished debugging! Press enter to continue..")


def debug_gui(persistent_data):
    "debug gui"

    # descriptions
    # descriptions_gui = descriptions.GuiHudDescriptions(persistent_data, "scripts\\hudlayout.res")
    # descriptions_gui.run()

    # start
    show_start_gui(persistent_data)

    # browser

    # browse = get_debug_gui_browser_instance(persistent_data)
    # browse.run()

    # editor menu gui
    # my_editor_menu_gui = GuiEditorMenuPopupContextmenu(persistent_data)
    # my_editor_menu_gui.run()
    # my_editor_menu_gui.show()


def get_debug_gui_browser_instance(persistent_data):
    "debug_gui_browser"
    print("debug_browser")
    hud_inc = get_hud_debug_instance(persistent_data)  # set active debug hud to load files into browser
    return GuiHudBrowser(persistent_data)

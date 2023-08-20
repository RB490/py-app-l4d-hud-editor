"""Module for debugging"""
# pylint: disable=unused-import, unused-variable

import os

from debug.game import debug_game_class
from debug.hud import get_hud_debug_instance
from gui.browser import GuiHudBrowser
from hud.hud import Hud
from utils.functions import load_data


def debug_main():
    "Main debug func"
    os.system("cls")  # clear terminal
    print("debug_main")
    persistent_data = load_data()

    # debug_game_class(persistent_data)

    # start_gui = GuiHudStart(persistent_data)
    # start_gui.run()

    hud_inc = get_hud_debug_instance(persistent_data)

    # browse = get_debug_gui_browser_instance(persistent_data)
    # browse.run()

    # debug_hud_syncer()

    input("Finished debugging! Press enter to continue..")


def get_debug_gui_browser_instance(persistent_data):
    "debug_gui_browser"
    print("debug_browser")
    return GuiHudBrowser(persistent_data)

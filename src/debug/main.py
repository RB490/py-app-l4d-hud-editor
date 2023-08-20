"""Module for debugging"""
# pylint: disable=unused-import, unused-variable

import os

from debug.game import debug_game_class
from debug.hud import get_hud_debug_instance
from gui import descriptions
from gui.browser import GuiHudBrowser
from gui.start import GuiHudStart
from hud.hud import Hud
from utils.functions import load_data
from utils.shared_utils import is_subdirectory


def debug_main():
    "Main debug func"
    os.system("cls")  # clear terminal
    print("debug_main")
    persistent_data = load_data()

    # debug_game_class(persistent_data)

    source_dir = "C:\\XboxGames"
    target_dir = "C:\\XboxGames\\Minecraft Launcher"
    is_subdirectory(source_dir, target_dir)

    input("Finished debugging! Press enter to continue..")


def debug_gui(persistent_data):
    "debug gui"
    
    descriptions_gui = GuiHudDescriptions()
    
    start_gui = GuiHudStart(persistent_data)
    start_gui.run()

    # set active debug hud to load files into browser
    hud_inc = get_hud_debug_instance(persistent_data)
    browse = get_debug_gui_browser_instance(persistent_data)
    browse.run()


def get_debug_gui_browser_instance(persistent_data):
    "debug_gui_browser"
    print("debug_browser")
    return GuiHudBrowser(persistent_data)

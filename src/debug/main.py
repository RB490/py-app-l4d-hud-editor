"""Module for debugging"""
# pylint: disable=unused-import

import os

from debug.game import debug_game_class
from utils.functions import load_data


def debug_main():
    os.system("cls")  # clear terminal
    persistent_data = load_data()
    
    print("debug_main")
    debug_game_class(persistent_data)


    # start_gui = GuiHudStart(persistent_data)
    # start_gui.run()

    # hud_inc = Hud(persistent_data)

    # browse = get_debug_gui_browser_instance(persistent_data)
    # browse.run()

    # debug_hud_syncer()

    input("Finished debugging! Press enter to continue..")
"""Module for debugging"""
# pylint: disable=unused-import

import atexit
import os

from game.game import debug_game_class
from gui.browser import get_debug_gui_browser_instance
from utils.functions import load_data, save_data

os.system("cls")  # clear terminal

def exit_handler_1():
    save_data(persistent_data)

atexit.register(exit_handler_1)


persistent_data = load_data()
debug_game_class(persistent_data)

browse = get_debug_gui_browser_instance(persistent_data)
browse.run()

input("Finished! Press enter to continue..")

"""Module for debugging"""
# pylint: disable=unused-import

import os

from game.dir_id_handler import debug_id_handler
from game.game import debug_game_class
from gui.browser import get_debug_gui_browser_instance
from utils.functions import load_data, save_data

os.system("cls")  # clear terminal


persistent_data = load_data()
# debug_game_class(persistent_data)
debug_id_handler(persistent_data)

# browse = get_debug_gui_browser_instance(persistent_data)
# browse.run()

input("Finished! Press enter to continue..")

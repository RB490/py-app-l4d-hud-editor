"""Module for debugging"""
# pylint: disable=unused-import
import os
from packages.game.game import Game
from packages.gui.browser import get_debug_gui_browser_instance
from packages.gui.start import debug_gui_start

from packages.utils.functions import load_data

os.system("cls")  # clear terminal


# setup classes
persistent_data = load_data()
# create initial singleton game class
# hud_instance = get_hud_debug_instance()
# game_instance = Game(persistent_data)
# game_instance2 = Game(persistent_data)
# installer_instance = GameManager(persistent_data, game_instance)
debug_gui_start(persistent_data)
# my_browser = get_debug_gui_browser_instance(persistent_data)
# my_browser.run()


input("Finished! Press enter to continue..")

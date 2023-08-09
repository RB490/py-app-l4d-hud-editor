"""Module for debugging"""
# pylint: disable=unused-import
import os
from packages.game.game import Game
from packages.gui.browser import get_debug_gui_browser_instance

from packages.utils.functions import load_data

os.system("cls")  # clear terminal


# setup classes
persistent_data = load_data()
# create initial singleton game class
# hud_instance = get_hud_debug_instance()
# game_instance = Game(persistent_data)
# game_instance2 = Game(persistent_data)
# installer_instance = GameManager(persistent_data, game_instance)
# my_start = get_gui_start_debug_instance(persistent_data, installer_instance)
my_browser = get_debug_gui_browser_instance(persistent_data)
my_browser.run()
# my_start.run()

# print(hud_instance.get_dir())

# Create instances
# this_is_a_func()
# game_instance_2 = GameSingleton()

# Set a value using game_instance_1


# Access the value using game_instance_2
# print(game_instance_2.data)  # Outputs: Hello, world!


input("Finished! Press enter to continue..")

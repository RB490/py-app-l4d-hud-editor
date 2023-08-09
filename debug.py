"""Module for debugging"""
# pylint: disable=unused-import
import os
import threading
import time
import winsound  # winsound.Beep(1250, 125)
import pyautogui
import keyboard
from packages.editor_menu.menu import EditorMenuClass
from packages.game import Game
from packages.game.game import debug_game_class
from packages.game.manager import GameManager
from packages.gui.browser import GuiHudBrowser, get_debug_gui_browser_instance
from packages.gui.editor_menu import debug_gui_editor_menu
from packages.gui.start import GuiHudStart, get_gui_start_debug_instance
from packages.hud.hud import Hud, debug_hud, get_hud_debug_instance
from packages.hud.descriptions import debug_hud_descriptions
from packages.hud.syncer import debug_hud_syncer
from packages.utils.constants import IMAGES_DIR, KEY_MAP
from packages.utils.functions import load_data, retrieve_hud_name_for_dir

os.system("cls")  # clear terminal


# setup classes
persistent_data = load_data()
# create initial singleton game class
game_instance = Game(persistent_data)

game_instance2 = Game()
# hud_instance = get_hud_debug_instance()
# installer_instance = GameManager(persistent_data, game_instance)
# my_start = get_gui_start_debug_instance(persistent_data, installer_instance, hud_instance)
# my_browser = get_debug_gui_browser_instance(hud_instance, game_instance, persistent_data)
# my_start.run()

print(game_instance2.game_exe)

# Create instances
# this_is_a_func()
# game_instance_2 = GameSingleton()

# Set a value using game_instance_1


# Access the value using game_instance_2
# print(game_instance_2.data)  # Outputs: Hello, world!


input("Finished! Press enter to continue..")

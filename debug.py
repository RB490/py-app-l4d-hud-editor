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


def create_first_gui():
    get_gui_start_debug_instance(persistent_data, installer_instance, hud_instance)


def create_second_gui():
    get_debug_gui_browser_instance(hud_instance, game_instance, persistent_data, start_instance)


def run_gui_in_thread(gui_instance):
    gui_instance.run()


# setup classes
persistent_data = load_data()
game_instance = Game(persistent_data)
hud_instance = get_hud_debug_instance()
installer_instance = GameManager(persistent_data, game_instance)
start_instance = GuiHudStart(persistent_data, game_instance, hud_instance)

# debug_game_class()
# debug_hud_syncer()
# debug_hud()

# Create threads for each GUI
# my_browser = get_debug_gui_browser_instance(hud_instance, game_instance, persistent_data, start_instance)
my_start = get_gui_start_debug_instance(persistent_data, installer_instance, hud_instance)
# my_start.root.after(22, my_start.change_addon_image, os.path.join(IMAGES_DIR, "cross128.png"))
# time.sleep(1)
my_start.run()
# my_start.change_addon_image(os.path.join(IMAGES_DIR, "cross128.png"))
# # thread1 = threading.Thread(target=my_start.run)

# thread1 = threading.Thread(target=run_gui_in_thread, args=(my_start))
# thread1.start()

# print("why does this code not run?")
# my_start.root.after(0, my_start.change_addon_image, os.path.join(IMAGES_DIR, "cross128.png"))
# thread2 = threading.Thread(target=my_browser.run())

# Start both threads
# thread1.start()
# thread2.start()

# debug_gui_start(persistent_data, installer_instance, hud_instance)


input("Finished! Press enter to continue..")

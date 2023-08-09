"""Module for debugging"""
# pylint: disable=unused-import
import os
import time
import winsound  # winsound.Beep(1250, 125)
import pyautogui
import keyboard
from packages.editor_menu.menu import EditorMenuClass
from packages.game import Game
from packages.gui.browser import GuiHudBrowser
from packages.gui.editor_menu import debug_gui_editor_menu
from packages.gui.start import GuiHudStart
from packages.hud.hud import Hud, debug_hud
from packages.hud.descriptions import debug_hud_descriptions
from packages.hud.syncer import debug_hud_syncer
from packages.utils.constants import KEY_MAP
from packages.utils.functions import load_data, retrieve_hud_name_for_dir

os.system("cls")  # clear terminal
persistent_data = load_data()
game_instance = Game(persistent_data)
hud_instance = Hud(game_instance)
start_instance = GuiHudStart(persistent_data, game_instance, hud_instance)
browser_instance = GuiHudBrowser(hud_instance, game_instance, persistent_data, start_instance)

# debug_hud_syncer()
# debug_hud()


# import atexit
# def save_data_before_exit():
#     input("press enter to fully exit the script")
# atexit.register(save_data_before_exit)


# print(f"Game version: {game_instance.get_version()}")
# game_instance.run("dev")
# game_instance.move("Center")
# debug_gui_editor_menu(persistent_data, game_instance, hud_instance, start_instance, browser_instance)


input("Finished! Press enter to continue..")

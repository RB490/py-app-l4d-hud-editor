"""Module for debugging"""
# pylint: disable=unused-import
import os
import time
import winsound  # winsound.Beep(1250, 125)
import pyautogui
import keyboard
from packages.editor_menu.menu import EditorMenuClass
from packages.game import Game
from packages.game.game import debug_game_class
from packages.game.manager import GameManager
from packages.gui.browser import GuiHudBrowser
from packages.gui.editor_menu import debug_gui_editor_menu
from packages.gui.start import GuiHudStart, debug_gui_start
from packages.hud.hud import Hud, debug_hud
from packages.hud.descriptions import debug_hud_descriptions
from packages.hud.syncer import debug_hud_syncer
from packages.utils.constants import KEY_MAP
from packages.utils.functions import load_data, retrieve_hud_name_for_dir

os.system("cls")  # clear terminal
# persistent_data = load_data()
# game_instance = Game(persistent_data)
# hud_instance = Hud(game_instance)
# installer_instance = GameManager(persistent_data, game_instance)
# start_instance = GuiHudStart(persistent_data, game_instance, hud_instance)
# browser_instance = GuiHudBrowser(hud_instance, game_instance, persistent_data, start_instance)

# debug_game_class()
# debug_hud_syncer()
debug_hud()


# debug_gui_start(persistent_data, installer_instance, hud_instance)


input("Finished! Press enter to continue..")

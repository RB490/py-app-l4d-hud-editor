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
from packages.utils.constants import KEY_MAP
from packages.utils.functions import load_data, retrieve_hud_name_for_dir

os.system("cls")  # clear terminal
persistent_data = load_data()
game_instance = Game(persistent_data)
hud_instance = Hud(game_instance)

# debug_hud()


# print(f"Game version: {game_instance.get_version()}")
game_instance.run("dev")
# game_instance.move("Center")
start_instance = GuiHudStart(persistent_data, game_instance, hud_instance)
browser_instance = GuiHudBrowser(hud_instance, game_instance, persistent_data, start_instance)
# debug_gui_editor_menu(persistent_data, game_instance, hud_instance, start_instance, browser_instance)

# game_instance.command._send_keys_in_background(["alt", "f4"])
# game_instance.command.send_keys_in_foreground(["escape"])


# game_instance.command.set_ui_panel("team")
# game_instance.command.execute("reload_hud")
# game_instance.command.set_ui_panel("team")
# game_instance.command.execute("reload_hud")
# game_instance.command.set_ui_panel("team")
# game_instance.command.execute("reload_hud")
# game_instance.command.set_ui_panel("info_window")
# game_instance.command.execute("reload_hud")
# game_instance.command.set_ui_panel("debug_zombie_panel 1")
# game_instance.command.execute("reload_hud")

# game_instance.command.execute("-jump; +jump")

# hud_dir = "D:\\Programming and projects\\l4d-addons-huds\\4. l4d2-2020HUD\\source"
# hud_name = retrieve_hud_name_for_dir(hud_dir)
# print(hud_name)
# debug_hud_browser()
# debug_hud_descriptions()
# winsound.Beep(1250, 125)
input("Finished! Press enter to continue..")

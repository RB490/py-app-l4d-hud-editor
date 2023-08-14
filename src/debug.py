"""Module for debugging"""
# pylint: disable=unused-import

import os
import sys
from msilib import Directory

from utils.steam_info_retriever import SteamInfoRetriever
from game.game import Game
from game_v2.game_v2 import DirectoryMode, GameV2
from gui.browser import get_debug_gui_browser_instance
from gui.start import GuiHudStart, debug_gui_start
from hud.hud import debug_hud
from utils.constants import EDITOR_AUTOEXEC_PATH, PROJECT_ROOT, SCRIPT_DIR
from utils.functions import get_steam_info, load_data
from utils.shared_utils import show_message

os.system("cls")  # clear terminal


############################
# Classes
############################
persistent_data = load_data()
# steam_info = get_steam_info(persistent_data)
# game_v2 = GameV2(persistent_data)
# game_v2.dir.get(DirectoryMode.USER)
# gamev2_instance.my_method()


# Create an instance of the class
steam_info_retriever = SteamInfoRetriever(persistent_data)

# Retrieve Steam root directory
root_dir = steam_info_retriever.get_root_dir()
# print(f"Steam Root Directory: {root_dir}")

# Retrieve Steam games directory
# games_dir = steam_info_retriever.get_games_dir()
# print(f"Steam Games Directory: {games_dir}")

# Retrieve Steam executable path
# exe_path = steam_info_retriever.get_exe_path()
# print(f"Steam Executable Path: {exe_path}")

# Save Steam root directory to persistent data
# steam_info_retriever.save_root_directory()
print("Steam root directory saved to persistent data:", persistent_data)

# result = game_v2.window.get_hwnd()
# result = game_v2.window.run("dev")
# print(f"result: {result}")


# game.dir.set(DirectoryMode.USER)
# game.dir.get(DirectoryMode.USER)
# game.installer.run(DirectoryMode.USER)
# game.installer.


############################
# GUI
############################
# my_browser = get_debug_gui_browser_instance(persistent_data)
# my_browser.run()
# start_instance = GuiHudStart(persistent_data)
# start_instance.run()


input("Finished! Press enter to continue..")

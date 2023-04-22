"""Module that starts the hud editor code"""

# ====================================================================================================
#     Information
# ====================================================================================================

# ====================================================================================================
#     Imports
# ====================================================================================================

import os
import atexit

# pylint: disable=unused-import
from include_modules.class_hud_select import debug_hud_select_gui

# pylint: disable=unused-import
from include_modules.class_hud_syncer import debug_hud_syncer

from include_modules.class_game import Game
from include_modules.class_installer import Installer
from include_modules.constants import PERSISTENT_DATA, SCRIPT_NAME
from include_modules.constants import NEW_HUD_DIR
from include_modules.functions import load_data, save_data_on_exit

# from include_modules.class_game import Game

os.system("cls")  # clear terminal

# ====================================================================================================
#     Load persistent data
# ====================================================================================================

PERSISTENT_DATA = load_data()

# Register the save_data_on_exit function to be called when the script exits
atexit.register(save_data_on_exit, PERSISTENT_DATA)

# ====================================================================================================
#     Auto-execute
# ====================================================================================================

game_instance = Game(PERSISTENT_DATA)
installer_instance = Installer(PERSISTENT_DATA, game_instance)

# debug_hud_syncer()
debug_hud_select_gui(PERSISTENT_DATA, installer_instance)

input(f"{SCRIPT_NAME}: End of auto-execute (Press enter to exit)")

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

from include_modules.constants import PERSISTENT_DATA, SCRIPT_NAME
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

# inst = Installer(PERSISTENT_DATA, game_instance)
# inst.toggle_dev_mode(True)

# game_instance = Game(PERSISTENT_DATA)
# debug_hud_syncer()
debug_hud_select_gui(PERSISTENT_DATA)

input(f"{SCRIPT_NAME}: End of auto-execute (Press enter to exit)")

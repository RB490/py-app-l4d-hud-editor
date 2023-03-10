"""Module that starts the hud editor code"""

# ====================================================================================================
#     Information
# ====================================================================================================

# ====================================================================================================
#     Imports
# ====================================================================================================

import os
import atexit
from include_modules.constants import PERSISTENT_DATA, SCRIPT_NAME
from include_modules.functions import save_data_on_exit
from include_modules.class_game import Game

os.system("cls")  # clear terminal

# ====================================================================================================
#     Load persistent data
# ====================================================================================================

# PERSISTENT_DATA = load_data()

# Register the save_data_on_exit function to be called when the script exits
atexit.register(save_data_on_exit, PERSISTENT_DATA)

# ====================================================================================================
#     Auto-execute
# ====================================================================================================

# inst = Installer(PERSISTENT_DATA, game_instance)
# inst.toggle_dev_mode(True)

game_instance = Game(PERSISTENT_DATA)

input(f"{SCRIPT_NAME}: End of auto-execute (Press enter to exit)")

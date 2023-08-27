"""Module that starts the hud editor code"""

# ====================================================================================================
#     Information
# ====================================================================================================

# ====================================================================================================
#     Imports
# ====================================================================================================

import os
from gui.start import show_start_gui
from utils.functions import preform_checks_and_prepare_program_start
from utils.persistent_data_manager import PersistentDataManager

# from packages.game.game import Game
# from packages.utils.functions import load_data

os.system("cls")  # clear terminal

# ====================================================================================================
#     Auto-execute
# ====================================================================================================

# ----------------------------------
#     Load persistent data
# ----------------------------------

data_manager = PersistentDataManager()

# ----------------------------------
#     Do stuff
# ----------------------------------

preform_checks_and_prepare_program_start()

# create initial singleton game class
show_start_gui()

# ----------------------------------
#     Finish
# ----------------------------------

input("End of auto-execute (Press enter to exit)...")

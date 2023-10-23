"""Module that starts the hud editor code"""

# ====================================================================================================
#     Information
# ====================================================================================================

# ====================================================================================================
#     Imports
# ====================================================================================================

import os

from src.utils.functions import preform_checks_to_prepare_program_start, show_start_gui

# from packages.game.game import Game
# from packages.utils.functions import load_data

os.system("cls")  # clear terminal

# ====================================================================================================
#     Auto-execute
# ====================================================================================================

preform_checks_to_prepare_program_start()
show_start_gui()

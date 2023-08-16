"""Module for debugging"""
# pylint: disable=unused-import

import os

from game.game import debug_game_class
from utils.functions import load_data

os.system("cls")  # clear terminal

persistent_data = load_data()
debug_game_class(persistent_data)

input("Finished! Press enter to continue..")

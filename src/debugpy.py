"""Module for debugging"""
# pylint: disable=unused-import

import os

from game_v2.game_v2 import debug_gamev2_class
from utils.functions import load_data

os.system("cls")  # clear terminal

persistent_data = load_data()
debug_gamev2_class(persistent_data)

input("Finished! Press enter to continue..")

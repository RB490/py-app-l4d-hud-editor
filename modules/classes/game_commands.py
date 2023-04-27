"""This module is a sub class of the game class.
functions related to the game folder such as switching between user/dev modes"""
from modules.utils.functions import get_steam_info


class GameCommands:
    """Sub class of the game class

    Everything related to sending the game commands such as
    - Sending direct console commands
    - Taking 'custom' input such as 'reloadFonts' or 'giveAllItems' and executing the correlating cmds"""

    def __init__(self, persistent_data, game_class):
        self.persistent_data = persistent_data
        self.steam_info = get_steam_info(self.persistent_data)
        self.game = game_class

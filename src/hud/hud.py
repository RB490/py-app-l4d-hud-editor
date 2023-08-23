"""Methods related to editing a hud"""
# pylint: disable=broad-exception-raised, broad-exception-caught


from game.game import Game
from hud.descriptions import HudDescriptions
from hud.editor import HudEditor
from hud.manager import HudManager
from hud.syncer import HudSyncer
from utils.persistent_data import PersistentDataManager
from utils.shared_utils import Singleton


class Hud(metaclass=Singleton):
    """Class to manage hud editing"""

    def __init__(self) -> None:
        self.data_manager = PersistentDataManager()

        self.game = Game()
        self.syncer = HudSyncer()
        self.desc = HudDescriptions()
        self.manager = HudManager()
        self.edit = HudEditor()
        self.hud_dir = None
        self.threaded_timer_game_exit = None
        self.browser = None

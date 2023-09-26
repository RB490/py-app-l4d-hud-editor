"""Methods related to editing a hud"""
# pylint: disable=broad-exception-raised, broad-exception-caught, import-outside-toplevel


from shared_utils.functions import Singleton

from src.hud.descriptions import HudDescriptions
from src.utils.constants import DATA_MANAGER


class Hud(metaclass=Singleton):
    """Class to manage hud editing"""

    def __init__(self) -> None:
        self.data_manager = DATA_MANAGER
        from src.hud.editor import HudEditor
        from src.hud.manager import HudManager

        self.manager = HudManager()
        self.edit = HudEditor()
        self.desc = HudDescriptions()

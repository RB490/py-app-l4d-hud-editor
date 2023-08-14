from enum import Enum, auto

from utils.steam_info_retriever import SteamInfoRetriever


class TitleRetrievalError(Exception):
    pass


class DirModeError(Exception):
    "Custom exception for invalid DirectoryMode parameter"


class DirectoryMode(Enum):
    """Enumeration representing directory modes"""

    USER = auto()
    DEVELOPER = auto()


ID_FILE_NAMES = {
    DirectoryMode.USER: "_user_directory.DoNotDelete",
    DirectoryMode.DEVELOPER: "_hud_development_directory.DoNotDelete",
}

from game_v2.dir import GameV2Dir
from game_v2.installer import GameV2Installer
from game_v2.window import GameV2Window
from utils.shared_utils import Singleton


class GameV2(metaclass=Singleton):
    """Singleton that handles anything related to the game. such as running and installation the dev/user versions"""

    def __init__(self, persistent_data):
        self.persistent_data = persistent_data
        self.window = GameV2Window(self)
        self.dir = GameV2Dir(self)
        self.installer = GameV2Installer(self)
        self.steam = SteamInfoRetriever(persistent_data)

        self.title = "Left 4 Dead 2"

    def get_title(self):
        """Retrieve information"""
        return self.title

    def get_version(self):
        """
        Retrieve game version based on title.

        :return: Game version string ("L4D1" or "L4D2") or None for invalid titles.
        :raises: TitleRetrievalError if the title cannot be retrieved.
        """
        try:
            title = self.get_title().lower()
        except Exception as err_info:
            raise TitleRetrievalError("Error retrieving title") from err_info

        valid_titles = {"left 4 dead": "L4D1", "left 4 dead 2": "L4D2"}
        return valid_titles.get(title, None)

    def validate_dir_mode(self, dir_mode):
        "Validate the dir_mode parameter"
        if not isinstance(dir_mode, DirectoryMode):
            raise DirModeError("Invalid dir_mode parameter. It should be a DirectoryMode enum value.")

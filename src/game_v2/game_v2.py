"Game class"
# pylint: disable=wrong-import-position, ungrouped-imports, protected-access
from enum import Enum, auto

from game_v2.commands import GameV2Commands
from utils.shared_utils import Singleton
from utils.steam_info_retriever import SteamInfoRetriever


class TitleRetrievalError(Exception):
    "Custom exception for invalid TitleRetrievalError parameter"

class InstallationError(Exception):
    "Custom exception for installation errors"

class DirModeError(Exception):
    "Custom exception for invalid DirectoryMode parameter"


class InstallationState(Enum):
    """Enumeration representing installation states"""

    UNKNOWN = auto()  # for example if the id file json was damaged
    COMPLETED = auto()
    # NOT_STARTED = auto()  # hud dev folder created
    # PAUSED = auto()
    # CANCELLED = auto()

    CREATE_DEV_DIR = auto()
    COPYING_FILES = auto()
    VERIFYING_GAME = auto()
    EXTRACTING_PAKS = auto()
    INSTALLING_MODS = auto()
    REBUILDING_AUDIO = auto()


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


class GameV2(metaclass=Singleton):
    """Singleton that handles anything related to the game. such as running and installation the dev/user versions"""

    def __init__(self, persistent_data):
        print(self.__class__.__name__)
        self.persistent_data = persistent_data
        self.window = GameV2Window(self)
        self.installer = GameV2Installer(self)
        self.command = GameV2Commands(self)
        self.steam = SteamInfoRetriever(persistent_data)
        self.dir = GameV2Dir(self)

        self.title = "Left 4 Dead 2"
        self.exe = "left4dead2.exe"

    def get_title(self):
        """Retrieve information"""
        return self.title

    def get_exe(self):
        """Retrieve information"""
        return self.exe

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

    def _validate_dir_mode(self, dir_mode):
        "Validate the dir_mode parameter"
        if not isinstance(dir_mode, DirectoryMode):
            raise DirModeError("Invalid dir_mode parameter. It should be a DirectoryMode enum value.")

    def close(self):
        "Close"
        print("TODO close game")


def debug_gamev2_class(persistent_data):
    "debug game class"
    print("this is a test")

    g_i = GameV2(persistent_data)

    ###########################
    # Installer
    ###########################
    result = g_i.installer._install()
    print(f"install result = {result}")

    ###########################
    # Directory
    ###########################
    # g_i.dir.set(DirectoryMode.USER)
    # g_i.dir.set(DirectoryMode.USER)

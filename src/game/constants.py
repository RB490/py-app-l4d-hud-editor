"Game constants"
from enum import Enum, auto


class TitleRetrievalError(Exception):
    "Custom exception for invalid TitleRetrievalError parameter"


class InstallationError(Exception):
    "Custom exception for installation errors"


class DirModeError(Exception):
    "Custom exception for invalid DirectoryMode parameter"


class DirectoryMode(Enum):
    """Enumeration representing directory modes"""

    USER = auto()
    DEVELOPER = auto()


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
    MAIN_DIR_BACKUP = auto()
    INSTALLING_MODS = auto()
    REBUILDING_AUDIO = auto()

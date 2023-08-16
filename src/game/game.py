"Game class"
# pylint: disable=wrong-import-position, ungrouped-imports, protected-access
import os
import shutil
from enum import Enum, auto

import vdf  # type: ignore

from utils.constants import DUMMY_ADDON_VPK_PATH, EDITOR_AUTOEXEC_PATH
from utils.shared_utils import Singleton, close_process_executable
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


class VideoSettingsModifier:
    "Modify video.txt"

    def __init__(self, config_dir):
        self.config_dir = config_dir
        self.video_settings_path = os.path.join(config_dir, "video.txt")

    def load_video_settings(self):
        "Load"
        if os.path.exists(self.video_settings_path):
            return vdf.load(open(self.video_settings_path, encoding="utf-8"))
        return None

    def save_video_settings(self, video_settings):
        "Save"
        with open(self.video_settings_path, "w", encoding="utf-8") as f_handle:
            vdf.dump(video_settings, f_handle, pretty=True)

    def modify_video_setting(self, setting_key, setting_value):
        "Modify a specific key value"
        video_settings = self.load_video_settings()
        if video_settings is not None:
            video_settings["VideoConfig"][setting_key] = setting_value
            self.save_video_settings(video_settings)

    def set_fullscreen(self, fullscreen_value):
        "Set fullscreen"
        self.modify_video_setting("setting.fullscreen", fullscreen_value)

    def set_nowindowborder(self, nowindowborder_value):
        "Set window border"
        self.modify_video_setting("setting.nowindowborder", nowindowborder_value)

    def get_nowindowborder(self):
        "Get borderless (setting.nowindowborder)"
        video_settings = self.load_video_settings()
        if video_settings is not None:
            return video_settings["VideoConfig"]["setting.nowindowborder"]
        return None

    def get_fullscreen(self):
        "Get fullscreen (setting.fullscreen)"
        video_settings = self.load_video_settings()
        if video_settings is not None:
            return video_settings["VideoConfig"]["setting.fullscreen"]
        return None

    def get_width(self):
        "Get width (setting.defaultres)"
        video_settings = self.load_video_settings()
        if video_settings is not None:
            return video_settings["VideoConfig"]["setting.defaultres"]
        return None

    def get_height(self):
        "Get height (setting.defaultresheight)"
        video_settings = self.load_video_settings()
        if video_settings is not None:
            return video_settings["VideoConfig"]["setting.defaultresheight"]
        return None


# importing after the above enums and exceptions becaus they are needed for the subclasses
from game.commands import GameCommands
from game.dir import GameDir
from game.installer import GameInstaller
from game.window import GameWindow


class Game(metaclass=Singleton):
    """Singleton that handles anything related to the game. such as running and installation the dev/user versions"""

    def __init__(self, persistent_data):
        print(self.__class__.__name__)
        self.persistent_data = persistent_data
        self.window = GameWindow(self)
        self.installer = GameInstaller(self)
        self.command = GameCommands(self)
        self.steam = SteamInfoRetriever(persistent_data)
        self.dir = GameDir(self)

        self.title = "Left 4 Dead 2"
        self.exe = "left4dead2.exe"
        self.app_id = "550"

    def get_title(self):
        """Retrieve information"""
        return self.title

    def get_exe(self):
        """Retrieve information"""
        return self.exe

    def get_app_id(self):
        """Retrieve information"""
        return self.app_id

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

    def _write_config(self):
        # variables
        config_dir = self.dir.get_cfg_dir(DirectoryMode.DEVELOPER)
        valverc_path = os.path.join(config_dir, "valve.rc")
        autoexec_name = os.path.split(EDITOR_AUTOEXEC_PATH)[-1]
        autoexec_path = os.path.join(config_dir, autoexec_name)

        # delete config
        open(os.path.join(config_dir, "config.cfg"), "w", encoding="utf-8").close()
        open(os.path.join(config_dir, "config_default.cfg"), "w", encoding="utf-8").close()

        # write config
        with open(valverc_path, "w", encoding="utf-8") as cfg_file:
            cfg_file.write(f"exec {autoexec_name}")

        shutil.copy(EDITOR_AUTOEXEC_PATH, autoexec_path)

        # append user settings to autoexec
        with open(autoexec_path, "a", encoding="utf-8") as file:
            if self.persistent_data["game_mute"]:
                file.write("\nvolume 0")  # adds the desired text to the file on a new line
            else:
                file.write("\nvolume 1")  # adds the desired text to the file on a new line

        # disable fullscreen in video settings
        video_modifier = VideoSettingsModifier(config_dir)
        video_modifier.set_fullscreen(0)

        print(autoexec_name)

    def _disable_addons(self):
        # variables
        addons_dir = self.dir._get_addons_dir(DirectoryMode.DEVELOPER)

        # disable mods by overwriting them with a dummy vpk (empty file caused ingame console errors)
        dirs = [
            addons_dir,
            os.path.join(addons_dir, "Workshop"),
        ]
        # not recursing so sourcemod doesn't break + game doesn't check subfolders
        # for addons anyways (besides addons/workshop)
        for loop_dir in dirs:
            for root, dirs, files in os.walk(loop_dir):
                for file in files:
                    file_path = os.path.join(root, file)
                    if file.endswith((".dll")):
                        open(file_path, "w", encoding="utf-8").close()
                    if file.endswith((".vpk")):
                        shutil.copy(DUMMY_ADDON_VPK_PATH, file_path)
                        print(f"'{DUMMY_ADDON_VPK_PATH}' -> '{file_path}'.")

    def _validate_dir_mode(self, dir_mode):
        "Validate the dir_mode parameter"
        if not isinstance(dir_mode, DirectoryMode):
            raise DirModeError("Invalid dir_mode parameter. It should be a DirectoryMode enum value.")

    def close(self):
        "Close"
        close_process_executable(self.get_exe())


def debug_game_class(persistent_data):
    "debug game class"
    print("this is a test")

    gamez = Game(persistent_data)

    ###########################
    # Installer
    ###########################
    # result = gamez.installer._install()
    result = gamez.window.run(DirectoryMode.DEVELOPER)
    # result = gamez.command.execute("noclip")
    # result = gamez.command._get_reload_fonts_command()
    # result = gamez.command.execute()
    # result = gamez.command.execute()
    # result = gamez.installer._uninstall()
    # gamez.installer._install()

    # result = gamez.installer._uninstall()
    # result = gamez.installer.__install_mods()
    # result = gamez.window.run(DirectoryMode.DEVELOPER, wait_on_close=120)
    # result = gamez._disable_addons()
    # result = gamez._write_config()

    print(f"install result = {result}")

    ###########################
    # Directory
    ###########################
    # g_i.dir.set(DirectoryMode.USER)
    # g_i.dir.set(DirectoryMode.USER)

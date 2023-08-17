"Game class"
# pylint: disable=wrong-import-position, ungrouped-imports, protected-access
import os
import shutil

# importing after the above enums and exceptions becaus they are needed for the subclasses
from game.commands import GameCommands
from game.constants import DirectoryMode, DirModeError, TitleRetrievalError
from game.dir import GameDir
from game.installer import GameInstaller
from game.video_settings_modifier import VideoSettingsModifier
from game.window import GameWindow
from utils.constants import DUMMY_ADDON_VPK_PATH, EDITOR_AUTOEXEC_PATH
from utils.shared_utils import Singleton, close_process_executable
from utils.steam_info_retriever import SteamInfoRetriever


class Game(metaclass=Singleton):
    """Singleton that handles anything related to the game. such as running and installation the dev/user versions"""

    def __init__(self, persistent_data):
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

    gamez = Game(persistent_data)

    # result = gamez.dir.get(DirectoryMode.USER)

    ###########################
    # Installer
    ###########################
    result = gamez.installer._install()
    # result = gamez.installer._main_dir_backup()
    # print("hi there!")
    # result = gamez.window.run(DirectoryMode.DEVELOPER)
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

    # debug_id_handler(gamez)

    ###########################
    # Directory
    ###########################
    # g_i.dir.set(DirectoryMode.USER)
    # g_i.dir.set(DirectoryMode.USER)

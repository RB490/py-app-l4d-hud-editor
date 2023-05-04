"""Module providing functions related to the game. such as running and installation the dev/user versions"""
import shutil
import os
import subprocess
import psutil
import vdf
from modules.classes.game_manager import GameManager
from modules.classes.game_commands import GameCommands
from modules.utils.functions import get_steam_info, is_process_running, load_data, get_hwnd_for_exe, wait_for_process
from modules.utils.constants import EDITOR_AUTOEXEC_PATH


class Game:
    """Class with functions related to the game. such as running and installation the dev/user versions"""

    def __init__(self, persistent_data):
        self.persistent_data = persistent_data
        self.steam_info = get_steam_info(self.persistent_data)
        self.manager = GameManager(self.persistent_data, self)
        self.command = GameCommands(self.persistent_data, self)

        self.game_title = "Left 4 Dead 2"
        self.game_exe = "left4dead2.exe"
        self.game_appid = 550
        self.game_hwnd = None

        # set metadata
        # self.active_exe = os.path.join(self.active_dir, self.game_exe)
        # print(self.active_exe)
        # self.run("user")
        # input('press enter to force close game')
        # self.close()
        # self.run("dev")

    def set_hwnd(self):
        """Retrieve game hwnd"""
        # print("Searching game window handle")
        self.game_hwnd = get_hwnd_for_exe(self.get_exe())
        if not self.game_hwnd:
            raise LookupError("No window handle was found")
        print(f"{self.get_exe()} hwnd '{self.game_hwnd}'")

    def get_title(self):
        """Retrieve information"""
        return self.game_title

    def get_version(self):
        """Retrieve information"""

        game_title = self.get_title().lower()
        assert game_title in ["left 4 dead", "left 4 dead 2"], "Invalid game title"

        if game_title == "left 4 dead":
            return "L4D1"
        elif game_title == "left 4 dead 2":
            return "L4D2"

    def get_exe(self):
        """Retrieve information"""
        return self.game_exe

    def get_appid(self):
        """Retrieve information"""
        return self.game_appid

    def get_dir(self, mode):
        """Retrieve information"""
        return self.manager.get_dir(mode)

    def get_hwnd(self):
        """Retrieve information"""
        return self.game_hwnd

    def get_main_dir(self, mode):
        """Retrieve information"""
        return self.manager.get_main_dir(mode)

    def is_running(self):
        """Checks if the game is running"""
        return is_process_running(self.get_exe())

    def activate_mode(self, mode):
        """Switch between user/dev modes"""
        return self.manager.activate_mode(mode)

    def _write_config(self):
        # don't alter user installation
        if self.manager.get_active_mode() == "user":
            print("Cancelled writing config for user folder")
            return

        # retrieve variables
        addons_dir = os.path.join(self.get_main_dir("dev"), "Addons")
        config_dir = os.path.join(self.get_main_dir("dev"), "cfg")

        # disable mods by overwriting them with empty files
        dirs = [
            addons_dir,
            os.path.join(addons_dir, "Workshop"),
        ]
        # don't recurse so sourcemod doesn't break + game doesn't check subfolders
        #   for addons anyways besides addons/workshop
        for loop_dir in dirs:
            for root, dirs, files in os.walk(loop_dir):
                for file in files:
                    if file.endswith((".vpk", ".dll")):
                        open(os.path.join(root, file), "w", encoding="utf-8").close()

        # delete config
        open(os.path.join(config_dir, "config.cfg"), "w", encoding="utf-8").close()
        open(os.path.join(config_dir, "config_default.cfg"), "w", encoding="utf-8").close()

        # write config
        autoexec_name = os.path.split(EDITOR_AUTOEXEC_PATH)[-1]
        autoexec_path = os.path.join(config_dir, autoexec_name)

        os.remove(os.path.join(config_dir, "valve.rc"))
        with open(os.path.join(config_dir, "valve.rc"), "w", encoding="utf-8") as cfg_file:
            cfg_file.write(f"exec {autoexec_name}")

        shutil.copy(EDITOR_AUTOEXEC_PATH, autoexec_path)

        # disable fullscreen in video settings
        video_settings_path = os.path.join(config_dir, "video.txt")
        if os.path.exists(video_settings_path):
            video_settings = vdf.load(open(video_settings_path, encoding="utf-8"))
            video_settings["VideoConfig"]["setting.fullscreen"] = 0
            vdf.dump(video_settings, open(video_settings_path, "w", encoding="utf-8"), pretty=True)

    def close(self):
        """Close game"""
        for proc in psutil.process_iter(["name"]):
            if proc.info["name"] == self.get_exe():
                proc.kill()
                proc.wait()  # Wait for the process to fully terminate
                break
        # print('close(): game force closed')

    def run(self, mode, wait_on_close=False):
        """Start game"""
        assert mode in ["user", "dev"], "Invalid mode parameter"

        # activate selected mode
        self.activate_mode(mode)

        # run game
        if self.is_running():
            self.set_hwnd()
            return

        # write config
        self._write_config()

        # build game argument params
        game_args = " -novid"  # skip intro videos
        game_args += " -console"  # enable developer console

        # run game
        if wait_on_close:
            # Run without waiting (opening through steam means code would not connect to left4dead2.exe)
            exe_path = os.path.join(self.get_dir("dev"), self.game_exe)
            subprocess.run('"' + exe_path + '"' + game_args, shell=True, check=False)
        else:
            # run the game through steam to prevent steam issues
            steam_args = f" -applaunch {str(self.get_appid())}"
            steam_exe = self.steam_info.get("steam_exe")
            subprocess.Popen('"' + steam_exe + '"' + steam_args + game_args, shell=True)

        # wait until game is running
        wait_for_process(self.get_exe())

        # set hwnd
        self.set_hwnd()


def debug_game_class():
    """Debug the class"""
    os.system("cls")  # clear terminal

    saved_data = load_data()
    game_debug_instance = Game(saved_data)
    game_debug_instance = Game(saved_data)
    result = game_debug_instance.get_title()
    print(result)

    input("end of class_game autoexecute")

    # game_instance = Game(PERSISTENT_DATA)
    # game_manager_instance = GameManager(PERSISTENT_DATA, game_instance)

    # debug_hud_syncer()
    # debug_hud_select_gui(PERSISTENT_DATA, game_manager_instance)
    # game_manager_instance.run_update_or_repair()
    # game_manager_instance.run_update_or_repair("repair")

    # hud_edit.finish_editing()
    # game_instance.run("dev")
    # game_instance.command.execute("map c12m2_traintunnel")
    # game_instance.command.execute("give_all_items")
    # game_instance.command.execute("echo this is a test 5!")
    # game_instance.command.execute("hud_reloadscheme")
    # game_instance.command.execute("")

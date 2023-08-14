import os
import subprocess

from utils.functions import is_valid_window, wait_for_process_and_get_hwnd


class GameV2Window:
    def __init__(self, game_class):
        self.game = game_class
        self.persistent_data = self.game.persistent_data

        self.hwnd = None
        self.exe = "left4dead2.exe"

    def get_exe(self):
        """Retrieve information"""
        return self.exe

    def get_hwnd(self):
        """Retrieve information"""

        if self.hwnd is None or not is_valid_window(self.hwnd):
            self.set_hwnd()

        if not self.hwnd:
            print("No window handle to get!")
        else:
            print(f"Get {self.get_exe()} hwnd '{self.hwnd}'")
            return self.hwnd

    def set_hwnd(self, timeout_seconds=0):
        """Retrieve game hwnd"""
        # wait until game is running

        self.hwnd = wait_for_process_and_get_hwnd(self.get_exe(), timeout_seconds)
        if not self.hwnd:
            print("No window handle to set!")
        else:
            print(f"Set {self.get_exe()} hwnd '{self.hwnd}'")

    def run(self, dir_mode, wait_on_close=False):
        """Start game"""

        self.game.validate_dir_mode(dir_mode)

        print(f"directory mode: {dir_mode.name}")

        # activate selected dir_mode
        # result = self.activate_mode(dir_mode) # TODO activate_mode
        # if not result:
        #     return False

        # run game
        # if self.is_running(): # TODO is_running
        #     self.set_hwnd()
        #     self.move(self.persistent_data["game_pos"])
        #     return

        # write config
        # self._write_config() # TODO _write_config

        # build game argument params
        game_args = " -novid"  # skip intro videos
        game_args += " -console"  # enable developer console

        # # run game
        # if wait_on_close:
        #     # Run without waiting (opening through steam means code would not connect to left4dead2.exe)
        #     exe_path = os.path.join(self.get_dir("dev"), self.game_exe) # TODO get_dir
        #     subprocess.run('"' + exe_path + '"' + game_args, shell=True, check=False)
        # else:
        #     # run the game through steam to prevent steam issues
        #     steam_args = f" -applaunch {str(self.get_appid())}"
        #     steam_exe = self.steam_info.get("steam_exe") # TODO steam_info.get("steam_exe")
        #     subprocess.Popen('"' + steam_exe + '"' + steam_args + game_args, shell=True)

        # set hwnd
        self.set_hwnd()

        # set position
        # self.move(self.persistent_data["game_pos"]) # TODO move(self.persistent_data["game_pos"])

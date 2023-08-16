# pylint: disable=broad-exception-caught
"Game class window methods"
# pylint: disable=protected-access, broad-exception-raised
import subprocess

import win32gui

from utils.constants import GAME_POSITIONS
from utils.functions import (
    get_hwnd_for_exe,
    is_process_running,
    is_valid_window,
    move_hwnd_to_position,
    wait_for_process,
)


class GameV2Window:
    "Game class window methods"

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
            self.__set_hwnd()

        if not self.hwnd:
            print("No window handle to get!")
        else:
            print(f"Get {self.get_exe()} hwnd '{self.hwnd}'")
            return self.hwnd

    def __restore_saved_position(self):
        self.set_position(self.persistent_data["game_pos"])

    def set_position(self, position):
        # pylint: disable=c-extension-no-member
        """Move window to position"""
        if position not in GAME_POSITIONS:
            raise Exception("Invalid position")

        # save position
        self.persistent_data["game_pos"] = position

        if "custom" in position.lower():
            self.persistent_data["game_pos_custom_coord"] = position
            window_pos = self.persistent_data.get("game_pos_custom_coord")  # using get method to avoid KeyError

            if (
                isinstance(window_pos, tuple)
                and len(window_pos) == 2
                and all(isinstance(i, int) and i >= 0 for i in window_pos)
            ):
                win32gui.SetWindowPos(self.get_hwnd(), 0, *window_pos, 0, 0, 0)
        else:
            move_hwnd_to_position(self.get_hwnd(), position)

    def __set_hwnd(self, timeout_seconds=0):
        """Retrieve game hwnd"""

        # exception because we need the window handle
        try:
            # wait until game is running
            wait_for_process(self.get_exe(), timeout_seconds)

            # retrieve hwnd
            self.hwnd = get_hwnd_for_exe(self.get_exe())
            if not self.hwnd:
                raise Exception("Could not set window handle!")
            else:
                print(f"Set {self.get_exe()} hwnd '{self.hwnd}'")
                return self.hwnd
        except Exception as err_info:
            print(f"An error occurred retrieving window handle: {err_info}")
            return False

    def run(self, dir_mode):
        """Start game"""

        self.game._validate_dir_mode(dir_mode)

        print(f"directory mode: {dir_mode.name}")

        # activate selected dir_mode
        result = self.game.dir.set(dir_mode)
        if not result:
            return False

        # run game
        if self.is_running():
            self.__set_hwnd()
            self.__restore_saved_position()
            return True

        # setup
        self.game._disable_addons()
        self.game._write_config()

        # build game argument params
        game_args = ["-novid", "-console"]  # novid=Skip intro videos  # consoleEnable developer console

        # run the game through steam to prevent steam issues
        steam_args = f"-applaunch {str(self.game.get_app_id())}"
        steam_exe = self.game.steam.get_exe_path()
        steam_command = f'"{steam_exe}" {steam_args} {" ".join(game_args)}'
        subprocess.Popen(steam_command, shell=False)

        # set hwnd
        self.__set_hwnd(20)

        # set position
        self.__restore_saved_position()

        return True

    def is_running(self):
        """Checks if the game is running"""
        return is_process_running(self.get_exe())

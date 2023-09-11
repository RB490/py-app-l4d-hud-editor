# pylint: disable=broad-exception-caught, c-extension-no-member
"Game class window methods"
# pylint: disable=protected-access, broad-exception-raised
import subprocess

import win32gui
from loguru import logger
from shared_utils.functions import show_message
from shared_utils.hwnd_window_manager import HwndWindowUtils

from game.constants import InstallationState
from utils.constants import GAME_POSITIONS
from utils.persistent_data_manager import PersistentDataManager


class GameWindow:
    "Game class window methods"

    def __init__(self, game_class):
        self.game = game_class
        self.data_manager = PersistentDataManager()
        self.hwnd_utils = HwndWindowUtils()

        self.hwnd = None
        self.exe = "left4dead2.exe"

    def get_exe(self):
        """Retrieve information"""
        return self.exe

    def get_hwnd(self):
        """Retrieve information"""

        if self.hwnd is None or not self.hwnd_utils.is_running(self.hwnd):
            if not self.__set_hwnd():
                return None

        return self.hwnd

    def __set_hwnd(self, input_hwnd=None):
        """Retrieve game hwnd"""

        if input_hwnd:
            # set specified hwnd from running game
            self.hwnd = input_hwnd
        else:
            # retrieve hwnd from process name
            self.hwnd = self.hwnd_utils.get_hwnd_from_process_name(self.get_exe())

        logger.debug(f"Set hwnd to '{self.hwnd}'")
        return self.hwnd

    def restore_saved_position(self):
        "Restore saved position"
        self.set_position(self.data_manager.get("game_pos"))

    def save_position(self):
        "Save custom position"
        # pylint: disable=unused-variable
        # Save custom location
        game_hwnd = self.game.window.get_hwnd()
        if game_hwnd:
            left, top, right, bottom = win32gui.GetWindowRect(game_hwnd)
            x_coordinate = left
            y_coordinate = top
            custom_position_tuple = (x_coordinate, y_coordinate)

            # Store the custom coordinate tuple in the persistent data dictionary
            self.data_manager.set("game_pos", "Custom (Save)")
            self.data_manager.set("game_pos_custom_coord", custom_position_tuple)

            logger.debug("Stored Custom Position Tuple:", custom_position_tuple)
            return custom_position_tuple
        else:
            return None

    def set_position(self, position):
        """Move window to position"""
        # pylint: disable=c-extension-no-member
        if position not in GAME_POSITIONS:
            raise Exception("Invalid position")

        # save position
        self.data_manager.set("game_pos", position)

        if "custom" in position.lower():
            # restore
            custom_position_tuple = self.data_manager.get("game_pos_custom_coord")
            custom_position_tuple = tuple(custom_position_tuple)  # load it back into a tuple to work with the coords
            if (  # verify tuple legitimacy
                isinstance(custom_position_tuple, tuple)
                and len(custom_position_tuple) == 2
                and all(isinstance(i, int) and i >= 0 for i in custom_position_tuple)
            ):
                position = custom_position_tuple
            else:
                raise ValueError(f"Invalid custom_position_tuple: {custom_position_tuple}")

        # move game
        self.hwnd_utils.move(self.game.window.get_hwnd(), position)

    def apply_always_on_top_setting(self):
        """Enable or disable always on top"""
        if self.data_manager.get("game_always_on_top") is True:
            self.hwnd_utils.set_always_on_top(self.game.window.get_hwnd(), True)
        else:
            self.hwnd_utils.set_always_on_top(self.game.window.get_hwnd(), False)

    def run(self, dir_mode, write_config=True):
        """Start the game
        'write_config' param is used by installation when rebuilding audio so valve.rc doesnt get overwritten"""

        self.game._validate_dir_mode(dir_mode)

        print(f"directory mode: {dir_mode.name}")

        # confirm dir mode isn't being deleted
        if self.game.dir.id.get_installation_state(dir_mode) == InstallationState.PENDING_DELETION:
            show_message(f"{dir_mode} is partially deleted!\n\nRe-install before running", "error")
            return False

        # activate selected dir_mode
        result = self.game.dir.set(dir_mode)
        if not result:
            return False

        # run game
        if self.is_running():
            self.__set_hwnd()
            self.apply_always_on_top_setting()
            self.restore_saved_position()
            return True

        # disable any enabled pak01s
        self.game.dir.disable_any_enabled_pak01s()

        # setup
        self.game._disable_addons()
        if write_config:
            self.game.write_config()

        # build game argument params
        game_args = ["-novid", "-console"]  # novid=Skip intro videos  # consoleEnable developer console

        # run the game through steam to prevent steam issues
        steam_args = f"-applaunch {str(self.game.get_app_id())}"
        steam_exe = self.game.steam.get_exe_path()
        steam_command = f'"{steam_exe}" {steam_args} {" ".join(game_args)}'

        result = subprocess.Popen(
            steam_command,
            shell=True,
            creationflags=subprocess.DETACHED_PROCESS,
            start_new_session=True,  # Required for some platforms
        )
        if not result:
            raise ValueError("Unable to run game!")

        # wait for game to fully open
        hwnd = self.hwnd_utils.get_hwnd_from_process_name_with_timeout_and_optionally_ram_usage(
            self.get_exe(), 100, 80
        )  # account for steam starting up

        # set hwnd
        if hwnd:
            self.__set_hwnd(hwnd)
            self.restore_saved_position()
            return True
        else:
            return False

    def is_running(self):
        """Checks if the game is running"""
        return self.hwnd_utils.is_running(self.get_hwnd())

    def close(self):
        "Close"
        self.hwnd_utils.close(self.get_hwnd())

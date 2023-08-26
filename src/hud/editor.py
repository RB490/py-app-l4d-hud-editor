"""Class to manage hud editing"""
# pylint: disable=broad-exception-raised, broad-exception-caught, import-outside-toplevel
import os
import threading
from tkinter import filedialog
from tkinter.filedialog import asksaveasfilename

import keyboard

from game.constants import DirectoryMode
from game.game import Game
from gui.browser import GuiHudBrowser, show_browser_gui
from gui.start import show_start_gui
from hud.descriptions import HudDescriptions
from hud.syncer import HudSyncer
from shared_utils.shared_utils import show_message
from utils.constants import DEBUG_MODE, HOTKEY_SYNC_HUD
from utils.functions import copy_directory
from utils.persistent_data_manager import PersistentDataManager
from utils.vpk import VPKClass


class HudEditor:
    """Class to manage hud editing"""

    def __init__(self) -> None:
        self.data_manager = PersistentDataManager()
        self.game = Game()
        self.syncer = HudSyncer()
        self.desc = HudDescriptions()
        self.hud_dir = None
        self.threaded_timer_game_exit = None
        self.browser = None

    def start_editing(self, hud_dir):
        """Perform all the actions needed to start hud editing"""

        print(f"Start editing: ({hud_dir})")

        # verify parameters
        result = self.set_dir(hud_dir)
        if not result:
            raise NotADirectoryError(f"The directory {hud_dir} is not valid.")

        # prompt to start game during debug mode
        if DEBUG_MODE:
            result = show_message("Start editing HUD ingame?", msgbox_type="yesno", title="Start editing HUD?")
            if not result:
                show_start_gui()
                return False

        # is developer mode installed? - also checks for user directory
        if not self.game.installation_completed(DirectoryMode.DEVELOPER):
            show_message("Development mode not fully installed!", "error")
            return False

        # cancel if this hud is already being edited
        if self.syncer.is_synced() and (self.syncer.get_source_dir() == self.get_dir()):
            return False

        # unsync previous hud
        self.syncer.unsync()

        # Stop checking for game exit
        self.stop_game_exit_check()

        # enable dev mode
        result = self.game.dir.set(DirectoryMode.DEVELOPER)
        if not result:
            print("Could not activate developer mode")
            show_start_gui()
            return False

        # sync the hud to the game folder
        self.syncer.sync(
            self.get_dir(),
            self.game.dir.get(DirectoryMode.DEVELOPER),
            os.path.basename(self.game.dir.get_main_dir(DirectoryMode.DEVELOPER)),
        )

        # hotkeys
        keyboard.add_hotkey(HOTKEY_SYNC_HUD, self.sync, suppress=True)

        # run the game
        self.game.window.run(DirectoryMode.DEVELOPER)

        # refresh hud incase game has not restarted
        self.game.command.execute("reload_all")

        # Start checking for game exit
        self.wait_for_game_exit_then_finish_editing()

        # Open browser
        self.browser = show_browser_gui()

        return True

    def finish_editing(self, open_start_gui=True):
        """Perform all the actions needed to finish hud editing"""
        print("finish_editing")

        # Stop checking for game exit
        self.stop_game_exit_check()

        # close browser
        if isinstance(self.browser, GuiHudBrowser):
            self.browser.hide()

        # unsync hud
        self.syncer.unsync()

        # remove hotkey
        hotkeys = keyboard.get_hotkey_name()
        if HOTKEY_SYNC_HUD in hotkeys:
            print("Hotkey exists")
            keyboard.remove_hotkey(self.sync)

        # clear variables
        self.set_dir(None)

        # enable user mode
        self.game.dir.set(DirectoryMode.DEVELOPER)

        # callback to the gui
        if open_start_gui:
            show_start_gui()

    def sync(self):
        """Sync hud"""

        hud_dir = self.get_dir()
        dev_game_dir = self.game.dir.get(DirectoryMode.DEVELOPER)
        main_dev_dir_basename = os.path.basename(self.game.dirget_main_dir(DirectoryMode.DEVELOPER))

        print("hud_dir:", hud_dir)
        print("dev_game_dir:", dev_game_dir)
        print("main_dev_dir_basename:", main_dev_dir_basename)

        # pylint: disable=broad-exception-caught
        try:
            self.syncer.sync(hud_dir, dev_game_dir, main_dev_dir_basename)
        except Exception as err_info:
            print(f"Could not sync: {err_info}")

    def unsync(self):
        """Unsync hud"""

        self.syncer.unsync()

        # clear variables
        self.set_dir(None)

    def synced(self):
        "Verify if hud is loaded"
        return self.syncer.is_synced()

    def is_loaded(self):
        "Verify if hud is loaded"
        if self.get_dir():
            return True
        else:
            return False

    def set_dir(self, directory):
        """Get information"""
        if not os.path.isdir(directory):
            print(f"Could not set HUD directory to edit because it does not exist: {directory}")
            return False

        self.hud_dir = directory
        return True

    def get_dir(self):
        """Get information"""
        return self.hud_dir

    def get_all_files_dict(self):
        """Retrieve key:value dict for all possible hud files"""
        return self.desc.get_all_descriptions()

    def get_files_dict(self):
        """Retrieve key:value dict for the hud files"""
        # pylint: disable=unused-variable

        # verify variables
        if not self.get_dir() or not os.path.exists(self.get_dir()):
            print(f"Could not retrieve files dictionary. Directory does not exist: {self.get_dir()}")
            return None

        root_folder = self.get_dir()
        files_dict = {}
        for dirpath, dirnames, filenames in os.walk(root_folder):
            for filename in filenames:
                full_path = os.path.join(dirpath, filename)
                relative_path = os.path.relpath(full_path, root_folder)
                file_desc = self.desc.get_file_description(relative_path)
                files_dict[filename] = (file_desc, relative_path)
        return files_dict

    def save_as_folder(self):
        """Save hud as folder"""

        source_dir = self.get_dir()

        # Validate source directory
        if not os.path.isdir(source_dir):
            raise NotADirectoryError(f"The source directory {source_dir} is not valid.")

        # Ask the user to select the target directory
        target_dir = filedialog.askdirectory(title="Select Target Directory")
        if not target_dir:
            return

        # Validate target directory
        if not os.path.isdir(target_dir):
            raise NotADirectoryError(f"The target directory {target_dir} is not valid.")

        # Check if target directory already exists and has any contents
        if os.path.exists(target_dir) and os.path.isdir(target_dir) and os.listdir(target_dir):
            # Prompt user whether to overwrite the target directory or not
            response = show_message(
                f"The directory {target_dir} already exists and is not empty. Do you want to overwrite it?",
                "yesno",
                "Confirmation",
            )
            if not response:
                return

        # pylint: disable=broad-exception-caught
        try:
            # Copy the contents of source_dir to target_dir
            copy_directory(source_dir, target_dir)
        except Exception as general_error:
            print(f"An error occurred: {general_error}")

    def save_vpk_file(self):
        """Save hud as vpk file"""

        # verify directory
        if not os.path.isdir(self.get_dir()):
            raise AssertionError("Directory does not exist.")

        # Prompt the user to select a file location to save the VPK file
        file_path = asksaveasfilename(
            defaultextension=".vpk", filetypes=[("Valve Package Files", "*.vpk"), ("All Files", "*.*")]
        )

        if file_path:
            # Perform the VPK file saving logic here
            # You can use the chosen file_path variable to save the file

            vpk_file_class = VPKClass()
            vpk_file_class.create(self.get_dir(), os.path.dirname(file_path), os.path.basename(file_path))

            print(f"VPK file saved at: {file_path}")
        else:
            print("Saving canceled.")

    def wait_for_game_exit_then_finish_editing(self):
        """Used to finish editing when game closes"""

        if not self.game.window.is_running():
            self.finish_editing(open_start_gui=True)
        else:
            # Schedule the function to be called again
            self.start_game_exit_check()

    def start_game_exit_check(self):
        """Start game exit check"""
        # Stop any currently running thread
        if self.threaded_timer_game_exit is not None:
            self.stop_game_exit_check()

        # Schedule the function to be called after 2 seconds
        self.threaded_timer_game_exit = threading.Timer(2, self.wait_for_game_exit_then_finish_editing)
        self.threaded_timer_game_exit.start()

    def stop_game_exit_check(self):
        """Stop game exit check"""
        if self.threaded_timer_game_exit is not None:
            self.threaded_timer_game_exit.cancel()
            self.threaded_timer_game_exit = None

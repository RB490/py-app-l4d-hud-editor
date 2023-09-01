"""Class to manage hud editing"""
# pylint: disable=broad-exception-raised, broad-exception-caught, import-outside-toplevel, invalid-name
import os
import threading
from tkinter import filedialog
from tkinter.filedialog import asksaveasfilename

from game.constants import DirectoryMode
from game.game import Game
from gui.browser import GuiHudBrowser
from hud.descriptions import HudDescriptions
from hud.manager import HudManager
from hud.syncer import HudSyncer
from shared_utils.hotkey_manager import HotkeyManager
from shared_utils.shared_utils import copy_directory, show_message
from utils.constants import DEBUG_MODE, HOTKEY_SYNC_HUD
from utils.functions import get_browser_gui, show_start_gui
from utils.persistent_data_manager import PersistentDataManager
from utils.vpk import VPKClass


class HudEditor:
    """Class to manage hud editing"""

    def __init__(self) -> None:
        self.data_manager = PersistentDataManager()
        self.game = Game()
        self.syncer = HudSyncer()
        self.desc = HudDescriptions()
        self.manager = HudManager()
        self.hotkey_manager = HotkeyManager()
        self.hud_dir = None
        self.hud_name = None
        self.threaded_timer_game_exit = None
        self.browser = None

    def _is_already_being_edited(self):
        """Check if the current HUD is already being edited."""

        if self.syncer.is_synced() and self.syncer.get_source_dir() == self.get_dir():
            return True
        return False

    def start_editing(self, hud_dir):
        """Perform all the actions needed to start hud editing"""

        print(f"Start editing: ({hud_dir})")

        # verify parameters
        result = self._set_hud_info(hud_dir)
        if not result:
            raise NotADirectoryError(f"The directory {hud_dir} is not valid.")

        # verify ID files (here in addition to on start because it might break after program starts)
        try:
            self.game.dir.check_for_invalid_id_file_structure()
        except Exception as e_info:
            show_message(f"Invalid ID file structure! Can't start HUD editing! {e_info}", "error")
            show_start_gui()
            return False

        # prompt to start game during debug mode
        if DEBUG_MODE and not self.game.window.is_running():
            result = show_message(
                f"Start editing {self.get_name()} ingame?",
                msgbox_type="yesno",
                title="Start editing HUD?",
            )
            if not result:
                show_start_gui()
                return False

        # is developer mode installed? - also checks for user directory
        if not self.game.installation_completed(DirectoryMode.DEVELOPER):
            show_message("Development mode not fully installed!", "error")
            show_start_gui()
            return False

        # cancel if this hud is already being edited
        if self._is_already_being_edited():
            show_start_gui()
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
        self.hotkey_manager.add_hotkey(HOTKEY_SYNC_HUD, self.sync_in_thread, suppress=True)

        # run the game
        try:
            self.game.window.run(DirectoryMode.DEVELOPER)
        except Exception as e:
            self.unsync()
            show_message(f"failed to run game: {e}")
            show_start_gui()
            return False

        # refresh hud incase game has not restarted
        self.game.command.execute("reload_all")

        # Start checking for game exit
        self.wait_for_game_exit_then_finish_editing()

        # Open browser
        self.browser = get_browser_gui()

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
        self.hotkey_manager.remove_hotkey(HOTKEY_SYNC_HUD)

        # clear variables
        self.clear_hud_info()

        # enable user mode
        self.game.dir.set(DirectoryMode.DEVELOPER)

        # callback to the gui
        if open_start_gui:
            show_start_gui()

    def sync_in_thread(self):
        """Assign this to a hotkey to prevent sync() taking too long and the hotkey not being suppressed"""
        thread = threading.Thread(target=self.sync)
        thread.start()

    def sync(self):
        """Sync hud"""

        hud_dir = self.get_dir()
        dev_game_dir = self.game.dir.get(DirectoryMode.DEVELOPER)
        main_dev_dir_basename = os.path.basename(self.game.dir.get_main_dir(DirectoryMode.DEVELOPER))

        # print("hud_dir:", hud_dir)
        # print("dev_game_dir:", dev_game_dir)
        # print("main_dev_dir_basename:", main_dev_dir_basename)

        try:
            self.syncer.sync(hud_dir, dev_game_dir, main_dev_dir_basename)

            self.game.command.execute(self.data_manager.get("hud_reload_mode"))
        except Exception as err_info:
            print(f"Could not sync: {err_info}")

    def unsync(self):
        """Unsync hud"""

        self.syncer.unsync()

        # clear variables
        self._set_hud_info(None)

    def synced(self):
        "Verify if hud is loaded"
        return self.syncer.is_synced()

    def is_synced(self):
        "Verify if hud is loaded"
        if self.get_dir():
            return True
        else:
            return False

    def _set_hud_info(self, directory):
        """Get information"""
        self.hud_dir = directory
        result = self.hud_name = self.manager.retrieve_hud_name_for_dir(directory)
        if result:
            return True
        else:
            return False

    def clear_hud_info(self):
        """Get information"""
        self.hud_dir = None
        self.hud_name = None
        return True

    def get_name(self):
        """Get information"""
        return self.hud_name

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
            print(f"Can't retrieve files dictionary. Directory does not exist: {self.get_dir()}")
            return None

        root_folder = self.get_dir()
        files_dict = {}
        for dirpath, dirnames, filenames in os.walk(root_folder):
            for filename in filenames:
                full_path = os.path.join(dirpath, filename)
                relative_path = os.path.relpath(full_path, root_folder)
                file_desc = self.desc.get_file_description(filename)
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

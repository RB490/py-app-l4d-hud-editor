"""Methods related to editing a hud"""
import os
import threading
from tkinter import filedialog
from tkinter.filedialog import asksaveasfilename
import keyboard
from packages.classes.vpk import VPKClass
from packages.gui.start import GuiHudStart
from packages.hud.descriptions import HudDescriptions
from packages.hud.syncer import HudSyncer

# pylint: disable=unused-import
from packages.gui.browser import GuiHudBrowser
from packages.game.game import Game
from packages.utils.functions import copy_files_in_directory, load_data
from packages.utils.constants import DEBUG_MODE, DEVELOPMENT_DIR, HOTKEY_SYNC_HUD, NEW_HUD_DIR
from packages.utils.shared_utils import show_message


class Hud:
    """Class to manage hud editing"""

    _instance = None

    def __new__(cls, persistent_data):
        if cls._instance is None:
            cls._instance = super(Hud, cls).__new__(cls)
            cls._instance.data = None
            cls.persistent_data = persistent_data

        return cls._instance

    def __init__(self, persistent_data) -> None:
        self.game = Game(persistent_data)
        self.persistent_data = persistent_data
        self.syncer = HudSyncer()
        self.desc = HudDescriptions()
        self.hud_dir = None
        self.threaded_timer_game_exit = None
        self.browser = None

        if DEBUG_MODE:
            self.hud_dir = os.path.join(DEVELOPMENT_DIR, "debug", "hud_debug", "Workspace", "2020HUD")

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
            # if hasattr(self, "hud_dir") and not os.path.exists(self.get_dir()):
            return

        root_folder = self.get_dir()
        files_dict = {}
        for dirpath, dirnames, filenames in os.walk(root_folder):
            for filename in filenames:
                full_path = os.path.join(dirpath, filename)
                relative_path = os.path.relpath(full_path, root_folder)
                file_desc = self.desc.get_description(relative_path)
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
            copy_files_in_directory(source_dir, target_dir)
        except Exception as general_error:
            print(f"An error occurred: {general_error}")

    def save_vpk_file(self):
        """Save hud as vpk file"""

        # verify directory
        assert os.path.isdir(self.get_dir())

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

    def wait_for_game_exit_then_finish_editing(self):
        """Used to finish editing when game closes"""

        if not self.game.is_running():
            self.finish_editing(open_start_gui=True)
        else:
            # Schedule the function to be called again
            self.start_game_exit_check()

    def start_editing(self, hud_dir, sync_hud=True):
        """Perform all the actions needed to start hud editing"""

        print(f"start_editing: ({hud_dir})")

        # verify parameters
        if not os.path.isdir(hud_dir):
            raise NotADirectoryError(f"The directory {hud_dir} is not valid.")
        self.hud_dir = hud_dir

        # debug mode - prompt to start game
        if DEBUG_MODE:
            result = show_message("Start editing HUD ingame?", msgbox_type="yesno", title="Start editing HUD?")
            if not result:
                return

        # cancel if this hud is already being edited
        if self.syncer.get_sync_status() and self.syncer.get_source_dir() == self.hud_dir and sync_hud:
            return

        # unsync previous hud
        if sync_hud:
            self.syncer.un_sync()

        # Stop checking for game exit
        self.stop_game_exit_check()

        # enable dev mode
        result = self.game.activate_mode("dev")
        if not result:
            print('Could not activate developer mode')
            return

        # sync the hud to the game folder
        if sync_hud:
            self.syncer.sync(self.hud_dir, self.game.get_dir("dev"), os.path.basename(self.game.get_main_dir("dev")))

        # hotkeys
        keyboard.add_hotkey(HOTKEY_SYNC_HUD, self.sync, suppress=True)

        # run the game
        self.game.run("dev")

        # refresh hud incase game has not restarted
        self.game.command.execute("reload_all")

        # Start checking for game exit
        self.wait_for_game_exit_then_finish_editing()

        # Open browser
        if isinstance(self.browser, GuiHudBrowser):
            self.browser.destroy_gui()
        self.browser = GuiHudBrowser(self.persistent_data)
        self.browser.run()

    def sync(self):
        """Sync hud"""

        hud_dir = self.hud_dir
        dev_game_dir = self.game.get_dir("dev")
        main_dev_dir_basename = os.path.basename(self.game.get_main_dir("dev"))

        print("hud_dir:", hud_dir)
        print("dev_game_dir:", dev_game_dir)
        print("main_dev_dir_basename:", main_dev_dir_basename)

        # pylint: disable=broad-exception-caught
        try:
            self.syncer.sync(hud_dir, dev_game_dir, main_dev_dir_basename)
        except Exception as err_info:
            print(f"Could not sync: {err_info}")

    def un_sync(self):
        """Unsync hud"""

        self.syncer.un_sync()

        # clear variables
        self.hud_dir = None

    def finish_editing(self, open_start_gui=True):
        """Perform all the actions needed to finish hud editing"""
        print("finish_editing")

        # Stop checking for game exit
        self.stop_game_exit_check()

        # close browser
        if isinstance(self.browser, GuiHudBrowser):
            self.browser.destroy_gui()

        # unsync hud
        self.syncer.un_sync()

        # remove hotkey
        hotkeys = keyboard.get_hotkey_name()
        if HOTKEY_SYNC_HUD in hotkeys:
            print("Hotkey exists")
            keyboard.remove_hotkey(self.sync)

        # clear variables
        self.hud_dir = None

        # enable user mode
        self.game.activate_mode("user")

        # callback to the gui
        if open_start_gui:
            start_instance = GuiHudStart(self.persistent_data)
            start_instance.run()


def debug_hud():
    # pylint: disable=unused-variable
    """Debug the hud class"""
    print("debug_hud")

    persistent_data = load_data()
    my_hud_instanc = Hud(persistent_data)
    # my_hud_instanc.save_as_folder()
    my_hud_instanc.start_editing(my_hud_instanc.get_dir())

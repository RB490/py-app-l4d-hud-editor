"""Methods related to editing a hud"""
import os
import threading
from tkinter.filedialog import asksaveasfilename
import easygui
from packages.classes.vpk import VPKClass
from packages.gui.descriptions import GuiHudDescriptions
from packages.hud.descriptions import HudDescriptions
from packages.hud.syncer import HudSyncer

# pylint: disable=unused-import
from packages.gui.browser import GuiHudBrowser
from packages.game import Game
from packages.utils.functions import copy_directory_contents, load_data
from packages.utils.constants import DEBUG_MODE, DEVELOPMENT_DIR, NEW_HUD_DIR


class Hud:
    """Class to manage hud editing"""

    def __init__(self, game_instance) -> None:
        assert isinstance(game_instance, Game)
        self.game = game_instance
        self.syncer = HudSyncer()
        self.desc = HudDescriptions()
        self.hud_dir = None
        self.timer_game_exit = None
        self.finish_editing_callback = None

    def set_finish_editing_callback(self, callback):
        """Callback to the hud select gui"""
        self.finish_editing_callback = callback

    def get_dir(self):
        """Get information"""
        return self.hud_dir

    def get_all_files_dict(self):
        """Retrieve key:value dict for all possible hud files"""
        return self.desc.get_all_descriptions()

    def get_files_dict(self):
        """Retrieve key:value dict for the hud files"""
        # pylint: disable=unused-variable
        root_folder = self.hud_dir
        files_dict = {}
        for dirpath, dirnames, filenames in os.walk(root_folder):
            for filename in filenames:
                full_path = os.path.join(dirpath, filename)
                relative_path = os.path.relpath(full_path, root_folder)
                file_desc = self.desc.get_description(relative_path)
                files_dict[filename] = file_desc
        return files_dict

    def save_as_folder(self):
        """Save hud as folder"""

        source_dir = self.get_dir()

        # verify directory
        assert os.path.isdir(source_dir)

        target_dir = easygui.diropenbox(
            msg="Please select the target directory", title="Select Target Directory", default=""
        )

        # Check if target directory already exists and has any files in it
        if os.path.exists(target_dir) and len(os.listdir(target_dir)) > 0:
            # Prompt user whether to overwrite the target directory or not
            response = easygui.boolbox(
                msg=f"The directory {target_dir} already exists and is not empty. Do you want to overwrite it?",
                title="Confirmation",
                choices=("Yes", "No"),
            )
            if not response:
                return

        # copy the contents of source_dir to target_dir
        copy_directory_contents(source_dir, target_dir)

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
        if self.timer_game_exit is not None:
            self.stop_game_exit_check()

        # Schedule the function to be called after 2 seconds
        self.timer_game_exit = threading.Timer(2, self.wait_for_game_exit_then_finish_editing)
        self.timer_game_exit.start()

    def stop_game_exit_check(self):
        """Stop game exit check"""
        if self.timer_game_exit is not None:
            self.timer_game_exit.cancel()
            self.timer_game_exit = None

    def wait_for_game_exit_then_finish_editing(self):
        """Used to finish editing when game closes"""

        if not self.game.is_running():
            self.finish_editing()
        else:
            # Schedule the function to be called again
            self.start_game_exit_check()

    def start_editing(self, hud_dir):
        """Perform all the actions needed to start hud editing"""

        print(f"start_editing: ({hud_dir})")

        # verify parameters
        assert os.path.isdir(hud_dir)
        self.hud_dir = hud_dir

        # debug mode - prompt to start game
        if DEBUG_MODE:
            result = easygui.ynbox("Start editing HUD ingame?", "Confirmation", ("Yes", "No"))
            if not result:
                return

        # cancel if this hud is already being edited
        if self.syncer.get_sync_status() and self.syncer.get_source_dir() == self.hud_dir:
            return

        # unsync previous hud
        self.syncer.un_sync()

        # Stop checking for game exit
        self.stop_game_exit_check()

        # enable dev mode
        self.game.activate_mode("dev")

        # sync the hud to the game folder
        self.syncer.sync(self.hud_dir, self.game.get_dir("dev"), os.path.basename(self.game.get_main_dir("dev")))

        # run the game
        self.game.run("dev")

        # refresh hud incase game has not restarted
        self.game.command.execute("reload_all")

        # Start checking for game exit
        self.wait_for_game_exit_then_finish_editing()

    def un_sync(self):
        """Unsync loaded hud"""

        self.syncer.un_sync()

        # clear variables
        self.hud_dir = None

    def finish_editing(self):
        """Perform all the actions needed to finish hud editing"""
        print("finish_editing")

        # Stop checking for game exit
        self.stop_game_exit_check()

        # unsync hud
        self.syncer.un_sync()

        # clear variables
        self.hud_dir = None

        # enable user mode
        self.game.activate_mode("user")

        # callback to the gui
        if self.finish_editing_callback:
            self.finish_editing_callback()


def debug_hud():
    # pylint: disable=unused-variable
    """Debug the hud class"""
    print("debug_hud")

    persistent_data = load_data()
    game_instance = Game(persistent_data)
    huds_debug_dir = os.path.join(DEVELOPMENT_DIR, "debug", "hud_debug")
    hud_debug_dir = os.path.join(huds_debug_dir, "Workspace", "2020HUD")
    hud_edit = Hud(game_instance)
    hud_edit.hud_dir = hud_debug_dir

    hud_desc_gui = GuiHudDescriptions(hud_edit, "scripts\\hudlayout.res")
    hud_desc_gui.root.mainloop()

    # hud_edit.start_editing(hud_debug_dir)
    # gui_browser = GuiHudBrowser(hud_edit)
    # gui_browser.root.mainloop()

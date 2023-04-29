"""Methods related to editing a hud"""
import os
import threading
import time
import psutil
import subprocess
from modules.classes.hud_descriptions import HudDescriptions
from modules.classes.hud_syncer import HudSyncer
from modules.classes.gui_hud_browser import GuiHudBrowser
from modules.classes.game import Game
from modules.utils.functions import load_data
from modules.utils.constants import DEVELOPMENT_DIR


class Hud:
    """Class for the hud select gui"""

    def __init__(self, game_instance) -> None:
        assert isinstance(game_instance, Game)
        self.game = game_instance
        self.syncer = HudSyncer()
        self.desc = HudDescriptions()
        self.hud_dir = None
        self.timer_game_exit = None

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
                file_desc = self.get_file_description(relative_path)
                files_dict[filename] = file_desc
        return files_dict

    def get_file_description(self, relative_path):
        """Get information"""
        print(f"get_file_description for: {relative_path}")
        return self.desc.get_description(relative_path)

    def wait_for_game_exit_then_finish_editing(self):
        """Used to finish editing when game closes"""

        if not self.game.is_running():
            self.finish_editing()
        else:
            # Schedule the function to be called again
            self.timer_game_exit = threading.Timer(2, self.wait_for_game_exit_then_finish_editing)
            self.timer_game_exit.start()

    def start_editing(self, hud_dir):
        """Perform all the actions needed to start hud editing"""
        print(f"start_hud_editing: todo... ({hud_dir})")

        # verify parameters
        assert os.path.isdir(hud_dir)
        self.hud_dir = hud_dir

        # cancel if this hud is already being edited
        if self.syncer.get_sync_status() and self.syncer.get_source_dir() == self.hud_dir:
            return

        # unsync previous hud
        self.syncer.un_sync()

        # Stop checking for game exit
        if self.timer_game_exit is not None:
            self.timer_game_exit.cancel()

        # enable dev mode
        self.game.activate_mode("dev")

        # sync the hud to the game folder
        # self.syncer.sync(
        #     self.hud_dir, self.game.get_dir("dev"), os.path.basename(self.game_instance.get_main_dir("dev"))
        # )

        # run the game
        self.game.run("dev")

        # refresh hud incase game has not restarted
        self.game.command.execute("reload_all")

        # Start checking for game exit
        self.wait_for_game_exit_then_finish_editing()

    def finish_editing(self):
        """Perform all the actions needed to finish hud editing"""
        print("finish_hud_editing: todo...")


def debug_hud():
    """Debug the hud class"""
    print("debug_hud")

    persistent_data = load_data()
    game_instance = Game(persistent_data)
    huds_debug_dir = os.path.join(DEVELOPMENT_DIR, "debug", "hud_debug")
    hud_debug_dir = os.path.join(huds_debug_dir, "Workspace", "2020HUD")
    hud_edit = Hud(game_instance)
    hud_edit.start_editing(hud_debug_dir)
    # gui_browser = GuiHudBrowser(hud_edit)
    # gui_browser.root.mainloop()

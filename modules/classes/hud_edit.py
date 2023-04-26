"""Methods related to editing a hud"""
import os
from modules.classes.hud_syncer import HudSyncer
from modules.classes.game import Game


class HudEdit:
    """Class for the hud select gui"""

    def __init__(self, game_instance) -> None:
        assert isinstance(game_instance, Game)
        self.game_instance = game_instance
        self.hud_syncer = HudSyncer()

    def start_editing(self, hud_dir):
        """Perform all the actions needed to start hud editing"""
        print(f"start_hud_editing: todo... ({hud_dir})")

        # verify parameters
        assert os.path.isdir(hud_dir)

        # cancel if this hud is already being edited
        if self.hud_syncer.get_sync_status() and self.hud_syncer.get_source_dir() == hud_dir:
            return

        # unsync previous hud
        self.hud_syncer.un_sync()

        # enable dev mode
        self.game_instance.activate_mode("dev")

        # sync the hud to the game folder
        self.hud_syncer.sync(
            hud_dir, self.game_instance.get_dir("dev"), os.path.basename(self.game_instance.get_main_dir("dev"))
        )

        # run the game
        self.game_instance.run("dev")

        # refresh hud incase game has not restarted

    def finish_editing(self):
        """Perform all the actions needed to finish hud editing"""
        print("finish_hud_editing: todo...")

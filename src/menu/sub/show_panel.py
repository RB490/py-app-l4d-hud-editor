# pylint: disable=attribute-defined-outside-init

import tkinter as tk

from shared_gui.menu_debug import menu_debug_gui
from shared_utils.functions import create_lambda_command

from src.menu.base import EditorMenuBase
from src.utils.constants import GAME_POSITIONS


class MenuShowPanel(EditorMenuBase):
    """Menu"""

    def __init__(self, editor_menu_instance):
        super().__init__(editor_menu_instance)

    def get(self, menubar):
        """get menu"""

        show_panel_dict = {
            "general": {
                "None": "None",
                "Sacrifice Failed": "info_window",
                "Tab Scoreboard": "scores",
                "Spectating Hud": "Specgui",
                "Versus spawn tutorial": "spawnmode",
                "MOTD": "info",
                "Team Switching Panel": "team",
                "Transition Screen": "transition_stats",
                "Versus Shut Down": "vs_shutting_down",
                "Versus TooFar": "debug_zombie_panel -1",
                "Versus BecomeTank": "debug_zombie_panel 1",
                "Versus OtherBecomeTank": "debug_zombie_panel 2",
                "Hide versus TooFar/Tank panel": "debug_zombie_panel 0",
            },
            "L4D1": {
                "Versus smoker tutorial": "spawn_smoker",
                "Versus hunter tutorial": "spawn_hunter",
                "Versus boomer tutorial": "spawn_boomer",
                "Survival Scoreboard End Of Round": "fullscreen_holdout_scoreboard",
                "Survival Shutting Down": "holdout_shutting_down",
                "Versus Scoreboard End Of Round": "multimap_vs_scoreboard",
            },
            "L4D2": {
                "Versus/Scavenge Rematch Hud": "fullscreen_scavenge_scoreboard",
                "Versus Scoreboard End of Match": "fullscreen_vs_results",
                "Versus Scoreboard End of Round": "fullscreen_vs_scoreboard",
                "Versus/Scavenge round start timer": "ready_countdown",
                "Survival Scoreboard": "fullscreen_survival_scoreboard",
                "Survival Shut Down": "survival_shutting_down",
            },
        }

        # Create general menu and add common options
        self.show_panel_menu_selected_var = tk.BooleanVar()
        self.show_panel_menu = tk.Menu(menubar, tearoff=True)
        for key, value in show_panel_dict["general"].items():
            command = create_lambda_command(self.handler.editor_menu_show_panel, value)

            if value == self.game.command.show_ui_panel:
                self.show_panel_menu.add_checkbutton(
                    label=key,
                    command=command,
                    variable=self.show_panel_menu_selected_var,
                    image=self.img.get("window_black_rounded_square_interface_symbol.png", 2),
                    compound="left",
                )
            else:
                self.show_panel_menu.add_command(
                    label=key,
                    command=command,
                    image=self.img.get("window_black_rounded_square_interface_symbol.png", 2),
                    compound="left",
                )

        # Check GAME_VERSION to determine which L4D-specific options to add
        if self.game.get_version() == "L4D1":
            show_panel_game_version_data = show_panel_dict.get("L4D1", {})
        elif self.game.get_version() == "L4D2":
            show_panel_game_version_data = show_panel_dict.get("L4D2", {})
        else:
            show_panel_game_version_data = {}

        # Add L4D-specific options to general menu
        for key, value in show_panel_game_version_data.items():
            command = create_lambda_command(self.handler.editor_menu_show_panel, value)
            if value == self.game.command.show_ui_panel:
                self.show_panel_menu.add_checkbutton(
                    label=key,
                    command=command,
                    variable=self.show_panel_menu_selected_var,
                    image=self.img.get("window_black_rounded_square_interface_symbol.png", 2),
                    compound="left",
                )
            else:
                self.show_panel_menu.add_command(
                    label=key,
                    command=command,
                    image=self.img.get("window_black_rounded_square_interface_symbol.png", 2),
                    compound="left",
                )

        self.show_panel_menu_selected_var.set(1)


        return self.show_panel_menu


def main():
    """debug"""
    from src.menu.main import EditorMenuClass

    gui = menu_debug_gui()
    editor_menu_instance = EditorMenuClass(gui)
    main_menu = tk.Menu(gui.root, tearoff=True)
    menu = MenuShowPanel(editor_menu_instance).get(main_menu)
    gui.debug_menu(menu)
    gui.show()


if __name__ == "__main__":
    main()



# pylint: disable=attribute-defined-outside-init

import tkinter as tk

from shared_gui.menu_debug import menu_debug_gui
from shared_utils.functions import create_lambda_command

from src.menu.base import EditorMenuBase
from src.utils.constants import GAME_POSITIONS


class MenuSwitch(EditorMenuBase):
    """Menu"""

    def __init__(self, editor_menu_instance):
        super().__init__(editor_menu_instance)

    def get(self, menubar):
        """get menu"""

        switch_team_data = {
            "Team": {"Spectate": "jointeam 1", "Survivor": "jointeam 2", "Infected": "jointeam 3"},
            "Left 4 Dead": {
                "Bill": "sb_takecontrol Bill",
                "Francis": "sb_takecontrol Francis",
                "Louis": "sb_takecontrol Louis",
                "Zoey": "sb_takecontrol Zoey",
            },
            "Left 4 Dead 2": {
                "Coach": "sb_takecontrol Coach",
                "Nick": "sb_takecontrol Nick",
                "Ellis": "sb_takecontrol Ellis",
                "Rochelle": "sb_takecontrol Rochelle",
            },
        }

        # Create Switch submenu
        self.switch_menu = tk.Menu(menubar)

        # Add divider between each section
        self.switch_menu.add_separator()

        # Add Team, Left 4 Dead, and Left 4 Dead 2 options to root menu
        for game, options in switch_team_data.items():
            self.switch_menu.add_command(label=game, state="disabled")
            self.switch_menu.add_separator()
            for character, value in options.items():
                self.switch_menu.add_cascade(
                    label=character,
                    command=create_lambda_command(self.handler.editor_menu_execute_game_command, value),
                    image=self.img.get("switch", 2),  # Set the selected image for the cascade label
                    compound="left",  # Set the image on the left side
                )

            # Add divider between each section
            self.switch_menu.add_separator()


        return self.switch_menu


def main():
    """debug"""
    from src.menu.main import EditorMenuClass

    gui = menu_debug_gui()
    editor_menu_instance = EditorMenuClass(gui)
    main_menu = tk.Menu(gui.root, tearoff=True)
    menu = MenuSwitch(editor_menu_instance).get(main_menu)
    gui.debug_menu(menu)
    gui.show()


if __name__ == "__main__":
    main()



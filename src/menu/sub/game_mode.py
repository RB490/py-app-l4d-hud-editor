# pylint: disable=attribute-defined-outside-init

import tkinter as tk

from shared_gui.menu_debug import menu_debug_gui
from shared_utils.functions import create_lambda_command

from src.menu.base import EditorMenuBase


class MenuGameMode(EditorMenuBase):
    """Menu"""

    def __init__(self, editor_menu_instance):
        super().__init__(editor_menu_instance)

    def get(self, menubar):
        """get menu"""

        game_modes = ["Coop", "Survival", "Versus", "Scavenge"]
        self.game_mode_menu = tk.Menu(menubar, tearoff=True)
        self.game_mode_vars = {}
        for game_mode in game_modes:
            self.game_mode_vars[game_mode] = tk.BooleanVar()
            self.game_mode_menu.add_checkbutton(
                label=game_mode,
                variable=self.game_mode_vars[game_mode],
                onvalue=True,
                offvalue=False,
                command=create_lambda_command(self.handler.editor_menu_game_mode, game_mode),
                image=self.img.get("switch", 2),
                compound="left",
            )
        game_mode = self.data_manager.get("game_mode")
        self.game_mode_vars[game_mode].set(True)

        return self.game_mode_menu


def main():
    """debug"""
    from src.menu.main import EditorMenuClass

    gui = menu_debug_gui()
    editor_menu_instance = EditorMenuClass(gui)
    main_menu = tk.Menu(gui.root, tearoff=True)
    menu = MenuGameMode(editor_menu_instance).get(main_menu)
    gui.debug_menu(menu)
    gui.show()


if __name__ == "__main__":
    main()

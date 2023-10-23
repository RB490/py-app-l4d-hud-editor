# pylint: disable=attribute-defined-outside-init

import tkinter as tk

from shared_gui.menu_debug import menu_debug_gui
from shared_utils.functions import create_lambda_command

from src.menu.base import EditorMenuBase
from src.utils.constants import GAME_POSITIONS


class MenuGamePos(EditorMenuBase):
    """Menu"""

    def __init__(self, editor_menu_instance):
        super().__init__(editor_menu_instance)

    def get(self, menubar):
        """get menu"""

        self.game_pos_menu = tk.Menu(menubar, tearoff=True)
        self.game_pos_vars = {}
        for pos in GAME_POSITIONS:
            self.game_pos_vars[pos] = tk.BooleanVar()
            self.game_pos_menu.add_checkbutton(
                label=pos,
                variable=self.game_pos_vars[pos],
                onvalue=True,
                offvalue=False,
                command=create_lambda_command(self.handler.editor_menu_game_pos, pos),
                image=self.img.get("two_opposite_diagonal_arrows_in_black_square.png", 2),
                compound="left",
            )
        game_pos = self.data_manager.get("game_pos")
        self.game_pos_vars[game_pos].set(True)

        return self.game_pos_menu


def main():
    """debug"""
    from src.menu.main import EditorMenuClass

    gui = menu_debug_gui()
    editor_menu_instance = EditorMenuClass(gui)
    main_menu = tk.Menu(gui.root, tearoff=True)
    menu = MenuGamePos(editor_menu_instance).get(main_menu)
    gui.debug_menu(menu)
    gui.show()


if __name__ == "__main__":
    main()

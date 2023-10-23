# pylint: disable=attribute-defined-outside-init

import tkinter as tk

from shared_gui.menu_debug import menu_debug_gui
from shared_utils.functions import create_lambda_command

from src.menu.base import EditorMenuBase


class MenuGiveItems(EditorMenuBase):
    """Menu"""

    def __init__(self, editor_menu_instance):
        super().__init__(editor_menu_instance)

    def get(self, menubar):
        """get menu"""

        give_items_dict = {
            "Everything": "give_all_items",
            "Guns": "give_all_guns",
            "Melee weapons": "give_all_melee_weapons",
            "Pickups": "give_all_pickups",
        }

        # Add a "Give Items" menu item with sub-items for each item in the dictionary
        self.give_items_menu = tk.Menu(menubar, tearoff=True)
        for label, action in give_items_dict.items():
            self.give_items_menu.add_command(
                label=label,
                command=create_lambda_command(self.handler.editor_give_items, action),
            )

        return self.give_items_menu


def main():
    """debug"""
    from src.menu.main import EditorMenuClass

    gui = menu_debug_gui()
    editor_menu_instance = EditorMenuClass(gui)
    main_menu = tk.Menu(gui.root, tearoff=True)
    menu = MenuGiveItems(editor_menu_instance).get(main_menu)
    gui.debug_menu(menu)
    gui.show()


if __name__ == "__main__":
    main()

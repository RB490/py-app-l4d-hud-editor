# pylint: disable=attribute-defined-outside-init

import os
import tkinter as tk

from shared_gui.menu_debug import menu_debug_gui
from shared_utils.functions import create_lambda_command

from src.menu.base import EditorMenuBase
from src.utils.constants import SNIPPETS_DIR


class MenuClipboard(EditorMenuBase):
    """Menu"""

    def __init__(self, editor_menu_instance):
        super().__init__(editor_menu_instance)

    def get(self, menubar):
        """get menu"""

        self.clipboard_menu = tk.Menu(menubar, tearoff=0)

        for file_name in os.listdir(SNIPPETS_DIR):
            file_path = os.path.join(SNIPPETS_DIR, file_name)
            if os.path.isfile(file_path):
                menu_name = os.path.splitext(file_name)[0]
                self.clipboard_menu.add_command(
                    label=menu_name,
                    command=create_lambda_command(self.handler.editor_menu_copy_snippet, file_path),
                    image=self.img.get("clipboard", 2),
                    compound="left",
                )

        return self.clipboard_menu


def main():
    """debug"""
    from src.menu.main import EditorMenuClass

    gui = menu_debug_gui()
    editor_menu_instance = EditorMenuClass(gui)
    main_menu = tk.Menu(gui.root, tearoff=False)
    menu = MenuClipboard(editor_menu_instance).get(main_menu)
    gui.debug_menu(menu)
    gui.show()


if __name__ == "__main__":
    main()

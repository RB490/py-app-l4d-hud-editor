# pylint: disable=attribute-defined-outside-init

import tkinter as tk

from shared_gui.menu_debug import menu_debug_gui
from shared_utils.functions import create_lambda_command

from src.game.constants import DirectoryMode
from src.menu.base import EditorMenuBase
from src.menu.sub.load_hud import MenuLoadHud
from src.utils.constants import PROJECT_ROOT


class MenuOpen(EditorMenuBase):
    """Menu"""

    def __init__(self, editor_menu_instance):
        super().__init__(editor_menu_instance)
        self.load_hud_menu = MenuLoadHud(editor_menu_instance)

    def get(self, menubar):
        """get menu"""

        self.open_menu = tk.Menu(menubar, tearoff=True)

        # self.open_menu.add_command(label="Open", state="disabled", columnbreak=True)
        # self.open_menu.add_separator()
        self.open_menu.add_cascade(
            label="Hud",
            image=self.img.get("paintbrush", 2),
            compound="left",
            menu=self.load_hud_menu,
        )
        # self.open_menu.add_separator()
        # self.open_menu.add_command(label="Directories", state="disabled")
        # self.open_menu.add_separator()
        self.open_menu.add_command(
            label="Game",
            command=create_lambda_command(self.handler.editor_open_folder, self.game.dir.get(DirectoryMode.DEVELOPER)),
            image=self.img.get("folder", 2),
            compound="left",
        )
        self.open_menu.add_command(
            label="Program",
            command=create_lambda_command(self.handler.editor_open_folder, PROJECT_ROOT),
            image=self.img.get("folder", 2),
            compound="left",
        )

        return self.open_menu


def main():
    """debug"""
    from src.menu.main import EditorMenuClass

    gui = menu_debug_gui()
    editor_menu_instance = EditorMenuClass(gui)
    main_menu = tk.Menu(gui.root, tearoff=True)
    menu = MenuOpen(editor_menu_instance).get(main_menu)
    gui.debug_menu(menu)
    gui.show()


if __name__ == "__main__":
    main()

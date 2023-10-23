# pylint: disable=attribute-defined-outside-init

import tkinter as tk

from shared_gui.menu_debug import menu_debug_gui
from shared_utils.functions import create_lambda_command

from src.menu.base import EditorMenuBase
from src.utils.constants import GAME_POSITIONS, HOTKEY_EDITOR_MENU, HOTKEY_SYNC_HUD, HOTKEY_TOGGLE_BROWSER


class MenuHotkeys(EditorMenuBase):
    """Menu"""

    def __init__(self, editor_menu_instance):
        super().__init__(editor_menu_instance)

    def get(self, menubar):
        """get menu"""

        self.hotkeys_menu = tk.Menu(menubar)
        self.hotkeys_menu.add_command(label="Global")
        self.hotkeys_menu.entryconfig("Global", state="disabled")
        self.hotkeys_menu.add_separator()
        self.hotkeys_menu.add_command(
            label="Sync Hud",
            image=self.img.get("buttons.png", 2),
            compound="left",
            accelerator=HOTKEY_SYNC_HUD,
        )
        self.hotkeys_menu.add_command(
            label="Browse Files",
            image=self.img.get("buttons.png", 2),
            compound="left",
            accelerator=HOTKEY_TOGGLE_BROWSER,
        )
        self.hotkeys_menu.add_command(
            label="Editor Menu",
            image=self.img.get("buttons.png", 2),
            compound="left",
            accelerator=HOTKEY_EDITOR_MENU,
        )
        self.hotkeys_menu.add_separator()
        self.hotkeys_menu.add_command(label="In-Game")
        self.hotkeys_menu.entryconfig("In-Game", state="disabled")
        self.hotkeys_menu.add_separator()
        self.hotkeys_menu.add_command(
            label="Load Dead Center finale",
            image=self.img.get("buttons.png", 2),
            compound="left",
            accelerator="O",
        )
        self.hotkeys_menu.add_command(
            label="Play credits (On a finale level)",
            image=self.img.get("buttons.png", 2),
            compound="left",
            accelerator="P",
        )
        self.hotkeys_menu.add_command(
            label="Noclip",
            image=self.img.get("buttons.png", 2),
            compound="left",
            accelerator="G",
        )
        self.hotkeys_menu.add_command(
            label="Pause",
            image=self.img.get("buttons.png", 2),
            compound="left",
            accelerator="F8",
        )
        self.hotkeys_menu.add_command(
            label="Admin system menu",
            image=self.img.get("buttons.png", 2),
            compound="left",
            accelerator="N",
        )
        self.hotkeys_menu.add_command(
            label="Slow-mo game speed",
            image=self.img.get("buttons.png", 2),
            compound="left",
            accelerator="F9",
        )
        self.hotkeys_menu.add_command(
            label="Default game speed",
            image=self.img.get("buttons.png", 2),
            compound="left",
            accelerator="F10",
        )
        self.hotkeys_menu.add_command(
            label="Last game cmd",
            image=self.img.get("buttons.png", 2),
            compound="left",
            accelerator="F11",
        )


        return self.hotkeys_menu


def main():
    """debug"""
    from src.menu.main import EditorMenuClass

    gui = menu_debug_gui()
    editor_menu_instance = EditorMenuClass(gui)
    main_menu = tk.Menu(gui.root, tearoff=True)
    menu = MenuHotkeys(editor_menu_instance).get(main_menu)
    gui.debug_menu(menu)
    gui.show()


if __name__ == "__main__":
    main()



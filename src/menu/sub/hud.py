# pylint: disable=attribute-defined-outside-init

import tkinter as tk

from shared_gui.menu_debug import menu_debug_gui
from shared_utils.functions import create_lambda_command

from src.menu.base import EditorMenuBase
from src.utils.constants import HOTKEY_SYNC_HUD


class MenuHud(EditorMenuBase):
    """Menu"""

    def __init__(self, editor_menu_instance):
        super().__init__(editor_menu_instance)

    def get(self, menubar):
        """get menu"""

        self.hud_menu = tk.Menu(menubar, tearoff=True)
        self.hud_menu.add_command(label="<hud_name>", state="disabled")
        if self.hud.edit.is_synced():
            self.hud_menu.entryconfigure(1, label=self.hud.manager.retrieve_hud_name_for_dir(self.hud.edit.get_dir()))
        self.hud_menu.add_separator()
        self.hud_menu.add_command(
            label=f"Sync ({HOTKEY_SYNC_HUD})",
            image=self.img.get("reload", 2),
            compound="left",
            command=self.handler.editor_sync_hud,
        )
        self.hud_menu.add_command(
            label="Unsync",
            image=self.img.get("reload", 2),
            compound="left",
            command=self.handler.editor_unsync_hud,
        )
        self.hud_menu.add_command(
            label="Close",
            image=self.img.get("close", 2),
            compound="left",
            command=self.handler.editor_stop_editing_hud,
        )
        self.hud_menu.add_separator()
        self.hud_menu.add_command(label="Save", state="disabled")
        self.hud_menu.add_separator()
        self.hud_menu.add_command(
            label="VPK",
            image=self.img.get("save", 2),
            compound="left",
            command=self.handler.editor_save_as_vpk,
        )
        self.hud_menu.add_command(
            label="Folder",
            image=self.img.get("save", 2),
            compound="left",
            command=self.handler.editor_save_as_folder,
        )
        self.hud_menu.add_command(label="Open", state="disabled", columnbreak=True)
        self.hud_menu.add_separator()
        self.hud_menu.add_command(
            label="Hud",
            command=create_lambda_command(self.handler.editor_open_folder, self.hud.edit.get_dir()),
            image=self.img.get("folder", 2),
            compound="left",
        )
        self.hud_menu.add_command(
            label="Hud (VS Code)",
            command=create_lambda_command(self.handler.editor_open_folder_in_vscode, self.hud.edit.get_dir()),
            image=self.img.get("vs_code.png", 2),
            compound="left",
        )

        # disable items when no hud is loaded
        # try:except added try except incase no hud is loaded TODO do i want to keep this
        try:
            if not self.hud.edit.is_synced():
                for i in range(self.hud_menu.index("end") + 1):
                    self.hud_menu.entryconfigure(i, state="disabled")
        except Exception:
            pass

        return self.hud_menu


def main():
    """debug"""
    from src.menu.main import EditorMenuClass

    gui = menu_debug_gui()
    editor_menu_instance = EditorMenuClass(gui)
    main_menu = tk.Menu(gui.root, tearoff=True)
    menu = MenuHud(editor_menu_instance).get(main_menu)
    gui.debug_menu(menu)
    gui.show()


if __name__ == "__main__":
    main()

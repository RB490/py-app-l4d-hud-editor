# pylint: disable=attribute-defined-outside-init

import tkinter as tk

from shared_gui.menu_debug import menu_debug_gui
from shared_utils.functions import add_empty_menu_separator

from src.game.constants import DirectoryMode
from src.menu.base import EditorMenuBase
from src.menu.sub.load_hud import MenuLoadHud


class MenuDevInstall(EditorMenuBase):
    """Menu"""

    def __init__(self, editor_menu_instance):
        super().__init__(editor_menu_instance)
        self.load_hud_menu = MenuLoadHud(editor_menu_instance)

    def get(self, menubar):
        """get menu"""

        # Create the menu
        self.dev_install_menu = tk.Menu(menubar, tearoff=0)

        # Directory Actions
        # -----------------
        self.dev_install_menu.add_command(label="Open Directory", state=tk.DISABLED, command=lambda: None)
        self.dev_install_menu.add_separator()

        self.dev_install_menu.add_command(
            label="User",
            image=self.img.get("folder", 2),
            compound=tk.LEFT,
            command=self.handler.editor_installer_open_user_dir,
        )

        self.dev_install_menu.add_command(
            label="Dev",
            image=self.img.get("folder", 2),
            compound=tk.LEFT,
            command=self.handler.editor_installer_open_dev_dir,
        )

        # Empty Separator
        add_empty_menu_separator(self.dev_install_menu)

        # Mode Actions
        # -------------
        self.dev_install_menu.add_command(label="Activate Mode", state=tk.DISABLED, command=lambda: None)
        self.dev_install_menu.add_separator()

        enable_dev_mode_menu_name = DirectoryMode.DEVELOPER.name
        self.dev_install_menu.add_command(
            label=enable_dev_mode_menu_name,
            image=self.img.get("paintbrush", 2),
            compound=tk.LEFT,
            command=self.handler.editor_installer_enable_dev_mode,
        )

        disable_dev_mode_menu_name = DirectoryMode.USER.name
        self.dev_install_menu.add_command(
            label=disable_dev_mode_menu_name,
            image=self.img.get("cup_trophy_silhouette.png", 2),
            compound=tk.LEFT,
            command=self.handler.editor_installer_disable_dev_mode,
        )

        active_dir_mode = self.game.dir.get_active_mode()
        if active_dir_mode:
            self.dev_install_menu.entryconfigure(active_dir_mode.name, state="disabled")

        # self.dev_install_menu.add_separator()
        # currently_active_mode_name = f"Active: {self.game.dir.get_active_mode().name}"
        # currently_active_mode_name = f"{self.game.dir.get_active_mode().name}"
        # self.dev_install_menu.add_command(
        #     label=currently_active_mode_name, image=self.img.get("link", 2), compound=tk.LEFT, state=tk.DISABLED
        # )

        # Empty Separator
        add_empty_menu_separator(self.dev_install_menu)

        # Installation Actions
        # ---------------------
        self.dev_install_menu.add_command(label="Installation", state=tk.DISABLED, command=lambda: None)
        self.dev_install_menu.add_separator()

        self.dev_install_menu.add_command(
            label="Install",
            image=self.img.get("paintbrush", 2),
            compound=tk.LEFT,
            command=self.handler.editor_installer_install,
        )

        self.dev_install_menu.add_command(
            label="Update",
            image=self.img.get("reload", 2),
            compound=tk.LEFT,
            command=self.handler.editor_installer_update,
        )

        self.dev_install_menu.add_command(
            label="Repair",
            image=self.img.get("settings", 2),
            compound=tk.LEFT,
            command=self.handler.editor_installer_repair,
        )

        self.dev_install_menu.add_separator()

        self.dev_install_menu.add_command(
            label="Remove",
            image=self.img.get("delete", 2),
            compound=tk.LEFT,
            command=self.handler.editor_installer_uninstall,
        )

        if self.hud.edit.is_synced_and_being_edited():
            self.dev_install_menu.entryconfig(enable_dev_mode_menu_name, state="disabled")
            self.dev_install_menu.entryconfig(disable_dev_mode_menu_name, state="disabled")
            self.dev_install_menu.entryconfig("Install", state="disabled")
            self.dev_install_menu.entryconfig("Update", state="disabled")
            self.dev_install_menu.entryconfig("Repair", state="disabled")
            self.dev_install_menu.entryconfig("Remove", state="disabled")

        return self.dev_install_menu


def main():
    """debug"""
    from src.menu.main import EditorMenuClass

    gui = menu_debug_gui()
    editor_menu_instance = EditorMenuClass(gui)
    main_menu = tk.Menu(gui.root, tearoff=False)
    menu = MenuDevInstall(editor_menu_instance).get(main_menu)
    gui.debug_menu(menu)
    gui.show()


if __name__ == "__main__":
    main()

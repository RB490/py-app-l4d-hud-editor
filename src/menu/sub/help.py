# pylint: disable=attribute-defined-outside-init

import os
import tkinter as tk

from shared_gui.menu_debug import menu_debug_gui
from shared_utils.functions import open_file, open_url

from src.menu.base import EditorMenuBase
from src.menu.sub.hotkeys import MenuHotkeys
from src.utils.constants import PROJECT_ROOT, TUTORIALS_DIR


class MenuHelp(EditorMenuBase):
    """Menu"""

    def __init__(self, editor_menu_instance):
        super().__init__(editor_menu_instance)
        self.menu_hotkeys = MenuHotkeys(editor_menu_instance)

    def get(self, menubar):
        """get menu"""

        # doodleLink = "http://doodlesstuff.com/?p=tf2hud"
        doodle_link = "https://web.archive.org/web/20221023012414/https://doodlesstuff.com/?p=tf2hud"
        flame_path = os.path.join(TUTORIALS_DIR, "Flame's Guide to HUDs - flamehud by StefanB.pdf")
        doodle_path = os.path.join(TUTORIALS_DIR, "TF2 Hud Editing Guide - DoodlesStuff.mhtml")
        readme_path = os.path.join(PROJECT_ROOT, "README.MD")
        if self.game.get_title() == "Left 4 Dead":
            all_cvars_link = "https://developer.valvesoftware.com/wiki/List_of_L4D_Cvars"
        else:
            all_cvars_link = "https://developer.valvesoftware.com/wiki/List_of_L4D2_Cvars"

        self.help_menu = tk.Menu(menubar, tearoff=0)

        # help
        self.help_menu.add_command(label="Help", state="disabled")
        self.help_menu.add_separator()
        self.help_menu.add_command(
            label=f"{self.game.get_title()} Commands",
            image=self.img.get("link", 2),
            compound="left",
            command=lambda: open_url(all_cvars_link),
        )
        self.help_menu.add_command(
            label="Script Readme",
            image=self.img.get("file", 2),
            compound="left",
            command=lambda: open_file(readme_path),
        )
        self.help_menu.add_cascade(
            label="Hotkeys",
            image=self.img.get("buttons.png", 2),
            compound="left",
            menu=self.menu_hotkeys.get(menubar),
        )
        self.help_menu.add_separator()

        # tutorials
        self.help_menu.add_command(label="Tutorials", state="disabled")
        self.help_menu.add_command(
            label="TF2 Hud Editing Guide - DoodlesStuff",
            image=self.img.get("link", 2),
            compound="left",
            command=lambda: open_url(doodle_link),
        )
        self.help_menu.add_command(
            label="TF2 Hud Editing Guide - DoodlesStuff",
            image=self.img.get("file", 2),
            compound="left",
            command=lambda: open_file(doodle_path),
        )
        self.help_menu.add_command(
            label="Flame's Guide to HUDs - flamehud by StefanB",
            image=self.img.get("file", 2),
            compound="left",
            command=lambda: open_file(flame_path),
        )
        self.help_menu.add_separator()

        # update
        self.help_menu.add_command(label="Update", state="disabled")
        self.help_menu.add_separator()
        self.help_menu.add_cascade(
            label="About",
            image=self.img.get("star", 2),
            compound="left",
            command=self.handler.editor_show_about_menu,
        )

        return self.help_menu


def main():
    """debug"""
    from src.menu.main import EditorMenuClass

    gui = menu_debug_gui()
    editor_menu_instance = EditorMenuClass(gui)
    main_menu = tk.Menu(gui.root, tearoff=False)
    menu = MenuHelp(editor_menu_instance).get(main_menu)
    gui.debug_menu(menu)
    gui.show()


if __name__ == "__main__":
    main()

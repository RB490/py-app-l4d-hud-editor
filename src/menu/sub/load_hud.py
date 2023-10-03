# pylint: disable=attribute-defined-outside-init

import tkinter as tk

from shared_gui.menu_debug import menu_debug_gui
from shared_utils.functions import create_lambda_command

from src.menu.base import EditorMenuBase
from src.utils.constants import GAME_POSITIONS


class MenuLoadHud(EditorMenuBase):
    """Menu"""

    def __init__(self, editor_menu_instance):
        super().__init__(editor_menu_instance)

    def get(self, menubar):
        """get menu"""

        self.load_hud_menu = tk.Menu(menubar, tearoff=0)

        #######################################################################
        # stored huds
        #######################################################################
        stored_huds_submenu = tk.Menu(menubar, tearoff=0)
        remove_stored_hud_menu = tk.Menu(menubar, tearoff=0)
        self.load_hud_menu.add_cascade(
            label="Stored",
            image=self.img.get("open", 2),
            compound="left",
            menu=stored_huds_submenu,
        )

        # stored huds - root
        self.load_hud_menu.add_separator()
        for hud_dir in self.data_manager.get("stored_huds"):
            hud_name = self.hud.manager.retrieve_hud_name_for_dir(hud_dir)
            self.load_hud_menu.add_command(
                label=hud_name,
                command=create_lambda_command(self.handler.editor_edit_hud, hud_dir),
                image=self.img.get("paintbrush", 2),
                compound="left",
            )
            remove_stored_hud_menu.add_command(
                label=hud_name,
                image=self.img.get("minus", 2),
                compound="left",
                command=create_lambda_command(self.handler.editor_remove_stored_hud, hud_dir),
            )
        # stored huds - submenu - add stored hud
        stored_huds_submenu.add_command(
            label="New",
            image=self.img.get("star", 2),
            compound="left",
            command=self.handler.editor_create_new_hud,
        )
        # stored huds - submenu - create new stored hud
        stored_huds_submenu.add_command(
            label="Add",
            image=self.img.get("plus", 2),
            compound="left",
            command=self.handler.editor_add_existing_hud,
        )
        # stored huds - submenu - remove stored hud
        stored_huds_submenu.add_cascade(
            label="Remove", image=self.img.get("minus", 2), compound="left", menu=remove_stored_hud_menu
        )
        if not self.data_manager.get("stored_huds"):
            stored_huds_submenu.entryconfigure("Remove", state="disabled")
        self.load_hud_menu.add_separator()

        #######################################################################
        # temp huds
        #######################################################################
        temp_huds_submenu = tk.Menu(menubar, tearoff=0)
        remove_temp_hud_menu = tk.Menu(menubar, tearoff=0)
        self.load_hud_menu.add_cascade(
            label="Temporary",
            image=self.img.get("open", 2),
            compound="left",
            menu=temp_huds_submenu,
        )

        # stored huds - root
        self.load_hud_menu.add_separator()
        for hud_dir in self.data_manager.get("stored_temp_huds"):
            hud_name = self.hud.manager.retrieve_hud_name_for_dir(hud_dir)
            self.load_hud_menu.add_command(
                label=hud_name,
                command=create_lambda_command(self.handler.editor_edit_hud, hud_dir),
                image=self.img.get("paintbrush", 2),
                compound="left",
            )
            remove_temp_hud_menu.add_command(
                label=hud_name,
                image=self.img.minus_big_symbol,
                compound="left",
                command=create_lambda_command(self.handler.editor_remove_temp_hud, hud_dir),
            )
        # stored huds - submenu - add temp hud
        temp_huds_submenu.add_command(
            label="Open",
            image=self.img.get("plus", 2),
            compound="left",
            command=self.handler.editor_open_temp_hud,
        )
        # stored huds - submenu - remove temp hud
        temp_huds_submenu.add_cascade(
            label="Remove", image=self.img.get("minus", 2), compound="left", menu=remove_temp_hud_menu
        )
        if not self.data_manager.get("stored_temp_huds"):
            temp_huds_submenu.entryconfigure("Remove", state="disabled")

        self.load_hud_menu.add_separator()

        return self.load_hud_menu


def main():
    """debug"""
    from src.menu.main import EditorMenuClass

    gui = menu_debug_gui()
    editor_menu_instance = EditorMenuClass(gui)
    main_menu = tk.Menu(gui.root, tearoff=False)
    menu = MenuLoadHud(editor_menu_instance).get(main_menu)
    gui.debug_menu(menu)
    gui.show()


if __name__ == "__main__":
    main()

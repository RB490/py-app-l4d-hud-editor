# pylint: disable=attribute-defined-outside-init

import tkinter as tk

from shared_gui.menu_debug import menu_debug_gui
from shared_utils.functions import create_lambda_command

from src.menu.base import EditorMenuBase
from src.utils.constants import EDITOR_HUD_RELOAD_MODES


class MenuReloadMode(EditorMenuBase):
    """Menu"""

    def __init__(self, editor_menu_instance):
        super().__init__(editor_menu_instance)

    def get(self, menubar):
        """get menu"""

        self.reload_mode_menu = tk.Menu(menubar, tearoff=True)
        reload_once_menu = tk.Menu(menubar, tearoff=True)

        self.reload_mode_menu.add_command(label="Modes", state="disabled")
        self.reload_mode_menu.add_separator()

        # reload mode setting
        self.reload_mode_menu_hud_reload_mode = tk.IntVar()  # Variable to hold the selected mode
        for idx, (reload_mode, reload_code) in enumerate(EDITOR_HUD_RELOAD_MODES.items()):
            self.reload_mode_menu.add_radiobutton(
                label=reload_mode,
                variable=self.reload_mode_menu_hud_reload_mode,
                value=idx + 1,  # Start from 1, not 0
                command=create_lambda_command(self.handler.editor_menu_set_hud_reload_mode, f"{reload_code.lower()}"),
                image=self.img.get("reload", 2),
                compound="left",
            )

            # enable checkmark for selected
            if self.data_manager.get("hud_reload_mode") == reload_code:
                self.reload_mode_menu_hud_reload_mode.set(idx + 1)

        self.reload_mode_menu.add_command(label="Options", state="disabled", columnbreak=True)
        self.reload_mode_menu.add_separator()

        # reload once menu
        for reload_mode, reload_code in EDITOR_HUD_RELOAD_MODES.items():
            reload_once_menu.add_command(
                label=reload_mode,
                command=create_lambda_command(self.handler.editor_menu_reload_hud_once, f"{reload_code.lower()}"),
                image=self.img.get("reload", 2),
                compound="left",
            )

        # reload options
        self.reload_mode_menu_reopen_menu_checkmark = tk.BooleanVar()
        self.reload_mode_menu_reopen_menu_checkmark.set(self.data_manager.get("reload_reopen_menu_on_reload"))
        self.reload_mode_menu.add_checkbutton(
            label="Reopen menu on reload",
            variable=self.reload_mode_menu_reopen_menu_checkmark,
            command=self.handler.editor_menu_reload_reopen_menu,
            image=self.img.get("reload", 2),
            compound="left",
        )
        self.reload_mode_menu_coord_clicks_checkmark = tk.BooleanVar()
        self.reload_mode_menu.add_checkbutton(
            label="Reload clicks",
            variable=self.reload_mode_menu_coord_clicks_checkmark,
            command=self.handler.editor_menu_reload_click,
            image=self.img.get("reload", 2),
            compound="left",
        )
        self.reload_mode_menu_coord_clicks_checkmark.set(self.data_manager.get("reload_mouse_clicks_enabled"))
        # label_coord_1 = "Coord 1" + str(self.data_manager.get("reload_mouse_clicks_coord_1"))
        # label_coord_2 = "Coord 2" + str(self.data_manager.get("reload_mouse_clicks_coord_2"))
        coords_1 = self.data_manager.get("reload_mouse_clicks_coord_1")
        label_coord_1 = f"Coord 1 - X: {coords_1[0]}, Y: {coords_1[1]}"
        coords_2 = self.data_manager.get("reload_mouse_clicks_coord_2")
        label_coord_2 = f"Coord 2 - X: {coords_2[0]}, Y: {coords_2[1]}"
        self.reload_mode_menu.add_command(
            label=label_coord_1,
            image=self.img.get("reload", 2),
            compound="left",
            command=self.handler.editor_menu_reload_click_coord1,
        )
        self.reload_mode_menu.add_command(
            label=label_coord_2,
            image=self.img.get("reload", 2),
            compound="left",
            command=self.handler.editor_menu_reload_click_coord2,
        )
        self.reload_mode_menu.add_cascade(
            label="Once",
            menu=reload_once_menu,
            image=self.img.get("reload", 2),
            compound="left",
        )

        return self.reload_mode_menu


def main():
    """debug"""
    from src.menu.main import EditorMenuClass

    gui = menu_debug_gui()
    editor_menu_instance = EditorMenuClass(gui)
    main_menu = tk.Menu(gui.root, tearoff=True)
    menu = MenuReloadMode(editor_menu_instance).get(main_menu)
    gui.debug_menu(menu)
    gui.show()


if __name__ == "__main__":
    main()

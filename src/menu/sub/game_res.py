# pylint: disable=attribute-defined-outside-init

import tkinter as tk

from shared_gui.menu_debug import menu_debug_gui
from shared_utils.functions import create_lambda_command

from src.menu.base import EditorMenuBase


class MenuGameRes(EditorMenuBase):
    """Menu"""

    def __init__(self, editor_menu_instance):
        super().__init__(editor_menu_instance)

    def get(self, menubar):
        """get menu"""

        self.game_res_menu = tk.Menu(menubar, tearoff=True)
        res_4_3_menu = tk.Menu(self.game_res_menu, tearoff=True)
        res_16_9_menu = tk.Menu(self.game_res_menu, tearoff=True)
        res_16_10_menu = tk.Menu(self.game_res_menu, tearoff=True)

        res_4_3_list = [
            "640x480",
            "720x576",
            "800x600",
            "1024x768",
            "1152x864",
            "1280x960",
            "1400x1050",
            "1600x1200",
            "2048x1536",
        ]
        for res in res_4_3_list:
            res_4_3_menu.add_command(
                label=res,
                image=self.img.get("monitor_black_tool.png", 2),
                compound="left",
                command=create_lambda_command(self.handler.editor_menu_game_resolution, res),
            )

        res_16_9_list = [
            "852x480",
            "1280x720",
            "1360x768",
            "1366x768",
            "1600x900",
            "1920x1080",
            "2560x1440",
            "3840x2160",
        ]
        for res in res_16_9_list:
            res_16_9_menu.add_command(
                label=res,
                image=self.img.get("monitor_black_tool.png", 2),
                compound="left",
                command=create_lambda_command(self.handler.editor_menu_game_resolution, res),
            )

        res_16_10_list = [
            "720x480",
            "1280x768",
            "1280x800",
            "1440x900",
            "1600x1024",
            "1680x1050",
            "1920x1200",
            "2560x1600",
            "3840x2400",
            "7680x4800",
        ]
        for res in res_16_10_list:
            res_16_10_menu.add_command(
                label=res,
                image=self.img.get("monitor_black_tool.png", 2),
                compound="left",
                command=create_lambda_command(self.handler.editor_menu_game_resolution, res),
            )

        self.game_res_menu.add_cascade(
            label="4:3", image=self.img.get("monitor_black_tool.png", 2), compound="left", menu=res_4_3_menu
        )
        self.game_res_menu.add_cascade(
            label="16:9", image=self.img.get("monitor_black_tool.png", 2), compound="left", menu=res_16_9_menu
        )
        self.game_res_menu.add_cascade(
            label="16:10", image=self.img.get("monitor_black_tool.png", 2), compound="left", menu=res_16_10_menu
        )

        return self.game_res_menu


def main():
    """debug"""
    from src.menu.main import EditorMenuClass

    gui = menu_debug_gui()
    editor_menu_instance = EditorMenuClass(gui)
    main_menu = tk.Menu(gui.root, tearoff=True)
    menu = MenuGameRes(editor_menu_instance).get(main_menu)
    gui.debug_menu(menu)
    gui.show()


if __name__ == "__main__":
    main()

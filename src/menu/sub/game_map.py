# pylint: disable=attribute-defined-outside-init

import os
import tkinter as tk

from shared_gui.menu_debug import menu_debug_gui

from src.menu.base import EditorMenuBase
from src.utils.constants import IMAGES_DIR_MISC, MAP_CODES


class MenuGameMap(EditorMenuBase):
    """Menu"""

    def __init__(self, editor_menu_instance):
        super().__init__(editor_menu_instance)

    def get(self, menubar):
        """get menu"""

        self.game_map_menu = tk.Menu(menubar, tearoff=True)
        # self.game_map_menu = tk.Menu(self.game_menu, tearoff=True)

        self.map_menu_l4d1_icon = tk.PhotoImage(
            # file=BIG_CROSS_ICON
            file=os.path.join(IMAGES_DIR_MISC, "left_4_dead_small_grayscale.png")
        ).subsample(1, 1)
        # self.map_menu_l4d2_icon = PhotoImage(
        #     file=os.path.join(IMAGES_DIR, "Left 4 Dead 2 small grayscale.png")
        # ).subsample(1, 1)

        self.map_menu_l4d2_icon = tk.PhotoImage(
            file=os.path.join(IMAGES_DIR_MISC, "left_4_dead_2_small_grayscale.png")
        )

        # main menu
        self.game_map_menu.add_command(
            label="Main Menu",
            command=self.handler.editor_menu_disconnect,
            image=self.img.get("black_map_folded_paper_symbol.png", 2),
            compound="left",
        )
        self.game_map_menu.add_separator()

        # misc maps
        self.game_map_menu.add_command(
            label="Hud Dev Map",
            command=lambda: self.handler.editor_menu_game_map("Hud Dev Map", "hud_dev_map"),
            image=self.img.get("black_map_folded_paper_symbol.png", 2),
            compound="left",
        )
        if self.game.get_version() == "L4D2":
            self.game_map_menu.add_command(
                label="Curling Stadium",
                image=self.img.get("black_map_folded_paper_symbol.png", 2),
                compound="left",
                command=lambda: self.handler.editor_menu_game_map("Curling Stadium", "curling_stadium"),
            )
        self.game_map_menu.add_command(
            label="Tutorial Standards",
            image=self.img.get("black_map_folded_paper_symbol.png", 2),
            compound="left",
            command=lambda: self.handler.editor_menu_game_map("Tutorial Standards", "tutorial_standards"),
        )
        self.game_map_menu.add_separator()

        # Create the L4D1 and L4D2 submenus
        map_menu_l4d1 = tk.Menu(self.game_map_menu, tearoff=True)
        map_menu_l4d2 = tk.Menu(self.game_map_menu, tearoff=True)
        self.game_map_menu.add_cascade(
            label="L4D1",
            menu=map_menu_l4d1,
            image=self.img.get("black_map_folded_paper_symbol.png", 2),
            compound=tk.LEFT,
        )
        self.game_map_menu.add_cascade(
            label="L4D2",
            menu=map_menu_l4d2,
            image=self.img.get("black_map_folded_paper_symbol.png", 2),
            compound=tk.LEFT,
        )

        # Separate L4D1 and L4D2 campaigns
        l4d1_campaigns = [
            "No Mercy",
            "Crash Course",
            "Death Toll",
            "Dead Air",
            "Blood Harvest",
            "The Sacrifice",
            "The Last Stand",
        ]
        # pylint: disable=unused-variable
        l4d2_campaigns = [
            "Dead Center",
            "Dark Carnival",
            "Swamp Fever",
            "Hard Rain",
            "The Parish",
            "The Passing",
            "Cold Stream",
        ]

        # Loop through each campaign in MAP_CODES
        for campaign, maps in MAP_CODES.items():
            # Create a submenu for the campaign
            if campaign in l4d1_campaigns:
                campaign_submenu = tk.Menu(map_menu_l4d1, tearoff=True)
                map_menu_l4d1.add_cascade(
                    label=campaign,
                    image=self.img.get("black_map_folded_paper_symbol.png", 2),
                    compound=tk.LEFT,
                    menu=campaign_submenu,
                )
            else:
                campaign_submenu = tk.Menu(map_menu_l4d2, tearoff=True)
                map_menu_l4d2.add_cascade(
                    label=campaign,
                    image=self.img.get("black_map_folded_paper_symbol.png", 2),
                    compound=tk.LEFT,
                    menu=campaign_submenu,
                )

            # Add each map to the campaign submenu
            for map_info in maps:
                map_name = map_info["name"]
                map_code = map_info["code"]
                campaign_submenu.add_command(
                    label=map_name,
                    command=lambda map_name=map_name, map_code=map_code: self.handler.editor_menu_game_map(
                        map_name, map_code
                    ),
                    image=self.img.get("black_map_folded_paper_symbol.png", 2),
                    compound=tk.LEFT,
                )

        return self.game_map_menu


def main():
    """debug"""
    from menu.main import EditorMenuClass

    gui = menu_debug_gui()
    editor_menu_instance = EditorMenuClass(gui)
    main_menu = tk.Menu(gui.root, tearoff=True)
    menu = MenuGameMap(editor_menu_instance).get(main_menu)
    gui.debug_menu(menu)
    gui.show()


if __name__ == "__main__":
    main()

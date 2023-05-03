"""Module for the """
import os
import tkinter as tk
from tkinter import Menu, PhotoImage
import keyboard
from modules.utils.constants import IMAGES_DIR
from modules.utils.functions import load_data


# Dictionary of map codes for each map
MAP_CODES = {
    "No Mercy": [
        {"name": "The Apartments", "code": "c8m1_apartment"},
        {"name": "The Subway", "code": "c8m2_subway"},
        {"name": "The Sewer", "code": "c8m3_sewers"},
        {"name": "The Hospital", "code": "c8m4_interior"},
        {"name": "Rooftop Finale", "code": "c8m5_rooftop"},
    ],
    "Crash Course": [
        {"name": "The Alleys", "code": "c2m1_highway"},
        {"name": "The Truck Depot Finale", "code": "c2m5_truckfactory"},
    ],
    "Death Toll": [
        {"name": "The Turnpike", "code": "c4m1_milltown_a"},
        {"name": "The Drains", "code": "c4m2_sugarmill_a"},
        {"name": "The Church", "code": "c4m3_creekbed_a"},
        {"name": "The Town", "code": "c4m4_ranchhouse_a"},
        {"name": "Boathouse Finale", "code": "c4m5_boat"},
    ],
    "Dead Air": [
        {"name": "The Greenhouse", "code": "c5m1_greenhouse"},
        {"name": "The Crane", "code": "c5m2_offices"},
        {"name": "The Construction Site", "code": "c5m3_bldg17"},
        {"name": "The Terminal", "code": "c5m4_terminal"},
        {"name": "Runway Finale", "code": "c5m5_runway"},
    ],
    "Blood Harvest": [
        {"name": "The Woods", "code": "c6m1_riverside"},
        {"name": "The Tunnel", "code": "c6m2_bedlam_a"},
        {"name": "The Bridge", "code": "c6m3_port_a"},
        {"name": "The Train Station", "code": "c6m4_mainstreet"},
        {"name": "Farmhouse Finale", "code": "c6m5_stairway"},
    ],
    "The Sacrifice": [
        {"name": "Docks", "code": "l4d2_docks"},
        {"name": "Barge", "code": "l4d2_barge"},
        {"name": "Port", "code": "l4d2_port"},
        {"name": "Sewer Junction", "code": "l4d2_sewers"},
        {"name": "Sacrificial Boat", "code": "l4d2_cemetery"},
    ],
    "Dead Center": [
        {"name": "Hotel", "code": "c1m1_hotel"},
        {"name": "Mall", "code": "c1m2_streets"},
        {"name": "Atrium", "code": "c1m3_atrium"},
        {"name": "Gun Shop", "code": "c1m4_mall"},
        {"name": "Concert Finale", "code": "c1m5_concert"},
    ],
    "Dark Carnival": [
        {"name": "Garage", "code": "c2m2_fairgrounds"},
        {"name": "Motel", "code": "c2m3_coaster"},
        {"name": "Barns", "code": "c2m4_barns"},
        {"name": "Concert", "code": "c2m5_concert"},
        {"name": "Atrium Finale", "code": "c2m5_atrium"},
    ],
    "Swamp Fever": [
        {"name": "Plank Country", "code": "c3m1_plankcountry"},
        {"name": "The Swamp", "code": "c3m2_swamp"},
        {"name": "Shantytown", "code": "c3m3_shantytown"},
        {"name": "The Plantation", "code": "c3m4_plantation"},
    ],
    "Hard Rain": [
        {"name": "Milltown", "code": "c13m1_milltown"},
        {"name": "Sugar Mill", "code": "c13m2_sugarmill"},
        {"name": "Mill Escape", "code": "c13m3_sugarmill_l4d2"},
        {"name": "Whitaker Farm", "code": "c13m4_lighthouse"},
        {"name": "Town Escape", "code": "c13m5_bridge"},
    ],
    "The Parish": [
        {"name": "Waterfront Market", "code": "c4m1_milltown_a"},
        {"name": "The Boulevard", "code": "c4m2_sugarmill_a"},
        {"name": "The Underground", "code": "c4m3_creekbed_a"},
        {"name": "The Rooftop", "code": "c4m4_ranchhouse_a"},
        {"name": "The Bridge", "code": "c4m5_boat"},
    ],
    "The Passing": [
        {"name": "The Riverbank", "code": "c13m1_l4d_garage"},
        {"name": "The Underground", "code": "c13m2_l4d_subway"},
        {"name": "The Port", "code": "c13m3_l4d_sewer"},
        {"name": "The Truck Depot Finale", "code": "c13m4_l4d_interactive"},
    ],
    "Cold Stream": [
        {"name": "Alpine Creek", "code": "c6m1_riverside"},
        {"name": "South Pine Stream", "code": "c6m2_bedlam_a"},
        {"name": "Memorial Bridge", "code": "c6m3_port_a"},
        {"name": "Cut-throat Creek", "code": "c6m4_mainstreet"},
        {"name": "Truck Depot Finale", "code": "c6m5_stairway"},
    ],
    "The Last Stand": [
        {"name": "The Junkyard", "code": "c14m1_junkyard"},
        {"name": "The Lighthouse", "code": "c14m2_lighthouse"},
    ],
}

# Separate L4D1 and L4D2 campaigns
L4D1_CAMPAIGNS = [
    "No Mercy",
    "Crash Course",
    "Death Toll",
    "Dead Air",
    "Blood Harvest",
    "The Sacrifice",
    "The Last Stand",
]
L4D2_CAMPAIGNS = [
    "Dead Center",
    "Dark Carnival",
    "Swamp Fever",
    "Hard Rain",
    "The Parish",
    "The Passing",
    "Cold Stream",
]


class EditorMenuMethods:
    def editor_menu_game_mode(self, selected_option):
        """Method to handle the selected game mode in the menu."""
        # Implement the logic to handle the selected game mode here
        print(f"The selected option is: {selected_option}")

    def editor_menu_change_map(self, map_name, map_code):
        print(f"The code for {map_name} is {map_code}.")


class GuiEditorMenu:
    """
    A class representing a toggle window with hotkey functionality and a menu bar.

    Attributes:
        root (tkinter.Tk): The main window of the application.
        is_hidden (bool): A flag indicating whether the window is currently hidden.

    Methods:
        __init__(self): Initializes the ToggleWindow instance and runs the main event loop.
        toggle_visibility(self): Toggles the visibility of the window.
        setup_hotkey(self): Sets up the hotkey for toggling window visibility.
        create_menu(self): Creates the menu bar for the application.
        do_nothing(self): A dummy function that does nothing.
    """

    def __init__(self, persistent_data):
        """
        Initializes a new instance of the ToggleWindow class and runs the main event loop.
        """
        self.root = tk.Tk()
        self.root.geometry("300x200")
        self.root.title("Toggle Window")
        self.is_hidden = False
        self.persistent_data = persistent_data
        self.setup_hotkey()
        self.create_menu()
        self.root.mainloop()

    def add_map_command(self, campaign_submenu, map_info):
        map_name = map_info["name"]
        map_code = map_info["code"]
        campaign_submenu.add_command(
            label=map_name, command=lambda: EditorMenuMethods().editor_menu_change_map(map_name, map_code)
        )

    def toggle_visibility(self):
        """
        Toggles the visibility of the window between visible and hidden.
        """
        if self.is_hidden:
            self.root.deiconify()
            self.is_hidden = False
        else:
            self.root.withdraw()
            self.is_hidden = True

    def setup_hotkey(self):
        """
        Sets up the F5 key as the hotkey for toggling window visibility.
        """
        keyboard.add_hotkey("F5", self.toggle_visibility)

    def create_menu(self):
        """
        Creates the menu bar for the application with three cascading menus: File, Edit, and Help.
        """
        menubar = Menu(self.root)

        # Create the image object for the Open icon
        self.open_icon = PhotoImage(file=os.path.join(IMAGES_DIR, "folder.png")).subsample(2, 2)

        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label="New", command=self.do_nothing)
        filemenu.add_command(label="Open", image=self.open_icon, compound=tk.LEFT, command=self.do_nothing)
        filemenu.add_command(label="Save", command=self.do_nothing)
        filemenu.add_command(label="Save as...", command=self.do_nothing)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=self.root.quit)
        menubar.add_cascade(label="File", menu=filemenu)

        editmenu = Menu(menubar, tearoff=0)
        editmenu.add_command(label="Undo", command=self.do_nothing)
        editmenu.add_separator()
        editmenu.add_command(label="Cut", command=self.do_nothing)
        editmenu.add_command(label="Copy", command=self.do_nothing)
        editmenu.add_command(label="Paste", command=self.do_nothing)
        editmenu.add_command(label="Delete", command=self.do_nothing)
        editmenu.add_command(label="Select All", command=self.do_nothing)
        menubar.add_cascade(label="Edit", menu=editmenu)

        helpmenu = Menu(menubar, tearoff=0)
        helpmenu.add_command(label="Help Index", command=self.do_nothing)
        helpmenu.add_command(label="About...", command=self.do_nothing)
        menubar.add_cascade(label="Help", menu=helpmenu)

        # Create the Game menu
        game_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Game", menu=game_menu)

        # ----------------------------------
        #       Create the Game Mode menu
        # ----------------------------------

        menubar.add_command(label="Coop", command=lambda: EditorMenuMethods().editor_menu_game_mode("Coop"))
        menubar.add_command(label="Survival", command=lambda: EditorMenuMethods().editor_menu_game_mode("Survival"))
        menubar.add_command(label="Versus", command=lambda: EditorMenuMethods().editor_menu_game_mode("Versus"))
        menubar.add_command(label="Scavenge", command=lambda: EditorMenuMethods().editor_menu_game_mode("Scavenge"))

        # ----------------------------------
        #       Create the Change Map menu
        # ----------------------------------
        self.map_menu_l4d1_icon = PhotoImage(
            file=os.path.join(IMAGES_DIR, "Left 4 Dead small grayscale.png")
        ).subsample(1, 1)
        self.map_menu_l4d2_icon = PhotoImage(
            file=os.path.join(IMAGES_DIR, "Left 4 Dead 2 small grayscale.png")
        ).subsample(1, 1)
        change_map_menu = tk.Menu(game_menu, tearoff=0)
        change_map_menu.add_command(
            label="Curling Stadium",
            command=lambda: EditorMenuMethods().editor_menu_change_map("Curling Stadium", "curling_stadium"),
        )
        change_map_menu.add_command(
            label="Tutorial Standards",
            command=lambda: EditorMenuMethods().editor_menu_change_map("Tutorial Standards", "tutorial_standards"),
        )
        game_menu.add_cascade(label="Map", menu=change_map_menu)

        # Create the L4D1 and L4D2 submenus
        map_menu_l4d1 = tk.Menu(change_map_menu, tearoff=0)
        map_menu_l4d2 = tk.Menu(change_map_menu, tearoff=0)
        change_map_menu.add_cascade(
            label="L4D1",
            menu=map_menu_l4d1,
            image=self.map_menu_l4d1_icon,
            compound=tk.LEFT,
        )
        change_map_menu.add_cascade(
            label="L4D2",
            menu=map_menu_l4d2,
            image=self.map_menu_l4d2_icon,
            compound=tk.LEFT,
        )

        # Loop through each campaign in MAP_CODES
        for campaign, maps in MAP_CODES.items():
            # Create a submenu for the campaign
            if campaign in L4D1_CAMPAIGNS:
                campaign_submenu = tk.Menu(map_menu_l4d1, tearoff=0)
                map_menu_l4d1.add_cascade(label=campaign, menu=campaign_submenu)
            else:
                campaign_submenu = tk.Menu(map_menu_l4d2, tearoff=0)
                map_menu_l4d2.add_cascade(label=campaign, menu=campaign_submenu)

            # Add each map to the campaign submenu
            for map_info in maps:
                self.add_map_command(campaign_submenu, map_info)

        # ----------------------------------
        #       Add the menu to the gui
        # ----------------------------------

        self.root.config(menu=menubar)

    def do_nothing(self):
        """
        A dummy function that does nothing.
        """
        print("Do nothing")


def debug_gui_editor_menu():
    """Debug gui class"""
    # pylint: disable=unused-variable
    persistent_data = load_data()
    app = GuiEditorMenu(persistent_data)

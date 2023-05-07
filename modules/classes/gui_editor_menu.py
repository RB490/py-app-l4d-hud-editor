# pylint : disable=too-many-lines ####
"""Module for the editor menu"""
import os
import tkinter as tk
from tkinter import Menu, PhotoImage
from tkinter import messagebox
import webbrowser
import keyboard
import pyperclip
from modules.utils.constants import SNIPPETS_DIR, IMAGES_DIR, SCRIPT_DIR, TUTORIALS_DIR
from modules.utils.functions import (
    prompt_add_existing_hud,
    prompt_open_temp_hud,
    remove_stored_hud,
    remove_temp_hud,
    retrieve_hud_name_for_dir,
)

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

    def __init__(self, persistent_data, game_instance, hud_instance):
        """
        Initializes a new instance of the ToggleWindow class and runs the main event loop.
        """
        self.root = tk.Tk()
        self.root.geometry("300x200")
        self.root.title("Toggle Window")
        self.is_hidden = False
        self.persistent_data = persistent_data
        self.game = game_instance
        self.hud = hud_instance
        keyboard.add_hotkey("F5", self.toggle_visibility)
        self.create_and_refresh_menu()
        # super().__init__(self, persistent_data, game_instance, hud_instance)
        self.root.mainloop()

    def create_lambda_command(self, func, *args):
        """
        The `create_lambda_command` method takes in a function `func`
        and any number of positional arguments `*args`
        and returns a lambda function that, when called,
        will execute the given function with the supplied arguments.

        :param self: the instance of the class that the method belongs to.
        :param func: the function that will be executed by the lambda command returned from this method.
        :param *args: any number of positional arguments that will be passed to the function when
            called through the returned lambda command.

        :return: A lambda function that executes the input function `func` with its corresponding arguments `args`.

        #Example:
            campaign_submenu.add_command(
                label=map_name, command=self.create_lambda_command(self.editor_menu_game_map, map_name, map_code)
            )
            > so when this menu entry is selected self.editor_menu_game_map gets called with map_name and map_code

        This method is useful for creating a function on-the-fly that takes no arguments
        but still needs to execute some code with certain values or variables.
        By using a lambda function created by `create_lambda_function`,
        you can defer binding the arguments until later when needed.
        This technique is also known as partial evaluation or currying,
        and it is commonly used in functional programming.
        """
        return lambda: func(*args)

    def open_file(self, path):
        """Open file"""
        print(path)
        os.startfile(path)

    def open_url(self, url):
        """Open url"""
        webbrowser.open(url)

    def do_nothing(self, *args):
        # pylint: disable=unused-argument
        """
        A dummy function that does nothing.
        """
        print("Do nothing with:", args)

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

    def create_and_refresh_menu(self):
        """
        Creates the menu bar for the application with three cascading menus: File, Edit, and Help.
        """
        menubar = Menu(self.root)

        # Create the image object for the Open icon
        self.open_icon = PhotoImage(file=os.path.join(IMAGES_DIR, "folder.png")).subsample(2, 2)

        # ----------------------------------
        #       Create reload mode menu
        # ----------------------------------

        self.reload_mode_menu = tk.Menu(menubar, tearoff=0)
        reload_once_menu = tk.Menu(menubar, tearoff=0)

        self.reload_mode_menu.add_command(label="Modes", state="disabled")
        self.reload_mode_menu.add_separator()

        reload_modes = ["All", "Hud", "Menu", "Materials", "Fonts"]
        for reload_mode in reload_modes:
            self.reload_mode_menu.add_command(
                label=reload_mode, command=self.create_lambda_command(self.do_nothing, f"reload_{reload_mode.lower()}")
            )

        self.reload_mode_menu.add_command(label="Options", state="disabled", columnbreak=True)
        self.reload_mode_menu.add_separator()

        for reload_mode in reload_modes:
            reload_once_menu.add_command(
                label=reload_mode, command=self.create_lambda_command(self.do_nothing, f"reload_{reload_mode.lower()}")
            )

        self.reload_mode_menu.add_cascade(label="Once", menu=reload_once_menu)
        self.reload_mode_menu_coord_clicks_checkmark = tk.BooleanVar()
        self.reload_mode_menu.add_checkbutton(
            label="Reopen menu on reload",
            variable=self.reload_mode_menu_coord_clicks_checkmark,
            command=self.editor_menu_reload_click,
        )
        self.reload_mode_menu_coord_clicks_checkmark.set(self.persistent_data["reload_mouse_clicks_enabled"])
        self.reload_mode_menu.add_command(label="Coord 1", command=self.editor_menu_reload_click_coord1)
        self.reload_mode_menu.add_command(label="Coord 2", command=self.editor_menu_reload_click_coord2)

        # ----------------------------------
        #       Create Hud menu
        # ----------------------------------

        self.hud_menu = tk.Menu(menubar, tearoff=0)
        self.hud_menu.add_command(label="<hud_name>", state="disabled")
        if self.hud.get_dir():
            self.hud_menu.entryconfigure(0, label=retrieve_hud_name_for_dir(self.hud.get_dir()))
        self.hud_menu.add_command(label="Unsync", command=self.editor_unsync_hud)
        self.hud_menu.add_command(label="Save", state="disabled")
        self.hud_menu.add_command(label="VPK", command=self.editor_save_as_vpk)
        self.hud_menu.add_command(label="Folder", command=self.editor_save_as_folder)
        self.hud_menu.add_command(label="Open", state="disabled", columnbreak=True)
        self.hud_menu.add_command(
            label="Hud", command=self.create_lambda_command(self.editor_open_folder, self.hud.get_dir())
        )
        self.hud_menu.add_command(
            label="Hud (VS)", command=self.create_lambda_command(self.editor_open_folder_in_vscode, self.hud.get_dir())
        )

        # ----------------------------------
        #       Create Game Mode menu
        # ----------------------------------

        self.game_menu = tk.Menu(menubar, tearoff=0)
        game_modes = ["Coop", "Survival", "Versus", "Scavenge"]
        self.game_mode_menu = tk.Menu(menubar, tearoff=0)
        self.game_mode_vars = {}
        for reload_mode in game_modes:
            self.game_mode_vars[reload_mode] = tk.BooleanVar()
            self.game_mode_menu.add_checkbutton(
                label=reload_mode,
                variable=self.game_mode_vars[reload_mode],
                onvalue=True,
                offvalue=False,
                command=lambda mode=reload_mode: self.editor_menu_game_mode(mode),
            )
        self.game_mode_vars[self.persistent_data["game_mode"]].set(True)

        # ----------------------------------
        #       Create Game Resolution menu
        # ----------------------------------

        game_res_menu = tk.Menu(menubar, tearoff=0)
        res_4_3_menu = tk.Menu(game_res_menu, tearoff=0)
        res_16_9_menu = tk.Menu(game_res_menu, tearoff=0)
        res_16_10_menu = tk.Menu(game_res_menu, tearoff=0)

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
            res_4_3_menu.add_command(label=res, command=lambda r=res: self.editor_menu_game_resolution(r))

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
            res_16_9_menu.add_command(label=res, command=lambda r=res: self.editor_menu_game_resolution(r))

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
            res_16_10_menu.add_command(label=res, command=lambda r=res: self.editor_menu_game_resolution(r))

        game_res_menu.add_cascade(label="4:3", menu=res_4_3_menu)
        game_res_menu.add_cascade(label="16:9", menu=res_16_9_menu)
        game_res_menu.add_cascade(label="16:10", menu=res_16_10_menu)

        # ----------------------------------
        #       Create Change Map menu
        # ----------------------------------
        self.map_menu_l4d1_icon = PhotoImage(
            file=os.path.join(IMAGES_DIR, "Left 4 Dead small grayscale.png")
        ).subsample(1, 1)
        self.map_menu_l4d2_icon = PhotoImage(
            file=os.path.join(IMAGES_DIR, "Left 4 Dead 2 small grayscale.png")
        ).subsample(1, 1)
        game_map_menu = tk.Menu(self.game_menu, tearoff=0)

        # main menu
        game_map_menu.add_command(
            label="Main Menu",
            command=self.create_lambda_command(self.editor_menu_send_keys, "{F11}"),
        )
        game_map_menu.add_separator()

        # misc maps
        game_map_menu.add_command(
            label="Hud Dev Map",
            command=lambda: self.editor_menu_game_map("Hud Dev Map", "hud_dev_map"),
        )
        if self.game.get_version() is "L4D2":
            game_map_menu.add_command(
                label="Curling Stadium",
                command=lambda: self.editor_menu_game_map("Curling Stadium", "curling_stadium"),
            )
        game_map_menu.add_command(
            label="Tutorial Standards",
            command=lambda: self.editor_menu_game_map("Tutorial Standards", "tutorial_standards"),
        )
        game_map_menu.add_separator()

        # Create the L4D1 and L4D2 submenus
        map_menu_l4d1 = tk.Menu(game_map_menu, tearoff=0)
        map_menu_l4d2 = tk.Menu(game_map_menu, tearoff=0)
        game_map_menu.add_cascade(
            label="L4D1",
            menu=map_menu_l4d1,
            image=self.map_menu_l4d1_icon,
            compound=tk.LEFT,
        )
        game_map_menu.add_cascade(
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
                map_name = map_info["name"]
                map_code = map_info["code"]
                campaign_submenu.add_command(
                    label=map_name, command=self.create_lambda_command(self.editor_menu_game_map, map_name, map_code)
                )

        # ----------------------------------
        #       Create Game Pos menu
        # ----------------------------------

        positions = [
            "Custom (Save)",
            "Center",
            "Top Left",
            "Top Right",
            "Bottom Left",
            "Bottom Right",
            "Top",
            "Bottom",
            "Left",
            "Right",
        ]
        self.game_pos_menu = tk.Menu(menubar, tearoff=0)
        self.game_pos_vars = {}
        for pos in positions:
            self.game_pos_vars[pos] = tk.BooleanVar()
            self.game_pos_menu.add_checkbutton(
                label=pos,
                variable=self.game_pos_vars[pos],
                onvalue=True,
                offvalue=False,
                command=lambda pos=pos: self.editor_menu_game_pos(pos),
            )
        self.game_pos_vars[self.persistent_data["game_pos"]].set(True)

        # ----------------------------------
        #       Create Hotkeys menu
        # ----------------------------------

        hotkeys_menu = Menu(menubar)
        hotkeys_menu.add_command(label="Global")
        hotkeys_menu.entryconfig("Global", state="disabled")
        hotkeys_menu.add_separator()
        hotkeys_menu.add_command(label="Sync Hud", accelerator="Ctrl+S")
        hotkeys_menu.add_command(label="Show Menu", accelerator="F4")
        hotkeys_menu.add_command(label="Browse Files", accelerator="F8")
        hotkeys_menu.add_separator()
        hotkeys_menu.add_command(label="In-Game")
        hotkeys_menu.entryconfig("In-Game", state="disabled")
        hotkeys_menu.add_separator()
        hotkeys_menu.add_command(label="Load Dead Center finale", accelerator="O")
        hotkeys_menu.add_command(label="Play credits (On a finale level)", accelerator="P")
        hotkeys_menu.add_command(label="Noclip", accelerator="G")
        hotkeys_menu.add_command(label="Pause", accelerator="F8")
        hotkeys_menu.add_command(label="Admin system menu", accelerator="N")
        hotkeys_menu.add_command(label="Slow-mo game speed", accelerator="F9")
        hotkeys_menu.add_command(label="Default game speed", accelerator="F10")
        hotkeys_menu.add_command(label="Last game cmd", accelerator="F11")
        # helpmenu.add_cascade(label="Hotkeys", menu=hotkeys_menu)

        # ----------------------------------
        #       Create help menu
        # ----------------------------------

        # doodleLink = "http://doodlesstuff.com/?p=tf2hud"
        doodle_link = "https://web.archive.org/web/20221023012414/https://doodlesstuff.com/?p=tf2hud"
        flame_path = os.path.join(TUTORIALS_DIR, "Flame's Guide to HUDs - flamehud by StefanB.pdf")
        doodle_path = os.path.join(TUTORIALS_DIR, "TF2 Hud Editing Guide - DoodlesStuff.mhtml")
        readme_path = os.path.join(SCRIPT_DIR, "README.MD")
        if self.game.get_title() is "Left 4 Dead":
            all_cvars_link = "https://developer.valvesoftware.com/wiki/List_of_L4D_Cvars"
        else:
            all_cvars_link = "https://developer.valvesoftware.com/wiki/List_of_L4D2_Cvars"

        helpmenu = Menu(menubar, tearoff=0)
        helpmenu.add_cascade(label="Hotkeys", menu=hotkeys_menu)
        helpmenu.add_command(label="Script Readme", command=lambda: self.open_file(readme_path))
        helpmenu.add_command(label="All Game Commands", command=lambda: self.open_url(all_cvars_link))
        helpmenu.add_separator()
        helpmenu.add_command(label="Tutorials")
        helpmenu.entryconfig("Tutorials", state="disabled")
        helpmenu.add_command(
            label="TF2 Hud Editing Guide - DoodlesStuff (link)", command=lambda: self.open_url(doodle_link)
        )
        helpmenu.add_command(
            label="TF2 Hud Editing Guide - DoodlesStuff (file)", command=lambda: self.open_file(doodle_path)
        )
        helpmenu.add_command(
            label="Flame's Guide to HUDs - flamehud by StefanB", command=lambda: self.open_file(flame_path)
        )

        # ----------------------------------
        #       Create Voting menu
        # ----------------------------------

        # Define the data dictionary with display names for each option and section
        voting_data = {
            "general_commands": {
                "display_name": "General Votes",
                "available_votes": [
                    {"display_name": "Restart game", "vote_command": "RestartGame"},
                    {"display_name": "Return to lobby", "vote_command": "ReturnToLobby"},
                    {"display_name": "Change all talk", "vote_command": "ChangeAllTalk"},
                ],
            },
            "change_mission": {
                "display_name": "Campaign Votes",
                "available_votes": {
                    "L4D1": [
                        {"display_name": "No Mercy", "vote_command": "ChangeMission Hospital"},
                        {"display_name": "Crash Course", "vote_command": "ChangeMission Garage"},
                        {"display_name": "Death Toll", "vote_command": "ChangeMission River"},
                        {"display_name": "Dead Air", "vote_command": "ChangeMission Airport"},
                        {"display_name": "Blood Harvest", "vote_command": "ChangeMission Farm"},
                        {"display_name": "The Sacrifice", "vote_command": "ChangeMission River"},
                    ],
                    "L4D2": [
                        {"display_name": "Dead Center", "vote_command": "ChangeMission L4D2C1"},
                        {"display_name": "Dark Carnival", "vote_command": "ChangeMission L4D2C2"},
                        {"display_name": "Swamp Fever", "vote_command": "ChangeMission L4D2C3"},
                        {"display_name": "Hard Rain", "vote_command": "ChangeMission L4D2C4"},
                        {"display_name": "The Parish", "vote_command": "ChangeMission L4D2C5"},
                        {"display_name": "The Passing", "vote_command": "ChangeMission L4D2C6"},
                        {"display_name": "Cold Stream", "vote_command": "ChangeMission L4D2C13"},
                        {"display_name": "The Sacrifice", "vote_command": "ChangeMission L4D2C7"},
                        {"display_name": "No Mercy", "vote_command": "ChangeMission L4D2C8"},
                        {"display_name": "Crash Course", "vote_command": "ChangeMission L4D2C9"},
                        {"display_name": "Death Toll", "vote_command": "ChangeMission L4D2C10"},
                        {"display_name": "Dead Air", "vote_command": "ChangeMission L4D2C11"},
                        {"display_name": "Blood Harvest", "vote_command": "ChangeMission L4D2C12"},
                        {"display_name": "The Last Stand", "vote_command": "ChangeMission L4D2C13"},
                    ],
                },
            },
            "kick_votes": {
                "display_name": "Kick Votes",
                "available_votes": [
                    {"display_name": "Kick 1", "vote_command": "Kick 1"},
                    {"display_name": "Kick 2", "vote_command": "Kick 2"},
                    {"display_name": "Kick 3", "vote_command": "Kick 3"},
                    {"display_name": "Kick 4", "vote_command": "Kick 4"},
                    {"display_name": "Kick 5", "vote_command": "Kick 5"},
                    {"display_name": "Kick 10", "vote_command": "Kick 10"},
                    {"display_name": "Kick 15", "vote_command": "Kick 15"},
                    {"display_name": "Kick 20", "vote_command": "Kick 20"},
                ],
            },
            "difficulty_votes": {
                "display_name": "Difficulty Votes",
                "available_votes": [
                    {"display_name": "Difficulty: Impossible", "vote_command": "ChangeDifficulty Impossible"},
                    {"display_name": "Difficulty: Expert", "vote_command": "ChangeDifficulty Expert"},
                    {"display_name": "Difficulty: Hard", "vote_command": "ChangeDifficulty Hard"},
                    {"display_name": "Difficulty: Normal", "vote_command": "ChangeDifficulty Normal"},
                ],
            },
        }

        # create a 'Voting' menu to hold all the sections
        voting_menu = tk.Menu(menubar)

        # iterate over the items in the data dictionary
        for section_name, section in voting_data.items():
            # get the display name and options list for current section
            section_display_name = section["display_name"]
            section_votes = (
                section["available_votes"][self.game.get_version()]
                if section_name == "change_mission"
                else section["available_votes"]
            )

            # create a submenu for the current section
            remove_temp_hud_menu = tk.Menu(voting_menu)
            voting_menu.add_cascade(label=section_display_name, menu=remove_temp_hud_menu)

            # add each option in the current section to the submenu
            for option in section_votes:
                vote_command = option["vote_command"]
                display_name = option["display_name"]
                remove_temp_hud_menu.add_command(
                    label=display_name, command=lambda v=vote_command: self.editor_menu_execute_game_command(v)
                )

        # ----------------------------------
        #       Create Show Panel menu
        # ----------------------------------

        switch_team_data = {
            "Team": {"Spectate": "jointeam 1", "Survivor": "jointeam 2", "Infected": "jointeam 3"},
            "Left 4 Dead": {
                "Bill": "sb_takecontrol Bill",
                "Francis": "sb_takecontrol Francis",
                "Louis": "sb_takecontrol Louis",
                "Zoey": "sb_takecontrol Zoey",
            },
            "Left 4 Dead 2": {
                "Coach": "sb_takecontrol Coach",
                "Nick": "sb_takecontrol Nick",
                "Ellis": "sb_takecontrol Ellis",
                "Rochelle": "sb_takecontrol Rochelle",
            },
        }

        # Create Switch submenu
        switch_menu = tk.Menu(menubar)

        # Add divider between each section
        switch_menu.add_separator()

        # Add Team, Left 4 Dead, and Left 4 Dead 2 options to root menu
        for game, options in switch_team_data.items():
            switch_menu.add_command(label=game, state="disabled")
            switch_menu.add_separator()
            for character, value in options.items():
                switch_menu.add_command(
                    label=character, command=lambda v=value: self.editor_menu_execute_game_command(v)
                )
            # Add divider between each section
            switch_menu.add_separator()

        # ----------------------------------
        #       Create Show Panel menu
        # ----------------------------------

        show_panel_dict = {
            "general": {
                "Sacrifice Failed": "info_window",
                "Tab Scoreboard": "scores",
                "Spectating Hud": "Specgui",
                "Versus spawn tutorial": "spawnmode",
                "MOTD": "info",
                "Team Switching Panel": "team",
                "Transition Screen": "transition_stats",
                "Versus Shut Down": "vs_shutting_down",
                "Versus TooFar": "debug_zombie_panel -1",
                "Versus BecomeTank": "debug_zombie_panel 1",
                "Versus OtherBecomeTank": "debug_zombie_panel 2",
                "Hide versus TooFar/Tank panel": "debug_zombie_panel 0",
            },
            "L4D1": {
                "Versus smoker tutorial": "spawn_smoker",
                "Versus hunter tutorial": "spawn_hunter",
                "Versus boomer tutorial": "spawn_boomer",
                "Survival Scoreboard End Of Round": "fullscreen_holdout_scoreboard",
                "Survival Shutting Down": "holdout_shutting_down",
                "Versus Scoreboard End Of Round": "multimap_vs_scoreboard",
            },
            "L4D2": {
                "Versus/Scavenge Rematch Hud": "fullscreen_scavenge_scoreboard",
                "Versus Scoreboard End of Match": "fullscreen_vs_results",
                "Versus Scoreboard End of Round": "fullscreen_vs_scoreboard",
                "Versus/Scavenge round start timer": "ready_countdown",
                "Survival Scoreboard": "fullscreen_survival_scoreboard",
                "Survival Shut Down": "survival_shutting_down",
            },
        }

        # Create general menu and add common options
        show_panel_menu = tk.Menu(menubar, tearoff=0)
        for key, value in show_panel_dict["general"].items():
            show_panel_menu.add_command(
                label=key, command=self.create_lambda_command(self.editor_menu_show_panel, value)
            )

        # Check GAME_VERSION to determine which L4D-specific options to add
        if self.game.get_version() == "L4D1":
            show_panel_game_version_data = show_panel_dict.get("L4D1", {})
        elif self.game.get_version() == "L4D2":
            show_panel_game_version_data = show_panel_dict.get("L4D2", {})
        else:
            show_panel_game_version_data = {}

        # Add L4D-specific options to general menu
        for key, value in show_panel_game_version_data.items():
            show_panel_menu.add_command(
                label=key, command=self.create_lambda_command(self.editor_menu_show_panel, value)
            )

        # ----------------------------------
        #       Create give items menu
        # ----------------------------------

        give_items_dict = {
            "Everything": "give_all_items",
            "Guns": "give_all_guns",
            "Melee weapons": "give_all_melee_weapons",
            "Pickups": "give_all_pickups",
        }

        # Add a "Give Items" menu item with sub-items for each item in the dictionary
        give_items_menu = tk.Menu(menubar, tearoff=False)
        for label, action in give_items_dict.items():
            give_items_menu.add_command(label=label, command=lambda action=action: self.editor_give_items(action))

        # ----------------------------------
        #       Create clipboard menu
        # ----------------------------------

        clipboard_menu = Menu(menubar, tearoff=0)

        for file_name in os.listdir(SNIPPETS_DIR):
            file_path = os.path.join(SNIPPETS_DIR, file_name)
            if os.path.isfile(file_path):
                menu_name = os.path.splitext(file_name)[0]
                clipboard_menu.add_command(
                    label=menu_name, command=self.create_lambda_command(self.editor_menu_copy_snippet, file_path)
                )

        # ----------------------------------
        #       Create load hud menu
        # ----------------------------------

        load_hud_menu = Menu(menubar, tearoff=0)

        # stored huds
        stored_huds_submenu = tk.Menu(menubar, tearoff=0)
        remove_stored_hud_menu = tk.Menu(menubar, tearoff=0)
        load_hud_menu.add_cascade(label="Stored", menu=stored_huds_submenu)

        # stored huds - root
        load_hud_menu.add_separator()
        for hud_dir in self.persistent_data["stored_huds"]:
            hud_name = retrieve_hud_name_for_dir(hud_dir)
            load_hud_menu.add_command(
                label=hud_name,
                command=self.create_lambda_command(self.editor_edit_hud, hud_dir),
            )
            remove_stored_hud_menu.add_command(
                label=hud_name, command=self.create_lambda_command(self.editor_remove_stored_hud, hud_dir)
            )
        # stored huds - submenu - add stored hud
        stored_huds_submenu.add_command(label="Add", command=self.editor_add_existing_hud)
        # stored huds - submenu - remove stored hud
        stored_huds_submenu.add_cascade(label="Remove", menu=remove_stored_hud_menu)
        if not self.persistent_data["stored_huds"]:
            stored_huds_submenu.entryconfigure("Remove", state="disabled")
        load_hud_menu.add_separator()

        # temp huds
        temp_huds_submenu = tk.Menu(menubar, tearoff=0)
        remove_temp_hud_menu = tk.Menu(menubar, tearoff=0)
        load_hud_menu.add_cascade(label="Temporary", menu=temp_huds_submenu)

        # stored huds - root
        load_hud_menu.add_separator()
        for hud_dir in self.persistent_data["stored_temp_huds"]:
            hud_name = retrieve_hud_name_for_dir(hud_dir)
            load_hud_menu.add_command(
                label=hud_name,
                command=self.create_lambda_command(self.editor_edit_hud, hud_dir),
            )
            remove_temp_hud_menu.add_command(
                label=hud_name, command=self.create_lambda_command(self.editor_remove_temp_hud, hud_dir)
            )
        # stored huds - submenu - add temp hud
        temp_huds_submenu.add_command(label="Open", command=self.editor_open_temp_hud)
        # stored huds - submenu - remove temp hud
        temp_huds_submenu.add_cascade(label="Remove", menu=remove_temp_hud_menu)
        if not self.persistent_data["stored_temp_huds"]:
            temp_huds_submenu.entryconfigure("Remove", state="disabled")

        load_hud_menu.add_separator()

        # ----------------------------------
        #       Parent tools menu
        # ----------------------------------

        self.tools_menu = tk.Menu(menubar, tearoff=0)
        self.tools_menu.add_command(label="Inspect", command=self.editor_inspect_hud)
        self.tools_menu.add_command(label="Chat Debug (WWWW)", command=self.editor_chat_debug_spam_w)
        self.tools_menu.add_command(label="Hide World", command=self.editor_hide_game_world)
        self.tools_menu.add_cascade(label="Clipboard", menu=clipboard_menu)

        # ----------------------------------
        #       Parent File menu
        # ----------------------------------

        self.file_menu = tk.Menu(menubar, tearoff=0)
        self.file_menu.add_command(label="Start", command=self.editor_open_hud_select)
        self.file_menu.add_command(label="Browser", command=self.editor_open_hud_browser)
        self.file_menu.add_separator()
        self.file_menu.add_cascade(label="Help", menu=helpmenu)
        self.file_menu.add_command(label="Exit", command=self.editor_exit_script)
        self.file_menu.add_command(label="Open", state="disabled", columnbreak=True)
        self.file_menu.add_separator()
        self.file_menu.add_command(
            label="Game", command=self.create_lambda_command(self.editor_open_folder, self.game.get_dir("dev"))
        )
        self.file_menu.add_command(
            label="Script", command=self.create_lambda_command(self.editor_open_folder, SCRIPT_DIR)
        )
        self.file_menu.add_cascade(label="Hud", menu=load_hud_menu)

        # ----------------------------------
        #       Parent Tools menu
        # ----------------------------------

        self.debug_menu = tk.Menu(menubar, tearoff=0)
        self.debug_menu.add_command(label="Game cmd", command=self.editor_prompt_game_command)
        self.debug_menu.add_cascade(label="Show panel", menu=show_panel_menu)
        self.debug_menu.add_cascade(label="Call vote", menu=voting_menu)
        self.debug_menu.add_cascade(label="Switch", menu=switch_menu)
        self.debug_menu.add_cascade(label="Give items", menu=give_items_menu)
        self.debug_menu.add_cascade(label="Tools", menu=self.tools_menu)

        # ----------------------------------
        #       Parent Game menu
        # ----------------------------------

        self.game_menu.add_cascade(label="Position", menu=self.game_pos_menu)
        self.game_menu.add_cascade(label="Resolution", menu=game_res_menu)
        self.game_menu.add_cascade(label="Map", menu=game_map_menu)
        self.game_menu.add_cascade(label="Mode", menu=self.game_mode_menu)

        self.editor_menu_game_insecure_checkmark = tk.BooleanVar()
        self.game_menu.add_checkbutton(
            label="Insecure",
            variable=self.editor_menu_game_insecure_checkmark,
            command=self.editor_menu_game_toggle_insecure,
            columnbreak=True,
        )

        self.editor_menu_game_mute_checkmark = tk.BooleanVar()
        self.game_menu.add_checkbutton(
            label="Muted", variable=self.editor_menu_game_mute_checkmark, command=self.editor_menu_game_toggle_mute
        )
        self.game_menu.add_command(label="Restart", columnbreak=False, command=self.editor_menu_game_restart)
        self.game_menu.add_command(label="Close", columnbreak=False, command=self.editor_menu_game_close)

        # ----------------------------------
        #       Parent menu
        # ----------------------------------

        menubar.add_cascade(label="File", menu=self.file_menu)
        menubar.add_cascade(label="Hud", menu=self.hud_menu)
        menubar.add_cascade(label="Mode", menu=self.reload_mode_menu)
        menubar.add_cascade(label="Debug", menu=self.debug_menu)
        menubar.add_cascade(label="Game", menu=self.game_menu)
        self.root.config(menu=menubar)

    def editor_menu_game_mode(self, mode):
        """Method to handle the selected game mode in the menu."""
        # Implement the logic to handle the selected game mode here
        print(f"The selected option is: {mode}")

        for mode_entry, var in self.game_mode_vars.items():
            if mode_entry == mode:
                var.set(True)
            else:
                var.set(False)

    def editor_menu_game_map(self, map_name, map_code):
        """Method to handle the selected game map in the menu."""
        print(f"The code for {map_name} is {map_code}.")

    def editor_menu_game_resolution(self, resolution):
        """Method to handle the selected game resolution in the menu."""
        print(f"Selected resolution: {resolution}")

    def editor_menu_game_pos(self, pos):
        """Method to handle the selected game position in the menu."""
        print(f"Selected Game Position: {pos}")

        self.persistent_data["game_pos"] = pos

        for pos_entry, var in self.game_pos_vars.items():
            if pos_entry == pos:
                var.set(True)
            else:
                var.set(False)

    def editor_menu_game_toggle_insecure(self):
        """Method to handle the selected secure/insecure option in the menu."""
        print("editor_menu_game_security")

        # toggle setting
        if self.persistent_data["game_insecure"] is True:
            self.persistent_data["game_insecure"] = False
            self.editor_menu_game_insecure_checkmark.set(0)
            # self.game_menu.entryconfig("Unmute", label="Mute")
        else:
            self.persistent_data["game_insecure"] = True
            self.editor_menu_game_insecure_checkmark.set(1)
            # self.game_menu.entryconfig("Mute", label="Unmute")

        # prompt to restart game
        message = "Restart needed for changes to take effect.\n\nDo you want to restart now?"
        if messagebox.askyesno("Restart Game", message):
            self.editor_menu_game_restart()

    def editor_menu_game_close(self):
        """Method to handle the selected secure/insecure option in the menu."""
        self.game.close()

    def editor_menu_game_restart(self):
        """Method to handle the selected secure/insecure option in the menu."""
        self.hud.stop_game_exit_check()
        self.game.close()
        self.game.run("dev")
        self.hud.start_game_exit_check()

    def editor_menu_game_toggle_mute(self):
        """Method to handle the selected secure/insecure option in the menu."""
        if self.persistent_data["game_mute"] is True:
            self.persistent_data["game_mute"] = False
            self.game.command.execute("volume 1")
            self.editor_menu_game_mute_checkmark.set(0)
            # self.game_menu.entryconfig("Unmute", label="Mute")
        else:
            self.persistent_data["game_mute"] = True
            self.game.command.execute("volume 0")
            self.editor_menu_game_mute_checkmark.set(1)
            # self.game_menu.entryconfig("Mute", label="Unmute")

    def editor_menu_copy_snippet(self, file_path):
        """Copy snippet to clipboard"""
        with open(file_path, "r", encoding="utf-8") as file:
            content = file.read()
            pyperclip.copy(content)
            print(content)

    def editor_menu_show_panel(self, panel):
        """Show selected panel ingame"""
        # Do something with the panel value (e.g. print it)
        print(panel)

    def editor_menu_execute_game_command(self, execute_command):
        """Execute selected command ingame"""
        # Do something with the panel value (e.g. print it)
        print(f"todo: execute {execute_command}")

    def editor_give_items(self, action):
        """TODO: probably redirect the give items menu to editor_menu_execute_command"""
        # Define the function to be called when a menu item is selected
        print(f"Executing action '{action}'")

    def editor_add_existing_hud(self):
        """Add exiting hud to the menu"""
        prompt_add_existing_hud(self.persistent_data)
        self.create_and_refresh_menu()

    def editor_remove_stored_hud(self, hud_dir):
        """Remove existing hud"""
        remove_stored_hud(self.persistent_data, hud_dir)
        self.create_and_refresh_menu()

    def editor_remove_temp_hud(self, hud_dir):
        """Remove existing hud"""
        print(f"todo: {hud_dir}")
        remove_temp_hud(self.persistent_data, hud_dir)
        self.create_and_refresh_menu()

    def editor_open_temp_hud(self):
        """Open temporary hud in the menu"""
        prompt_open_temp_hud(self.persistent_data)
        self.create_and_refresh_menu()

    def editor_edit_hud(self, hud_dir):
        """Start editing selected hud"""
        print(f"todo: {hud_dir}")

    def editor_exit_script(self):
        """Exit script"""
        print("editor_exit_script: todo")

    def editor_open_hud_select(self):
        """Open hud select gui"""
        print("editor_open_hud_select: todo")

    def editor_open_hud_browser(self):
        """Open hud browser"""
        print("editor_open_hud_browser: todo")

    def editor_open_folder(self, input_dir):
        """Open folder"""
        print(f"editor_open_folder todo: {input_dir}")

    def editor_open_folder_in_vscode(self, input_dir):
        """Open folder"""
        print(f"editor_open_folder_in_vscode todo: {input_dir}")

    def editor_prompt_game_command(self):
        """Prompt & execute game command"""
        print("editor_prompt_game_command")

    def editor_inspect_hud(self):
        """Show inspect hud gui (vgui_drawtree)"""
        print("editor_inspect_hud")

    def editor_chat_debug_spam_w(self):
        """Spam W's to debug chat"""
        print("editor_chat_debug_spam_w")

    def editor_hide_game_world(self):
        """Hide game world"""
        print("Hide game world")

    def editor_unsync_hud(self):
        """Unsync hud"""
        print("editor_unsync_hud")

    def editor_save_as_vpk(self):
        """Export hud as vpk"""
        print("editor_save_as_vpk")

    def editor_save_as_folder(self):
        """Export hud as folder"""
        print("editor_save_as_folder")

    def editor_menu_reload_click(self):
        """Toggle reload click coordinate"""
        print("editor_save_as_folder")
        self.persistent_data["reload_mouse_clicks_enabled"] = not self.persistent_data["reload_mouse_clicks_enabled"]
        self.reload_mode_menu_coord_clicks_checkmark.set(self.persistent_data["reload_mouse_clicks_enabled"])
        self.create_and_refresh_menu()
        print(self.persistent_data["reload_mouse_clicks_enabled"])

    def editor_menu_reload_click_coord1(self):
        """Set reload click coordinate"""
        print("editor_menu_reload_click_coord1")

    def editor_menu_reload_click_coord2(self):
        """Set reload click coordinate"""
        print("editor_menu_reload_click_coord2")

    def editor_menu_send_keys(self, keys):
        """Send input keys to game"""
        print(f"editor_menu_send_keys: {keys}")


def debug_gui_editor_menu(persistent_data, game_instance, hud_instance):
    """Debug gui class"""
    # pylint: disable=unused-variable
    app = GuiEditorMenu(persistent_data, game_instance, hud_instance)

"""Module for the """
import os
import tkinter as tk
from tkinter import Menu, PhotoImage
from tkinter import messagebox
import webbrowser
import keyboard
import pyperclip
from modules.utils.constants import SNIPPETS_DIR, IMAGES_DIR, SCRIPT_DIR, TUTORIALS_DIR

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
        self.create_menu()
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

    def do_nothing(self):
        """
        A dummy function that does nothing.
        """
        print("Do nothing")

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

    def create_menu(self):
        """
        Creates the menu bar for the application with three cascading menus: File, Edit, and Help.
        """
        menubar = Menu(self.root)

        # Create the image object for the Open icon
        self.open_icon = PhotoImage(file=os.path.join(IMAGES_DIR, "folder.png")).subsample(2, 2)

        # ----------------------------------
        #       Create parent menus
        # ----------------------------------

        self.game_menu = tk.Menu(menubar, tearoff=0)
        self.tool_menu = tk.Menu(menubar, tearoff=0)

        # ----------------------------------
        #       Create file menu
        # ----------------------------------

        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label="New", command=self.do_nothing)
        filemenu.add_command(label="Open", image=self.open_icon, compound=tk.LEFT, command=self.do_nothing)
        filemenu.add_command(label="Save", command=self.do_nothing)
        filemenu.add_command(label="Save as...", command=self.do_nothing)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=self.root.quit)

        # ----------------------------------
        #       Create edit menu
        # ----------------------------------

        editmenu = Menu(menubar, tearoff=0)
        editmenu.add_command(label="Undo", command=self.do_nothing)
        editmenu.add_separator()
        editmenu.add_command(label="Cut", command=self.do_nothing)
        editmenu.add_command(label="Copy", command=self.do_nothing)
        editmenu.add_command(label="Paste", command=self.do_nothing)
        editmenu.add_command(label="Delete", command=self.do_nothing)
        editmenu.add_command(label="Select All", command=self.do_nothing)

        # ----------------------------------
        #       Create Game Mode menu
        # ----------------------------------

        game_modes = ["Coop", "Survival", "Versus", "Scavenge"]
        self.game_mode_menu = tk.Menu(menubar, tearoff=0)
        self.game_mode_vars = {}
        for mode in game_modes:
            self.game_mode_vars[mode] = tk.BooleanVar()
            self.game_mode_menu.add_checkbutton(
                label=mode,
                variable=self.game_mode_vars[mode],
                onvalue=True,
                offvalue=False,
                command=lambda mode=mode: self.editor_menu_game_mode(mode),
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
        game_map_menu.add_command(
            label="Curling Stadium",
            command=lambda: self.editor_menu_game_map("Curling Stadium", "curling_stadium"),
        )
        game_map_menu.add_command(
            label="Tutorial Standards",
            command=lambda: self.editor_menu_game_map("Tutorial Standards", "tutorial_standards"),
        )
        game_map_menu.add_command(
            label="Hud Dev Map",
            command=lambda: self.editor_menu_game_map("Hud Dev Map", "hud_dev_map"),
        )

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
        #       Create clipboard menu
        # ----------------------------------

        clipboardmenu = Menu(menubar, tearoff=0)

        for file_name in os.listdir(SNIPPETS_DIR):
            file_path = os.path.join(SNIPPETS_DIR, file_name)
            if os.path.isfile(file_path):
                menu_name = os.path.splitext(file_name)[0]
                clipboardmenu.add_command(
                    label=menu_name, command=self.create_lambda_command(self.editor_menu_copy_snippet, file_path)
                )

        # ----------------------------------
        #       Parent Main menu
        # ----------------------------------

        menubar.add_cascade(label="File", menu=filemenu)
        filemenu.add_cascade(label="Help", menu=helpmenu)
        menubar.add_cascade(label="Tools", menu=self.tool_menu)
        self.tool_menu.add_cascade(label="Clipboard", menu=clipboardmenu)
        self.tool_menu.add_cascade(label="Show panel", menu=show_panel_menu)
        menubar.add_cascade(label="Edit", menu=editmenu)
        menubar.add_cascade(label="Game", menu=self.game_menu)

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
        #       Add the menu to the gui
        # ----------------------------------

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


def debug_gui_editor_menu(persistent_data, game_instance, hud_instance):
    """Debug gui class"""
    # pylint: disable=unused-variable
    app = GuiEditorMenu(persistent_data, game_instance, hud_instance)

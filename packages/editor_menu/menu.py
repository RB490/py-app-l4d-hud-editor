# pylint: disable=attribute-defined-outside-init
"""Module containing editor menu methods for GuiEditorMenu to keep things organized"""

import os
import tkinter as tk
from tkinter import Menu, PhotoImage
import webbrowser
from packages.editor_menu.handler import EditorMenuHandler
from packages.game.game import Game
from packages.utils.constants import (
    EDITOR_HUD_RELOAD_MODES,
    GAME_POSITIONS,
    MAP_CODES,
    SNIPPETS_DIR,
    IMAGES_DIR,
    SCRIPT_DIR,
    TUTORIALS_DIR,
)
from packages.utils.functions import (
    retrieve_hud_name_for_dir,
)


class EditorMenuClass:
    """Class containing editor menu methods for GuiEditorMenu to keep things organized

    using this in the main gui because a context menu hotkey doesn't work right in python"""

    def __init__(
        self, child_instance, root, persistent_data, hud_instance, browser_instance
    ):
        self.handler = EditorMenuHandler(
            self, persistent_data, hud_instance, browser_instance
        )
        self.root = root
        self.child_instance = child_instance
        self.persistent_data = persistent_data
        self.game = Game()
        self.hud = hud_instance

        self.open_icon = PhotoImage(file=os.path.join(IMAGES_DIR, "folder.png")).subsample(2, 2)

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

    def create_lambda_command(self, func, *args):
        # pylint: disable=line-too-long
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
                label=map_name, command=self.create_lambda_command(self.handler.editor_menu_game_map, map_name, map_code)
            )
            > so when this menu entry is selected self.handler.editor_menu_game_map gets called with map_name and map_code

        This method is useful for creating a function on-the-fly that takes no arguments
        but still needs to execute some code with certain values or variables.
        By using a lambda function created by `create_lambda_function`,
        you can defer binding the arguments until later when needed.
        This technique is also known as partial evaluation or currying,
        and it is commonly used in functional programming.
        """
        return lambda: func(*args)

    def create_game_map_menu(self, menubar):
        """Create game map menu"""

        self.game_map_menu = tk.Menu(menubar, tearoff=0)
        # self.game_map_menu = tk.Menu(self.game_menu, tearoff=0)

        if os.path.exists(os.path.join(IMAGES_DIR, "Left 4 Dead small grayscale.png")):
            print("The directory path exists.")
        else:
            print("The directory path does not exist or is invalid.")

        self.map_menu_l4d1_icon = PhotoImage(
            # file=os.path.join(IMAGES_DIR, "cross128.png")
            file=os.path.join(IMAGES_DIR, "Left 4 Dead small grayscale.png")
        ).subsample(1, 1)
        # self.map_menu_l4d2_icon = PhotoImage(
        #     file=os.path.join(IMAGES_DIR, "Left 4 Dead 2 small grayscale.png")
        # ).subsample(1, 1)

        self.map_menu_l4d2_icon = PhotoImage(file=os.path.join(IMAGES_DIR, "Left 4 Dead 2 small grayscale.png"))

        # main menu
        self.game_map_menu.add_command(
            label="Main Menu",
            command=self.handler.editor_menu_disconnect,
        )
        self.game_map_menu.add_separator()

        # misc maps
        self.game_map_menu.add_command(
            label="Hud Dev Map",
            command=lambda: self.handler.editor_menu_game_map("Hud Dev Map", "hud_dev_map"),
        )
        if self.game.get_version() is "L4D2":
            self.game_map_menu.add_command(
                label="Curling Stadium",
                command=lambda: self.handler.editor_menu_game_map("Curling Stadium", "curling_stadium"),
            )
        self.game_map_menu.add_command(
            label="Tutorial Standards",
            command=lambda: self.handler.editor_menu_game_map("Tutorial Standards", "tutorial_standards"),
        )
        self.game_map_menu.add_separator()

        # Create the L4D1 and L4D2 submenus
        map_menu_l4d1 = tk.Menu(self.game_map_menu, tearoff=0)
        map_menu_l4d2 = tk.Menu(self.game_map_menu, tearoff=0)
        self.game_map_menu.add_cascade(
            label="L4D1",
            menu=map_menu_l4d1,
            # image=self.map_menu_l4d1_icon,
            compound=tk.LEFT,
        )
        self.game_map_menu.add_cascade(
            label="L4D2",
            menu=map_menu_l4d2,
            # image=self.map_menu_l4d2_icon,
            # image=test_obj.map_menu_l4d2_icon,
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
                    label=map_name,
                    command=self.create_lambda_command(self.handler.editor_menu_game_map, map_name, map_code),
                )

    def create_game_res_menu(self, menubar):
        """Create game resolution menu"""

        self.game_res_menu = tk.Menu(menubar, tearoff=0)
        res_4_3_menu = tk.Menu(self.game_res_menu, tearoff=0)
        res_16_9_menu = tk.Menu(self.game_res_menu, tearoff=0)
        res_16_10_menu = tk.Menu(self.game_res_menu, tearoff=0)

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
            res_4_3_menu.add_command(label=res, command=lambda r=res: self.handler.editor_menu_game_resolution(r))

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
            res_16_9_menu.add_command(label=res, command=lambda r=res: self.handler.editor_menu_game_resolution(r))

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
            res_16_10_menu.add_command(label=res, command=lambda r=res: self.handler.editor_menu_game_resolution(r))

        self.game_res_menu.add_cascade(label="4:3", menu=res_4_3_menu)
        self.game_res_menu.add_cascade(label="16:9", menu=res_16_9_menu)
        self.game_res_menu.add_cascade(label="16:10", menu=res_16_10_menu)

    def create_game_pos_menu(self, menubar):
        """Create game position menu"""
        self.game_pos_menu = tk.Menu(menubar, tearoff=0)
        self.game_pos_vars = {}
        for pos in GAME_POSITIONS:
            self.game_pos_vars[pos] = tk.BooleanVar()
            self.game_pos_menu.add_checkbutton(
                label=pos,
                variable=self.game_pos_vars[pos],
                onvalue=True,
                offvalue=False,
                command=lambda pos=pos: self.handler.editor_menu_game_pos(pos),
            )
        self.game_pos_vars[self.persistent_data["game_pos"]].set(True)

    def create_game_mode_menu(self, menubar):
        """Create game mode menu"""

        game_modes = ["Coop", "Survival", "Versus", "Scavenge"]
        self.game_mode_menu = tk.Menu(menubar, tearoff=0)
        self.game_mode_vars = {}
        for game_mode in game_modes:
            self.game_mode_vars[game_mode] = tk.BooleanVar()
            self.game_mode_menu.add_checkbutton(
                label=game_mode,
                variable=self.game_mode_vars[game_mode],
                onvalue=True,
                offvalue=False,
                command=lambda mode=game_mode: self.handler.editor_menu_game_mode(mode),
            )
        self.game_mode_vars[self.persistent_data["game_mode"]].set(True)

    def create_game_menu(self, menubar):
        """Create game menu"""

        self.game_menu = tk.Menu(menubar, tearoff=0)
        self.create_game_mode_menu(menubar)
        self.create_game_res_menu(menubar)
        self.create_game_map_menu(menubar)
        self.create_game_pos_menu(menubar)

    def create_hud_menu(self, menubar):
        """Create hud menu"""

        self.hud_menu = tk.Menu(menubar, tearoff=0)
        self.hud_menu.add_command(label="<hud_name>", state="disabled")
        if self.hud.get_dir():
            self.hud_menu.entryconfigure(0, label=retrieve_hud_name_for_dir(self.hud.get_dir()))
        self.hud_menu.add_command(label="Unsync", command=self.handler.editor_unsync_hud)
        self.hud_menu.add_command(label="Save", state="disabled")
        self.hud_menu.add_command(label="VPK", command=self.handler.editor_save_as_vpk)
        self.hud_menu.add_command(label="Folder", command=self.handler.editor_save_as_folder)
        self.hud_menu.add_command(label="Open", state="disabled", columnbreak=True)
        self.hud_menu.add_command(
            label="Hud", command=self.create_lambda_command(self.handler.editor_open_folder, self.hud.get_dir())
        )
        self.hud_menu.add_command(
            label="Hud (VS)",
            command=self.create_lambda_command(self.handler.editor_open_folder_in_vscode, self.hud.get_dir()),
        )

    def create_load_hud_menu(self, menubar):
        """Create load hud menu"""

        self.load_hud_menu = Menu(menubar, tearoff=0)

        # stored huds
        stored_huds_submenu = tk.Menu(menubar, tearoff=0)
        remove_stored_hud_menu = tk.Menu(menubar, tearoff=0)
        self.load_hud_menu.add_cascade(label="Stored", menu=stored_huds_submenu)

        # stored huds - root
        self.load_hud_menu.add_separator()
        for hud_dir in self.persistent_data["stored_huds"]:
            hud_name = retrieve_hud_name_for_dir(hud_dir)
            self.load_hud_menu.add_command(
                label=hud_name,
                command=self.create_lambda_command(self.handler.editor_edit_hud, hud_dir),
            )
            remove_stored_hud_menu.add_command(
                label=hud_name, command=self.create_lambda_command(self.handler.editor_remove_stored_hud, hud_dir)
            )
        # stored huds - submenu - add stored hud
        stored_huds_submenu.add_command(label="Add", command=self.handler.editor_add_existing_hud)
        # stored huds - submenu - remove stored hud
        stored_huds_submenu.add_cascade(label="Remove", menu=remove_stored_hud_menu)
        if not self.persistent_data["stored_huds"]:
            stored_huds_submenu.entryconfigure("Remove", state="disabled")
        self.load_hud_menu.add_separator()

        # temp huds
        temp_huds_submenu = tk.Menu(menubar, tearoff=0)
        remove_temp_hud_menu = tk.Menu(menubar, tearoff=0)
        self.load_hud_menu.add_cascade(label="Temporary", menu=temp_huds_submenu)

        # stored huds - root
        self.load_hud_menu.add_separator()
        for hud_dir in self.persistent_data["stored_temp_huds"]:
            hud_name = retrieve_hud_name_for_dir(hud_dir)
            self.load_hud_menu.add_command(
                label=hud_name,
                command=self.create_lambda_command(self.handler.editor_edit_hud, hud_dir),
            )
            remove_temp_hud_menu.add_command(
                label=hud_name, command=self.create_lambda_command(self.handler.editor_remove_temp_hud, hud_dir)
            )
        # stored huds - submenu - add temp hud
        temp_huds_submenu.add_command(label="Open", command=self.handler.editor_open_temp_hud)
        # stored huds - submenu - remove temp hud
        temp_huds_submenu.add_cascade(label="Remove", menu=remove_temp_hud_menu)
        if not self.persistent_data["stored_temp_huds"]:
            temp_huds_submenu.entryconfigure("Remove", state="disabled")

        self.load_hud_menu.add_separator()

    def create_voting_menu(self, menubar):
        """Create call vote menu"""

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
        self.voting_menu = tk.Menu(menubar)

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
            remove_temp_hud_menu = tk.Menu(self.voting_menu)
            self.voting_menu.add_cascade(label=section_display_name, menu=remove_temp_hud_menu)

            # add each option in the current section to the submenu
            for option in section_votes:
                vote_command = option["vote_command"]
                display_name = option["display_name"]
                remove_temp_hud_menu.add_command(
                    label=display_name, command=lambda v=vote_command: self.handler.editor_menu_execute_game_command(v)
                )

    def create_show_panel_menu(self, menubar):
        """Create show panel menu"""

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
        self.show_panel_menu = tk.Menu(menubar, tearoff=0)
        for key, value in show_panel_dict["general"].items():
            self.show_panel_menu.add_command(
                label=key, command=self.create_lambda_command(self.handler.editor_menu_show_panel, value)
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
            self.show_panel_menu.add_command(
                label=key, command=self.create_lambda_command(self.handler.editor_menu_show_panel, value)
            )

    def create_switch_team_menu(self, menubar):
        """Create switch team menu"""

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
        self.switch_menu = tk.Menu(menubar)

        # Add divider between each section
        self.switch_menu.add_separator()

        # Add Team, Left 4 Dead, and Left 4 Dead 2 options to root menu
        for game, options in switch_team_data.items():
            self.switch_menu.add_command(label=game, state="disabled")
            self.switch_menu.add_separator()
            for character, value in options.items():
                self.switch_menu.add_command(
                    label=character, command=lambda v=value: self.handler.editor_menu_execute_game_command(v)
                )
            # Add divider between each section
            self.switch_menu.add_separator()

    def create_hotkeys_menu(self, menubar):
        """Create hotkeys menu"""

        self.hotkeys_menu = Menu(menubar)
        self.hotkeys_menu.add_command(label="Global")
        self.hotkeys_menu.entryconfig("Global", state="disabled")
        self.hotkeys_menu.add_separator()
        self.hotkeys_menu.add_command(label="Sync Hud", accelerator="Ctrl+S")
        self.hotkeys_menu.add_command(label="Show Menu", accelerator="F4")
        self.hotkeys_menu.add_command(label="Browse Files", accelerator="F8")
        self.hotkeys_menu.add_separator()
        self.hotkeys_menu.add_command(label="In-Game")
        self.hotkeys_menu.entryconfig("In-Game", state="disabled")
        self.hotkeys_menu.add_separator()
        self.hotkeys_menu.add_command(label="Load Dead Center finale", accelerator="O")
        self.hotkeys_menu.add_command(label="Play credits (On a finale level)", accelerator="P")
        self.hotkeys_menu.add_command(label="Noclip", accelerator="G")
        self.hotkeys_menu.add_command(label="Pause", accelerator="F8")
        self.hotkeys_menu.add_command(label="Admin system menu", accelerator="N")
        self.hotkeys_menu.add_command(label="Slow-mo game speed", accelerator="F9")
        self.hotkeys_menu.add_command(label="Default game speed", accelerator="F10")
        self.hotkeys_menu.add_command(label="Last game cmd", accelerator="F11")
        # self.help_menu.add_cascade(label="Hotkeys", menu=self.hotkeys_menu)

    def create_help_menu(self, menubar):
        """Create help menu"""

        # doodleLink = "http://doodlesstuff.com/?p=tf2hud"
        doodle_link = "https://web.archive.org/web/20221023012414/https://doodlesstuff.com/?p=tf2hud"
        flame_path = os.path.join(TUTORIALS_DIR, "Flame's Guide to HUDs - flamehud by StefanB.pdf")
        doodle_path = os.path.join(TUTORIALS_DIR, "TF2 Hud Editing Guide - DoodlesStuff.mhtml")
        readme_path = os.path.join(SCRIPT_DIR, "README.MD")
        if self.game.get_title() is "Left 4 Dead":
            all_cvars_link = "https://developer.valvesoftware.com/wiki/List_of_L4D_Cvars"
        else:
            all_cvars_link = "https://developer.valvesoftware.com/wiki/List_of_L4D2_Cvars"

        self.help_menu = Menu(menubar, tearoff=0)
        self.help_menu.add_cascade(label="Hotkeys", menu=self.hotkeys_menu)
        self.help_menu.add_command(label="Script Readme", command=lambda: self.open_file(readme_path))
        self.help_menu.add_command(label="All Game Commands", command=lambda: self.open_url(all_cvars_link))
        self.help_menu.add_separator()
        self.help_menu.add_command(label="Tutorials")
        self.help_menu.entryconfig("Tutorials", state="disabled")
        self.help_menu.add_command(
            label="TF2 Hud Editing Guide - DoodlesStuff (link)", command=lambda: self.open_url(doodle_link)
        )
        self.help_menu.add_command(
            label="TF2 Hud Editing Guide - DoodlesStuff (file)", command=lambda: self.open_file(doodle_path)
        )
        self.help_menu.add_command(
            label="Flame's Guide to HUDs - flamehud by StefanB", command=lambda: self.open_file(flame_path)
        )

    def create_reload_mode_menu(self, menubar):
        """Create reload mode menu"""
        self.reload_mode_menu = tk.Menu(menubar, tearoff=0)
        reload_once_menu = tk.Menu(menubar, tearoff=0)

        self.reload_mode_menu.add_command(label="Modes", state="disabled")
        self.reload_mode_menu.add_separator()

        # reload mode setting
        for reload_mode, reload_code in EDITOR_HUD_RELOAD_MODES.items():
            self.reload_mode_menu.add_command(
                label=reload_mode, command=self.create_lambda_command(self.do_nothing, f"reload_{reload_code.lower()}")
            )

        self.reload_mode_menu.add_command(label="Options", state="disabled", columnbreak=True)
        self.reload_mode_menu.add_separator()

        # reload once menu
        for reload_mode, reload_code in EDITOR_HUD_RELOAD_MODES.items():
            reload_once_menu.add_command(
                label=reload_mode, command=self.create_lambda_command(self.do_nothing, f"reload_{reload_code.lower()}")
            )

        # reload options
        self.reload_mode_menu.add_cascade(label="Once", menu=reload_once_menu)
        self.reload_mode_menu_coord_clicks_checkmark = tk.BooleanVar()
        self.reload_mode_menu.add_checkbutton(
            label="Reload clicks",
            variable=self.reload_mode_menu_coord_clicks_checkmark,
            command=self.handler.editor_menu_reload_click,
        )
        self.reload_mode_menu_coord_clicks_checkmark.set(self.persistent_data["reload_mouse_clicks_enabled"])
        self.reload_mode_menu.add_command(label="Coord 1", command=self.handler.editor_menu_reload_click_coord1)
        self.reload_mode_menu.add_command(label="Coord 2", command=self.handler.editor_menu_reload_click_coord2)

        self.reload_mode_menu_reopen_menu_checkmark = tk.BooleanVar()
        self.reload_mode_menu_reopen_menu_checkmark.set(self.persistent_data["reload_reopen_menu_on_reload"])
        self.reload_mode_menu.add_checkbutton(
            label="Reopen menu on reload",
            variable=self.reload_mode_menu_reopen_menu_checkmark,
            command=self.handler.editor_menu_reload_reopen_menu,
        )

    def create_clipboard_menu(self, menubar):
        """Create give items menu"""

        self.clipboard_menu = Menu(menubar, tearoff=0)

        for file_name in os.listdir(SNIPPETS_DIR):
            file_path = os.path.join(SNIPPETS_DIR, file_name)
            if os.path.isfile(file_path):
                menu_name = os.path.splitext(file_name)[0]
                self.clipboard_menu.add_command(
                    label=menu_name,
                    command=self.create_lambda_command(self.handler.editor_menu_copy_snippet, file_path),
                )

    def create_give_items_menu(self, menubar):
        """Create give items menu"""

        give_items_dict = {
            "Everything": "give_all_items",
            "Guns": "give_all_guns",
            "Melee weapons": "give_all_melee_weapons",
            "Pickups": "give_all_pickups",
        }

        # Add a "Give Items" menu item with sub-items for each item in the dictionary
        self.give_items_menu = tk.Menu(menubar, tearoff=False)
        for label, action in give_items_dict.items():
            self.give_items_menu.add_command(
                label=label, command=lambda action=action: self.handler.editor_give_items(action)
            )

    def create_and_refresh_menu(self):
        """
        Creates the menu bar for the application with three cascading menus: File, Edit, and Help.
        """
        self.menu_bar = Menu(self.root, tearoff=False)

        self.create_reload_mode_menu(self.menu_bar)
        self.create_hud_menu(self.menu_bar)
        self.create_game_menu(self.menu_bar)
        self.create_load_hud_menu(self.menu_bar)
        self.create_voting_menu(self.menu_bar)
        self.create_show_panel_menu(self.menu_bar)
        self.create_switch_team_menu(self.menu_bar)
        self.create_hotkeys_menu(self.menu_bar)
        self.create_help_menu(self.menu_bar)
        self.create_give_items_menu(self.menu_bar)
        self.create_clipboard_menu(self.menu_bar)

        # ----------------------------------
        #       Parent tools menu
        # ----------------------------------

        self.tools_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.editor_menu_inspect_hud_checkmark = tk.BooleanVar()
        self.tools_menu.add_checkbutton(
            label="Inspect",
            variable=self.editor_menu_inspect_hud_checkmark,
            command=self.handler.editor_inspect_hud,
            columnbreak=False,
        )
        self.tools_menu.add_command(label="Chat Debug (WWWW)", command=self.handler.editor_chat_debug_spam_w)

        # self.tools_menu.add_command(label="Hide World", command=self.handler.editor_hide_game_world)
        self.editor_menu_hide_world_checkmark = tk.BooleanVar()
        self.tools_menu.add_checkbutton(
            label="Hide world",
            variable=self.editor_menu_hide_world_checkmark,
            command=self.handler.editor_hide_game_world,
            columnbreak=False,
        )

        self.tools_menu.add_cascade(label="Clipboard", menu=self.clipboard_menu)

        # ----------------------------------
        #       Parent File menu
        # ----------------------------------

        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.file_menu.add_command(label="Start", command=self.handler.editor_open_hud_select)
        self.file_menu.add_command(label="Browser", command=self.handler.editor_open_hud_browser)
        self.file_menu.add_separator()
        self.file_menu.add_cascade(label="Help", menu=self.help_menu)
        self.file_menu.add_command(label="Close", command=self.handler.editor_finish_editing)
        self.file_menu.add_command(label="Exit", command=self.handler.editor_exit_script)
        self.file_menu.add_command(label="Open", state="disabled", columnbreak=True)
        self.file_menu.add_separator()
        self.file_menu.add_command(
            label="Game", command=self.create_lambda_command(self.handler.editor_open_folder, self.game.get_dir("dev"))
        )
        self.file_menu.add_command(
            label="Script", command=self.create_lambda_command(self.handler.editor_open_folder, SCRIPT_DIR)
        )
        self.file_menu.add_cascade(label="Hud", menu=self.load_hud_menu)

        # ----------------------------------
        #       Parent Tools menu
        # ----------------------------------

        self.debug_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.debug_menu.add_command(label="Game cmd", command=self.handler.editor_prompt_game_command)
        self.debug_menu.add_cascade(label="Show panel", menu=self.show_panel_menu)
        self.debug_menu.add_cascade(label="Call vote", menu=self.voting_menu)
        self.debug_menu.add_cascade(label="Switch", menu=self.switch_menu)
        self.debug_menu.add_cascade(label="Give items", menu=self.give_items_menu)
        self.debug_menu.add_cascade(label="Tools", menu=self.tools_menu)

        # ----------------------------------
        #       Parent Game menu
        # ----------------------------------

        self.game_menu.add_cascade(label="Position", menu=self.game_pos_menu)
        self.game_menu.add_cascade(label="Resolution", menu=self.game_res_menu)
        self.game_menu.add_cascade(label="Map", menu=self.game_map_menu)
        self.game_menu.add_cascade(label="Mode", menu=self.game_mode_menu)

        self.editor_menu_game_insecure_checkmark = tk.BooleanVar()
        self.game_menu.add_checkbutton(
            label="Insecure",
            variable=self.editor_menu_game_insecure_checkmark,
            command=self.handler.editor_menu_game_toggle_insecure,
            columnbreak=True,
        )

        self.editor_menu_game_mute_checkmark = tk.BooleanVar()
        self.game_menu.add_checkbutton(
            label="Muted",
            variable=self.editor_menu_game_mute_checkmark,
            command=self.handler.editor_menu_game_toggle_mute,
        )
        if self.persistent_data["game_mute"]:
            self.editor_menu_game_mute_checkmark.set(1)
        else:
            self.editor_menu_game_mute_checkmark.set(0)
        self.game_menu.add_command(label="Restart", columnbreak=False, command=self.handler.editor_menu_game_restart)
        self.game_menu.add_command(label="Close", columnbreak=False, command=self.handler.editor_menu_game_close)

        # ----------------------------------
        #       Parent menu
        # ----------------------------------

        self.menu_bar.add_cascade(label="File", menu=self.file_menu)
        self.menu_bar.add_cascade(label="Hud", menu=self.hud_menu)
        self.menu_bar.add_cascade(label="Mode", menu=self.reload_mode_menu)
        self.menu_bar.add_cascade(label="Game", menu=self.game_menu)
        self.menu_bar.add_cascade(label="Debug", menu=self.debug_menu)
        # self.menu_bar.add_command(label="Close", command=self.do_nothing) # useful when displaying popup
        self.root.config(menu=self.menu_bar)

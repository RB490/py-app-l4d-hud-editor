# pylint: disable=attribute-defined-outside-init, broad-exception-caught, too-many-lines
"""Module containing editor menu methods for GuiEditorMenu to keep things organized"""

import os
import tkinter as tk
import webbrowser
from tkinter import Menu, PhotoImage

from loguru import logger

from game.constants import DirectoryMode
from game.game import Game
from menu.handler import EditorMenuHandler
from shared_utils.shared_utils import add_empty_menu_separator, create_lambda_command
from utils.constants import (
    EDITOR_HUD_RELOAD_MODES,
    GAME_POSITIONS,
    HOTKEY_EDITOR_MENU,
    HOTKEY_SYNC_HUD,
    HOTKEY_TOGGLE_BROWSER,
    IMAGES_DIR_MISC,
    MAP_CODES,
    PROJECT_ROOT,
    SNIPPETS_DIR,
    TUTORIALS_DIR,
    ImageConstants,
)
from utils.persistent_data_manager import PersistentDataManager


class EditorMenuClass:
    """Class containing editor menu methods for GuiEditorMenu to keep things organized

    using this in the main gui because a context menu hotkey doesn't work right in python"""

    def __init__(self, parent_instance, parent_root):
        self.data_manager = PersistentDataManager()
        self.handler = EditorMenuHandler(self)
        self.root = parent_root
        self.parent = parent_instance
        self.img = ImageConstants()
        self.game = Game()
        # pylint: disable=import-outside-toplevel # importing outside top level to avoid circular imports

        from hud.hud import Hud

        self.hud = Hud()
        self.create_and_refresh_menu()

    def open_file(self, path):
        """Open file"""
        logger.debug("Opening file: {path}")
        os.startfile(path)

    def open_url(self, url):
        """Open url"""
        webbrowser.open(url)
        logger.debug("Opening URL: {url}")

    def do_nothing(self, *args):
        # pylint: disable=unused-argument, unnecessary-pass
        """
        A dummy function that does nothing.
        """
        pass

    def create_game_map_menu(self, menubar):
        """Create game map menu"""

        self.game_map_menu = tk.Menu(menubar, tearoff=0)
        # self.game_map_menu = tk.Menu(self.game_menu, tearoff=0)

        self.map_menu_l4d1_icon = PhotoImage(
            # file=BIG_CROSS_ICON
            file=os.path.join(IMAGES_DIR_MISC, "left_4_dead_small_grayscale.png")
        ).subsample(1, 1)
        # self.map_menu_l4d2_icon = PhotoImage(
        #     file=os.path.join(IMAGES_DIR, "Left 4 Dead 2 small grayscale.png")
        # ).subsample(1, 1)

        self.map_menu_l4d2_icon = PhotoImage(file=os.path.join(IMAGES_DIR_MISC, "left_4_dead_2_small_grayscale.png"))

        # main menu
        self.game_map_menu.add_command(
            label="Main Menu",
            command=self.handler.editor_menu_disconnect,
            image=self.img.black_map_folded_paper_symbol,
            compound="left",
        )
        self.game_map_menu.add_separator()

        # misc maps
        self.game_map_menu.add_command(
            label="Hud Dev Map",
            command=lambda: self.handler.editor_menu_game_map("Hud Dev Map", "hud_dev_map"),
            image=self.img.black_map_folded_paper_symbol,
            compound="left",
        )
        if self.game.get_version() == "L4D2":
            self.game_map_menu.add_command(
                label="Curling Stadium",
                image=self.img.black_map_folded_paper_symbol,
                compound="left",
                command=lambda: self.handler.editor_menu_game_map("Curling Stadium", "curling_stadium"),
            )
        self.game_map_menu.add_command(
            label="Tutorial Standards",
            image=self.img.black_map_folded_paper_symbol,
            compound="left",
            command=lambda: self.handler.editor_menu_game_map("Tutorial Standards", "tutorial_standards"),
        )
        self.game_map_menu.add_separator()

        # Create the L4D1 and L4D2 submenus
        map_menu_l4d1 = tk.Menu(self.game_map_menu, tearoff=0)
        map_menu_l4d2 = tk.Menu(self.game_map_menu, tearoff=0)
        self.game_map_menu.add_cascade(
            label="L4D1",
            menu=map_menu_l4d1,
            image=self.img.black_map_folded_paper_symbol,
            compound=tk.LEFT,
        )
        self.game_map_menu.add_cascade(
            label="L4D2",
            menu=map_menu_l4d2,
            image=self.img.black_map_folded_paper_symbol,
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
                map_menu_l4d1.add_cascade(
                    label=campaign,
                    image=self.img.black_map_folded_paper_symbol,
                    compound=tk.LEFT,
                    menu=campaign_submenu,
                )
            else:
                campaign_submenu = tk.Menu(map_menu_l4d2, tearoff=0)
                map_menu_l4d2.add_cascade(
                    label=campaign,
                    image=self.img.black_map_folded_paper_symbol,
                    compound=tk.LEFT,
                    menu=campaign_submenu,
                )

            # Add each map to the campaign submenu
            for map_info in maps:
                map_name = map_info["name"]
                map_code = map_info["code"]
                campaign_submenu.add_command(
                    label=map_name,
                    command=create_lambda_command(self.handler.editor_menu_game_map, map_name, map_code),
                    image=self.img.black_map_folded_paper_symbol,
                    compound=tk.LEFT,
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
            res_4_3_menu.add_command(
                label=res,
                image=self.img.monitor_black_tool,
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
                image=self.img.monitor_black_tool,
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
                image=self.img.monitor_black_tool,
                compound="left",
                command=create_lambda_command(self.handler.editor_menu_game_resolution, res),
            )

        self.game_res_menu.add_cascade(
            label="4:3", image=self.img.monitor_black_tool, compound="left", menu=res_4_3_menu
        )
        self.game_res_menu.add_cascade(
            label="16:9", image=self.img.monitor_black_tool, compound="left", menu=res_16_9_menu
        )
        self.game_res_menu.add_cascade(
            label="16:10", image=self.img.monitor_black_tool, compound="left", menu=res_16_10_menu
        )

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
                command=create_lambda_command(self.handler.editor_menu_game_pos, pos),
                image=self.img.two_opposite_diagonal_arrows_in_black_square,
                compound="left",
            )
        game_pos = self.data_manager.get("game_pos")
        self.game_pos_vars[game_pos].set(True)

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
                command=create_lambda_command(self.handler.editor_menu_game_mode, game_mode),
                image=self.img.switch_black_solid_symbol,
                compound="left",
            )
        game_mode = self.data_manager.get("game_mode")
        self.game_mode_vars[game_mode].set(True)

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
        if self.hud.edit.is_synced():
            self.hud_menu.entryconfigure(0, label=self.hud.manager.retrieve_hud_name_for_dir(self.hud.edit.get_dir()))
        self.hud_menu.add_separator()
        self.hud_menu.add_command(
            label=f"Sync ({HOTKEY_SYNC_HUD})",
            image=self.img.arrows_couple_counterclockwise_rotating_symbol,
            compound="left",
            command=self.handler.editor_sync_hud,
        )
        self.hud_menu.add_command(
            label="Unsync",
            image=self.img.arrows_couple_counterclockwise_rotating_symbol,
            compound="left",
            command=self.handler.editor_unsync_hud,
        )
        self.hud_menu.add_command(
            label="Close",
            image=self.img.cross_black_circular_button,
            compound="left",
            command=self.handler.editor_close_hud,
        )
        self.hud_menu.add_separator()
        self.hud_menu.add_command(label="Save", state="disabled")
        self.hud_menu.add_separator()
        self.hud_menu.add_command(
            label="VPK",
            image=self.img.save_black_diskette_interface_symbol,
            compound="left",
            command=self.handler.editor_save_as_vpk,
        )
        self.hud_menu.add_command(
            label="Folder",
            image=self.img.save_black_diskette_interface_symbol,
            compound="left",
            command=self.handler.editor_save_as_folder,
        )
        self.hud_menu.add_command(label="Open", state="disabled", columnbreak=True)
        self.hud_menu.add_separator()
        self.hud_menu.add_command(
            label="Hud",
            command=create_lambda_command(self.handler.editor_open_folder, self.hud.edit.get_dir()),
            image=self.img.folder_black_interface_symbol,
            compound="left",
        )
        self.hud_menu.add_command(
            label="Hud (VS Code)",
            command=create_lambda_command(self.handler.editor_open_folder_in_vscode, self.hud.edit.get_dir()),
            image=self.img.vs_code,
            compound="left",
        )

        # disable items when no hud is loaded
        # try:except added try except incase no hud is loaded TODO do i want to keep this
        try:
            if not self.hud.edit.is_synced():
                for i in range(self.hud_menu.index("end") + 1):
                    self.hud_menu.entryconfigure(i, state="disabled")
        except Exception:
            pass

    def create_load_hud_menu(self, menubar):
        """Create load hud menu"""

        self.load_hud_menu = Menu(menubar, tearoff=0)

        #######################################################################
        # stored huds
        #######################################################################
        stored_huds_submenu = tk.Menu(menubar, tearoff=0)
        remove_stored_hud_menu = tk.Menu(menubar, tearoff=0)
        self.load_hud_menu.add_cascade(
            label="Stored",
            image=self.img.right_arrow_curved_black_symbol,
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
                image=self.img.paintbrush_design_tool_interface_symbol,
                compound="left",
            )
            remove_stored_hud_menu.add_command(
                label=hud_name,
                image=self.img.minus_big_symbol,
                compound="left",
                command=create_lambda_command(self.handler.editor_remove_stored_hud, hud_dir),
            )
        # stored huds - submenu - add stored hud
        stored_huds_submenu.add_command(
            label="New",
            image=self.img.star_black_fivepointed_shape_symbol,
            compound="left",
            command=self.handler.editor_create_new_hud,
        )
        # stored huds - submenu - create new stored hud
        stored_huds_submenu.add_command(
            label="Add",
            image=self.img.addition_sign,
            compound="left",
            command=self.handler.editor_add_existing_hud,
        )
        # stored huds - submenu - remove stored hud
        stored_huds_submenu.add_cascade(
            label="Remove", image=self.img.minus_big_symbol, compound="left", menu=remove_stored_hud_menu
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
            image=self.img.right_arrow_curved_black_symbol,
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
                image=self.img.paintbrush_design_tool_interface_symbol,
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
            image=self.img.addition_sign,
            compound="left",
            command=self.handler.editor_open_temp_hud,
        )
        # stored huds - submenu - remove temp hud
        temp_huds_submenu.add_cascade(
            label="Remove", image=self.img.minus_big_symbol, compound="left", menu=remove_temp_hud_menu
        )
        if not self.data_manager.get("stored_temp_huds"):
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

        # Choose an image to use for all items from the provided list
        selected_image = self.img.verify_black_square_interface_button_symbol

        # iterate over the items in the data dictionary
        for section_name, section in voting_data.items():
            # get the display name and options list for the current section
            section_display_name = section["display_name"]
            section_votes = (
                section["available_votes"][self.game.get_version()]
                if section_name == "change_mission"
                else section["available_votes"]
            )

            # create a submenu for the current section
            remove_temp_hud_menu = tk.Menu(self.voting_menu)
            self.voting_menu.add_cascade(
                label=section_display_name,
                image=selected_image,  # Set the selected image for the cascade label
                compound="left",  # Set the image on the left side
                menu=remove_temp_hud_menu,
            )

            # add each option in the current section to the submenu
            for option in section_votes:
                vote_command = option["vote_command"]
                display_name = option["display_name"]

                # Check if the image is available in the list before using it
                if selected_image is not None:
                    remove_temp_hud_menu.add_command(
                        label=display_name,
                        image=selected_image,  # Use the selected image for all items
                        compound="left",  # Set the image on the left side
                        command=create_lambda_command(self.handler.editor_menu_execute_game_command, vote_command),
                    )
                else:
                    remove_temp_hud_menu.add_command(
                        label=display_name,
                        command=create_lambda_command(self.handler.editor_menu_execute_game_command, vote_command),
                    )

    def create_show_panel_menu(self, menubar):
        """Create show panel menu"""

        show_panel_dict = {
            "general": {
                "None": "None",
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
        self.show_panel_menu_selected_var = tk.BooleanVar()
        self.show_panel_menu = tk.Menu(menubar, tearoff=0)
        for key, value in show_panel_dict["general"].items():
            command = create_lambda_command(self.handler.editor_menu_show_panel, value)

            if value == self.game.command.show_ui_panel:
                self.show_panel_menu.add_checkbutton(
                    label=key,
                    command=command,
                    variable=self.show_panel_menu_selected_var,
                    image=self.img.window_black_rounded_square_interface_symbol,
                    compound="left",
                )
            else:
                self.show_panel_menu.add_command(
                    label=key,
                    command=command,
                    image=self.img.window_black_rounded_square_interface_symbol,
                    compound="left",
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
            command = create_lambda_command(self.handler.editor_menu_show_panel, value)
            if value == self.game.command.show_ui_panel:
                self.show_panel_menu.add_checkbutton(
                    label=key,
                    command=command,
                    variable=self.show_panel_menu_selected_var,
                    image=self.img.window_black_rounded_square_interface_symbol,
                    compound="left",
                )
            else:
                self.show_panel_menu.add_command(
                    label=key,
                    command=command,
                    image=self.img.window_black_rounded_square_interface_symbol,
                    compound="left",
                )

        self.show_panel_menu_selected_var.set(1)

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
                self.switch_menu.add_cascade(
                    label=character,
                    command=create_lambda_command(self.handler.editor_menu_execute_game_command, value),
                    image=self.img.switch_black_solid_symbol,  # Set the selected image for the cascade label
                    compound="left",  # Set the image on the left side
                )

            # Add divider between each section
            self.switch_menu.add_separator()

    def create_hotkeys_menu(self, menubar):
        """Create hotkeys menu"""
        self.hotkeys_menu = Menu(menubar)
        self.hotkeys_menu.add_command(label="Global")
        self.hotkeys_menu.entryconfig("Global", state="disabled")
        self.hotkeys_menu.add_separator()
        self.hotkeys_menu.add_command(
            label="Sync Hud",
            image=self.img.buttons,
            compound="left",
            accelerator=HOTKEY_SYNC_HUD,
        )
        self.hotkeys_menu.add_command(
            label="Browse Files",
            image=self.img.buttons,
            compound="left",
            accelerator=HOTKEY_TOGGLE_BROWSER,
        )
        self.hotkeys_menu.add_command(
            label="Editor Menu",
            image=self.img.buttons,
            compound="left",
            accelerator=HOTKEY_EDITOR_MENU,
        )
        self.hotkeys_menu.add_separator()
        self.hotkeys_menu.add_command(label="In-Game")
        self.hotkeys_menu.entryconfig("In-Game", state="disabled")
        self.hotkeys_menu.add_separator()
        self.hotkeys_menu.add_command(
            label="Load Dead Center finale",
            image=self.img.buttons,
            compound="left",
            accelerator="O",
        )
        self.hotkeys_menu.add_command(
            label="Play credits (On a finale level)",
            image=self.img.buttons,
            compound="left",
            accelerator="P",
        )
        self.hotkeys_menu.add_command(
            label="Noclip",
            image=self.img.buttons,
            compound="left",
            accelerator="G",
        )
        self.hotkeys_menu.add_command(
            label="Pause",
            image=self.img.buttons,
            compound="left",
            accelerator="F8",
        )
        self.hotkeys_menu.add_command(
            label="Admin system menu",
            image=self.img.buttons,
            compound="left",
            accelerator="N",
        )
        self.hotkeys_menu.add_command(
            label="Slow-mo game speed",
            image=self.img.buttons,
            compound="left",
            accelerator="F9",
        )
        self.hotkeys_menu.add_command(
            label="Default game speed",
            image=self.img.buttons,
            compound="left",
            accelerator="F10",
        )
        self.hotkeys_menu.add_command(
            label="Last game cmd",
            image=self.img.buttons,
            compound="left",
            accelerator="F11",
        )

    def create_help_menu(self, menubar):
        """Create help menu"""

        # doodleLink = "http://doodlesstuff.com/?p=tf2hud"
        doodle_link = "https://web.archive.org/web/20221023012414/https://doodlesstuff.com/?p=tf2hud"
        flame_path = os.path.join(TUTORIALS_DIR, "Flame's Guide to HUDs - flamehud by StefanB.pdf")
        doodle_path = os.path.join(TUTORIALS_DIR, "TF2 Hud Editing Guide - DoodlesStuff.mhtml")
        readme_path = os.path.join(PROJECT_ROOT, "README.MD")
        if self.game.get_title() == "Left 4 Dead":
            all_cvars_link = "https://developer.valvesoftware.com/wiki/List_of_L4D_Cvars"
        else:
            all_cvars_link = "https://developer.valvesoftware.com/wiki/List_of_L4D2_Cvars"

        self.help_menu = Menu(menubar, tearoff=0)

        # help
        self.help_menu.add_command(label="Help", state="disabled")
        self.help_menu.add_separator()
        self.help_menu.add_command(
            label=f"{self.game.get_title()} Commands",
            image=self.img.link,
            compound="left",
            command=lambda: self.open_url(all_cvars_link),
        )
        self.help_menu.add_command(
            label="Script Readme",
            image=self.img.file_black_rounded_symbol_1,
            compound="left",
            command=lambda: self.open_file(readme_path),
        )
        self.help_menu.add_cascade(
            label="Hotkeys",
            image=self.img.buttons,
            compound="left",
            menu=self.hotkeys_menu,
        )
        self.help_menu.add_separator()

        # tutorials
        self.help_menu.add_command(label="Tutorials", state="disabled")
        self.help_menu.add_command(
            label="TF2 Hud Editing Guide - DoodlesStuff",
            image=self.img.link,
            compound="left",
            command=lambda: self.open_url(doodle_link),
        )
        self.help_menu.add_command(
            label="TF2 Hud Editing Guide - DoodlesStuff",
            image=self.img.file_black_rounded_symbol_1,
            compound="left",
            command=lambda: self.open_file(doodle_path),
        )
        self.help_menu.add_command(
            label="Flame's Guide to HUDs - flamehud by StefanB",
            image=self.img.file_black_rounded_symbol_1,
            compound="left",
            command=lambda: self.open_file(flame_path),
        )
        self.help_menu.add_separator()

        # update
        self.help_menu.add_command(label="Update", state="disabled")
        self.help_menu.add_separator()
        self.help_menu.add_cascade(
            label="About",
            image=self.img.star_black_fivepointed_shape_symbol,
            compound="left",
            command=self.handler.editor_show_about_menu,
        )

        return self.help_menu

    def create_reload_mode_menu(self, menubar):
        """Create reload mode menu"""
        self.reload_mode_menu = tk.Menu(menubar, tearoff=0)
        reload_once_menu = tk.Menu(menubar, tearoff=0)

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
                image=self.img.arrows_couple_counterclockwise_rotating_symbol,
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
                image=self.img.arrows_couple_counterclockwise_rotating_symbol,
                compound="left",
            )

        # reload options
        self.reload_mode_menu_reopen_menu_checkmark = tk.BooleanVar()
        self.reload_mode_menu_reopen_menu_checkmark.set(self.data_manager.get("reload_reopen_menu_on_reload"))
        self.reload_mode_menu.add_checkbutton(
            label="Reopen menu on reload",
            variable=self.reload_mode_menu_reopen_menu_checkmark,
            command=self.handler.editor_menu_reload_reopen_menu,
            image=self.img.arrows_couple_counterclockwise_rotating_symbol,
            compound="left",
        )
        self.reload_mode_menu_coord_clicks_checkmark = tk.BooleanVar()
        self.reload_mode_menu.add_checkbutton(
            label="Reload clicks",
            variable=self.reload_mode_menu_coord_clicks_checkmark,
            command=self.handler.editor_menu_reload_click,
            image=self.img.arrows_couple_counterclockwise_rotating_symbol,
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
            image=self.img.arrows_couple_counterclockwise_rotating_symbol,
            compound="left",
            command=self.handler.editor_menu_reload_click_coord1,
        )
        self.reload_mode_menu.add_command(
            label=label_coord_2,
            image=self.img.arrows_couple_counterclockwise_rotating_symbol,
            compound="left",
            command=self.handler.editor_menu_reload_click_coord2,
        )
        self.reload_mode_menu.add_cascade(
            label="Once",
            menu=reload_once_menu,
            image=self.img.arrows_couple_counterclockwise_rotating_symbol,
            compound="left",
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
                    command=create_lambda_command(self.handler.editor_menu_copy_snippet, file_path),
                    image=self.img.clipboard_black_square_interface_symbol,
                    compound="left",
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
                label=label,
                command=create_lambda_command(self.handler.editor_give_items, action),
            )

    def create_developer_installer_menu(self, menubar):
        """Create developer installer menu"""

        # Create the menu
        self.dev_install_menu = tk.Menu(menubar, tearoff=0)

        # Directory Actions
        # -----------------
        self.dev_install_menu.add_command(label="Open Directory", state=tk.DISABLED, command=lambda: None)
        self.dev_install_menu.add_separator()

        self.dev_install_menu.add_command(
            label="User",
            image=self.img.folder_black_interface_symbol,
            compound=tk.LEFT,
            command=self.handler.editor_installer_open_user_dir,
        )

        self.dev_install_menu.add_command(
            label="Dev",
            image=self.img.folder_black_interface_symbol,
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
            image=self.img.paintbrush_design_tool_interface_symbol,
            compound=tk.LEFT,
            command=self.handler.editor_installer_enable_dev_mode,
        )

        disable_dev_mode_menu_name = DirectoryMode.USER.name
        self.dev_install_menu.add_command(
            label=disable_dev_mode_menu_name,
            image=self.img.cup_trophy_silhouette,
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
        #     label=currently_active_mode_name, image=self.img.link, compound=tk.LEFT, state=tk.DISABLED
        # )

        # Empty Separator
        add_empty_menu_separator(self.dev_install_menu)

        # Installation Actions
        # ---------------------
        self.dev_install_menu.add_command(label="Installation", state=tk.DISABLED, command=lambda: None)
        self.dev_install_menu.add_separator()

        self.dev_install_menu.add_command(
            label="Install",
            image=self.img.paintbrush_design_tool_interface_symbol,
            compound=tk.LEFT,
            command=self.handler.editor_installer_install,
        )

        self.dev_install_menu.add_command(
            label="Update",
            image=self.img.arrows_couple_counterclockwise_rotating_symbol,
            compound=tk.LEFT,
            command=self.handler.editor_installer_update,
        )

        self.dev_install_menu.add_command(
            label="Repair",
            image=self.img.wrench_black_silhouette,
            compound=tk.LEFT,
            command=self.handler.editor_installer_repair,
        )

        self.dev_install_menu.add_separator()

        self.dev_install_menu.add_command(
            label="Remove",
            image=self.img.trash_can_black_symbol,
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

    def get_context_menu_dev(self):
        """Retrieve developer installer menu (for adding it to a context menu for example)"""
        self.create_and_refresh_menu(is_context_menu=True)
        return self.dev_install_menu

    def get_context_menu_main(self):
        """Retrieve developer installer menu (for adding it to a context menu for example)"""
        self.create_and_refresh_menu(is_context_menu=True)
        return self.main_menu

    def get_context_menu_help(self):
        """Retrieve developer installer menu (for adding it to a context menu for example)"""
        self.create_and_refresh_menu(is_context_menu=True)
        return self.help_menu

    def get_main_menu(self):
        """Retrieve main menu (for adding as menu bar)"""
        # this line is replaced by 'editor_menu_refresh' in 'create_and_refresh_menu'
        #       self.create_and_refresh_menu(is_context_menu=False)

        return self.main_menu

    def create_and_refresh_menu(self, is_context_menu=False):
        """
        Creates the menu bar for the application
        if not is_context_menu:
        """
        logger.debug("Refreshing editor menu!")

        self.data_manager.save()

        self.main_menu = Menu(self.root, tearoff=False)

        self.create_reload_mode_menu(self.main_menu)
        self.create_hud_menu(self.main_menu)
        self.create_game_menu(self.main_menu)
        self.create_load_hud_menu(self.main_menu)
        self.create_voting_menu(self.main_menu)
        self.create_show_panel_menu(self.main_menu)
        self.create_switch_team_menu(self.main_menu)
        self.create_hotkeys_menu(self.main_menu)
        self.create_help_menu(self.main_menu)
        self.create_give_items_menu(self.main_menu)
        self.create_clipboard_menu(self.main_menu)
        self.create_developer_installer_menu(self.main_menu)

        # ----------------------------------
        #       Parent tools menu
        # ----------------------------------

        self.tools_menu = tk.Menu(self.main_menu, tearoff=0)
        self.editor_menu_inspect_hud_checkmark = tk.BooleanVar()
        self.tools_menu.add_checkbutton(
            label="Inspect",
            variable=self.editor_menu_inspect_hud_checkmark,
            command=self.handler.editor_inspect_hud,
            columnbreak=False,
            image=self.img.plus_sign_on_zoom_magnifier,
            compound="left",
        )
        self.editor_menu_hide_world_checkmark = tk.BooleanVar()
        self.tools_menu.add_checkbutton(
            label="Hide world",
            variable=self.editor_menu_hide_world_checkmark,
            command=self.handler.editor_hide_game_world,
            columnbreak=False,
            image=self.img.minus_big_symbol,
            compound="left",
        )
        self.tools_menu.add_command(
            label="Chat Debug (WWWW)",
            image=self.img.chat_oval_black_interface_symbol_with_text_lines,
            compound="left",
            command=self.handler.editor_chat_debug_spam_w,
            columnbreak=True,
        )
        self.tools_menu.add_cascade(
            label="Clipboard",
            image=self.img.clipboard_black_square_interface_symbol,
            compound="left",
            menu=self.clipboard_menu,
        )

        # ----------------------------------
        #       Parent File menu
        # ----------------------------------

        self.file_menu = tk.Menu(self.main_menu, tearoff=0)
        self.file_menu.add_command(
            label="Start",
            image=self.img.flag_black_cutted_shape,
            compound="left",
            command=self.handler.editor_open_start_gui,
        )
        if is_context_menu:
            self.file_menu.add_command(
                label="Browser",
                image=self.img.book_black_opened_symbol,
                compound="left",
                command=self.handler.editor_open_browser_gui,
            )
        # self.file_menu.add_cascade( # doesn't really make any sense to have an installer option in here
        #     label="Installer", image=self.img.wrench_black_silhouette, compound="left", menu=self.dev_install_menu
        # )
        self.file_menu.add_separator()
        self.file_menu.add_cascade(label="Help", image=self.img.questionmark, compound="left", menu=self.help_menu)
        self.file_menu.add_command(
            label="Close",
            image=self.img.cross_black_circular_button,
            compound="left",
            command=self.handler.editor_finish_editing,
        )
        self.file_menu.add_command(
            label="Exit",
            image=self.img.cross_black_circular_button,
            compound="left",
            command=self.handler.editor_save_and_exit_script,
        )
        self.file_menu.add_command(label="Open", state="disabled", columnbreak=True)
        self.file_menu.add_separator()
        self.file_menu.add_command(
            label="Game",
            command=create_lambda_command(self.handler.editor_open_folder, self.game.dir.get(DirectoryMode.DEVELOPER)),
            image=self.img.folder_black_interface_symbol,
            compound="left",
        )
        self.file_menu.add_command(
            label="Script",
            command=create_lambda_command(self.handler.editor_open_folder, PROJECT_ROOT),
            image=self.img.folder_black_interface_symbol,
            compound="left",
        )
        self.file_menu.add_cascade(
            label="Hud",
            image=self.img.paintbrush_design_tool_interface_symbol,
            compound="left",
            menu=self.load_hud_menu,
        )

        # ----------------------------------
        #       Parent Tools menu
        # ----------------------------------

        self.debug_menu = tk.Menu(self.main_menu, tearoff=0)
        self.debug_menu.add_command(
            label="Game cmd", command=self.handler.editor_prompt_game_command, image=self.img.game_alt, compound="left"
        )
        self.debug_menu.add_cascade(
            label="Show panel",
            menu=self.show_panel_menu,
            image=self.img.window_black_rounded_square_interface_symbol,
            compound="left",
        )
        self.debug_menu.add_cascade(
            label="Call vote",
            menu=self.voting_menu,
            image=self.img.verify_black_square_interface_button_symbol,
            compound="left",
        )
        self.debug_menu.add_cascade(
            label="Switch", menu=self.switch_menu, image=self.img.switch_black_solid_symbol, compound="left"
        )
        self.debug_menu.add_cascade(
            label="Give items", menu=self.give_items_menu, image=self.img.giftbox, compound="left"
        )
        self.debug_menu.add_cascade(
            label="Tools", menu=self.tools_menu, image=self.img.wrench_black_silhouette, compound="left"
        )

        # ----------------------------------
        #       Parent Game menu
        # ----------------------------------

        self.game_menu.add_cascade(
            label="Position",
            menu=self.game_pos_menu,
            image=self.img.two_opposite_diagonal_arrows_in_black_square,
            compound="left",
        )
        self.game_menu.add_cascade(
            label="Resolution",
            menu=self.game_res_menu,
            image=self.img.monitor_black_tool,
            compound="left",
        )
        self.game_menu.add_cascade(
            label="Map",
            menu=self.game_map_menu,
            image=self.img.black_map_folded_paper_symbol,
            compound="left",
        )
        self.game_menu.add_cascade(
            label="Mode", menu=self.game_mode_menu, image=self.img.switch_black_solid_symbol, compound="left"
        )

        self.editor_menu_game_insecure_checkmark = tk.BooleanVar()
        self.game_menu.add_checkbutton(
            label="Insecure",
            variable=self.editor_menu_game_insecure_checkmark,
            command=self.handler.editor_menu_game_toggle_insecure,
            columnbreak=True,
            image=self.img.unlocked_padlock,
            compound="left",
        )
        if self.data_manager.get("game_insecure") is True:
            self.editor_menu_game_insecure_checkmark.set(1)
        else:
            self.editor_menu_game_insecure_checkmark.set(0)

        self.editor_menu_game_always_on_top_checkmark = tk.BooleanVar()
        self.game_menu.add_checkbutton(
            label="Topmost",
            variable=self.editor_menu_game_always_on_top_checkmark,
            command=self.handler.editor_menu_game_toggle_always_on_top,
            image=self.img.up_arrow_button,
            compound="left",
        )
        if self.data_manager.get("game_always_on_top") is True:
            self.editor_menu_game_always_on_top_checkmark.set(1)
        else:
            self.editor_menu_game_always_on_top_checkmark.set(0)

        self.editor_menu_game_mute_checkmark = tk.BooleanVar()
        self.game_menu.add_checkbutton(
            label="Muted",
            variable=self.editor_menu_game_mute_checkmark,
            command=self.handler.editor_menu_game_toggle_mute,
            image=self.img.mute_speaker_symbol_of_interface_with_a_cross,
            compound="left",
        )
        if self.data_manager.get("game_mute"):
            self.editor_menu_game_mute_checkmark.set(1)
        else:
            self.editor_menu_game_mute_checkmark.set(0)

        self.game_menu.add_command(
            label="Restart",
            columnbreak=False,
            command=self.handler.editor_menu_game_restart,
            image=self.img.arrows_couple_counterclockwise_rotating_symbol,
            compound="left",
        )
        self.game_menu.add_command(
            label="Close",
            columnbreak=False,
            command=self.handler.editor_menu_game_close,
            image=self.img.cross_black_circular_button,
            compound="left",
        )

        # ----------------------------------
        #       Parent menu
        # ----------------------------------

        if not is_context_menu:
            self.main_menu.add_cascade(label="File", menu=self.file_menu)
            self.main_menu.add_cascade(label="Hud", menu=self.hud_menu)
            self.main_menu.add_cascade(label="Mode", menu=self.reload_mode_menu)
            self.main_menu.add_cascade(label="Game", menu=self.game_menu)
            self.main_menu.add_cascade(label="Debug", menu=self.debug_menu)
        else:
            self.main_menu.add_cascade(
                label="File", image=self.img.file_black_rounded_symbol_1, compound="left", menu=self.file_menu
            )
            self.main_menu.add_cascade(
                label="Hud",
                image=self.img.paintbrush_design_tool_interface_symbol,
                compound="left",
                menu=self.hud_menu,
            )
            self.main_menu.add_cascade(
                label="Mode",
                image=self.img.arrows_couple_counterclockwise_rotating_symbol,
                compound="left",
                menu=self.reload_mode_menu,
            )
            self.main_menu.add_cascade(label="Game", image=self.img.game_alt, compound="left", menu=self.game_menu)
            self.main_menu.add_cascade(
                label="Debug", image=self.img.hot_or_burn_interface_symbol, compound="left", menu=self.debug_menu
            )
            self.main_menu.add_command(
                label="Close (ESC)", image=self.img.cross, compound="left", command=self.do_nothing
            )  # useful when displaying menu as popup

        if not self.hud.edit.get_dir():
            self.main_menu.entryconfig("Hud", state="disabled")

        # call method to update menu
        if (
            self.parent.has_been_run()
            and hasattr(self.parent, "editor_menu_refresh")
            and callable(getattr(self.parent, "editor_menu_refresh"))
        ):
            self.parent.editor_menu_refresh(called_by_editor_menu=True)

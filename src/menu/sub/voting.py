# pylint: disable=attribute-defined-outside-init

import tkinter as tk

from shared_gui.menu_debug import menu_debug_gui
from shared_utils.functions import create_lambda_command

from src.menu.base import EditorMenuBase
from src.utils.constants import GAME_POSITIONS


class MenuVoting(EditorMenuBase):
    """Menu"""

    def __init__(self, editor_menu_instance):
        super().__init__(editor_menu_instance)

    def get(self, menubar):
        """get menu"""

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
        selected_image = self.img.get("verify_black_square_interface_button_symbol.png", 2)

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

        return self.voting_menu


def main():
    """debug"""
    from src.menu.main import EditorMenuClass

    gui = menu_debug_gui()
    editor_menu_instance = EditorMenuClass(gui)
    main_menu = tk.Menu(gui.root, tearoff=True)
    menu = MenuVoting(editor_menu_instance).get(main_menu)
    gui.debug_menu(menu)
    gui.show()


if __name__ == "__main__":
    main()






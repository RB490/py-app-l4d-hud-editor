"Installer prompts"
from game.constants import DirectoryMode
from game.game import Game
from shared_utils.shared_utils import show_message
from utils.functions import get_dir_size_in_gb


def prompt_start(install_type, message_extra=""):
    "Installer prompts"
    game_class = Game()
    install_type = install_type.lower()  # Convert to lowercase

    # verify install type
    valid_modes = ["install", "update", "repair"]
    if install_type not in valid_modes:
        raise ValueError("Invalid mode parameter")

    # create message
    install_type_capitalized = install_type.capitalize()
    title = f"{install_type_capitalized} hud editing for {game_class.get_title()}?"
    disk_space = get_dir_size_in_gb(game_class.dir.get(DirectoryMode.USER))
    message = f"{title}\n\n"
    if message_extra:  # Check if the variable is not empty
        message += f"- {message_extra}\n"  # Add the extra line
    message += (
        "- This can take up to ~30 minutes depending on drive and processor speed\n"
        f"- This will use around {disk_space} of disk space (copy of the game folder)\n"
        "- Keep any L4D games closed during this process\n\n"
        "It is possible to cancel the setup at any time by closing the progress window"
    )

    # prompt message
    response = show_message(message, "yesno", title)  # Using "yesno" type for this confirmation

    return response


def prompt_delete(message_extra=""):
    "Installer prompts"

    game_class = Game()

    # create message
    title = f"Delete developer directory for {game_class.get_title()}?"
    message = f"{title}\n\n"
    message += f"Directory:\n'{game_class.dir.get(DirectoryMode.DEVELOPER)}'"
    if message_extra:  # Check if the variable is not empty
        message += f"\n\n{message_extra}\n"  # Add the extra line

    # prompt message
    response = show_message(message, "yesno", title)  # Using "yesno" type for this confirmation

    return response


def prompt_verify_game():
    "Prompt user to verify game"
    print("Prompting user to verify game")

    game_class = Game()
    game_title = game_class.get_title()
    title = "Verify game files"

    # https://help.steampowered.com/en/faqs/view/0C48-FCBD-DA71-93EB

    message = (
        f"Verify game files for {game_title}\n\n"
        f"Steam -> Right-Click {game_title} -> Properties -> Installed Files -> 'Verify integrity of game files'. "
        "(this is how to do it at time of writing on 2023.09.02. Might differ slightly)\n\n"
        "This will not affect your game installation. Only the copy that was just made\n\n"
        "Are you sure steam has finished verifying AND downloaded any missing files?"
    )

    response = show_message(message, "info", title)  # Using "yesno" type for this confirmation

    if response:
        # Ask a second time - are you really sure?
        confirm_message = (
            f"Are you REALLY sure steam has finished verifying AND" f" downloaded any missing files for {game_title}?"
        )
        response = show_message(confirm_message, "info", title)  # Using "yesno" type for this confirmation

        return response  # Response is already a boolean value
    else:
        return False

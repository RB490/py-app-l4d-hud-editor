"""Debug"""
# pylint: disable=unused-variable
from game.constants import DirectoryMode, InstallationState, SyncState
from game.game import Game


def debug_id_handler():
    "Debug"
    game = Game()

    sync_state = game.dir.id.set_sync_state(DirectoryMode.DEVELOPER, SyncState.FULLY_SYNCED)

    # my_obj = {"mykey1": "value1", "mykey2": "value2", "mykey3": "value3"}
    my_obj = {}
    game.dir.id.set_sync_changes(DirectoryMode.DEVELOPER, my_obj)
    sync_changes = game.dir.id.get_sync_changes(DirectoryMode.DEVELOPER)

    print("finished debug_id_handler")


def test_id_handler():
    "Debug"
    game_class = Game()

    game_id_handler = game_class.dir.id
    # game_class.dir.id.set_path(DirectoryMode.DEVELOPER)

    # Set the ID location for developer directory
    dir_mode = DirectoryMode.DEVELOPER
    game_id_handler.set_path(dir_mode)

    # Set installation state for developer directory
    installation_state = InstallationState.COMPLETED
    game_id_handler.set_installation_state(dir_mode, installation_state)

    # Set sync state for developer directory
    sync_state = SyncState.FULLY_SYNCED
    game_id_handler.set_sync_state(dir_mode, sync_state)

    # Get installation state for developer directory
    retrieved_installation_state = game_id_handler.get_installation_state(dir_mode)
    if retrieved_installation_state:
        print("Retrieved Installation State:", retrieved_installation_state.name)
    else:
        print("Installation State not found.")

    # Get sync state for developer directory
    retrieved_sync_state = game_id_handler.get_sync_state(dir_mode)
    if retrieved_sync_state:
        print("Retrieved Sync State:", retrieved_sync_state.name)
    else:
        print("Sync State not found.")

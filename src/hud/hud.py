"""Methods related to editing a hud"""
# pylint: disable=broad-exception-raised, broad-exception-caught, import-outside-toplevel


import os
import shutil
from shared_utils.functions import Singleton

from src.hud.descriptions import HudDescriptions
from src.utils.constants import DATA_MANAGER, DEVELOPMENT_DIR


class Hud(metaclass=Singleton):
    """Class to manage hud editing"""

    def __init__(self) -> None:
        self.data_manager = DATA_MANAGER
        from src.hud.editor import HudEditor
        from src.hud.manager import HudManager

        self.manager = HudManager()
        self.edit = HudEditor()
        self.desc = HudDescriptions()

def create_hud_debug_workspace():
    # pylint: disable=line-too-long
    """Debugs the hud syncer class"""

    sync_debug_dir = os.path.join(DEVELOPMENT_DIR, "debug", "hud")
    workspace = os.path.join(sync_debug_dir, "workspace")
    if os.path.isdir(workspace):
        shutil.rmtree(workspace)

    source_dir_template = os.path.join(sync_debug_dir, "samples", "tiny", "debug_hud")
    target_dir_template = os.path.join(sync_debug_dir, "samples", "large", "game_dir")
    source_dir_workspace = os.path.join(workspace, "debug_hud")
    target_dir_workspace = os.path.join(workspace, "game_dir")
    shutil.copytree(source_dir_template, source_dir_workspace)
    shutil.copytree(target_dir_template, target_dir_workspace)

def get_hud_debug_instance():
    """Debug the hud class"""
    # pylint: disable=unused-variable

    # debug_hud_dir = os.path.join(DEVELOPMENT_DIR, "debug", "hud", "Workspace", "debug_hud")
    debug_hud_dir = "D:\\projects\\l4d-addons-huds\\4. l4d2-2020HUD\\source"
    h = Hud()

    # set hud info. usually done by __set_hud_info inside the class
    h.edit.hud_dir = debug_hud_dir
    h.edit.hud_name = h.manager.retrieve_hud_name_for_dir(debug_hud_dir)

    return h

def main():
    "debug hud class"
    h = get_hud_debug_instance()
    # result = hud.edit.get_all_files_dict()
    # result = hud.edit.get_files_dict()
    h.edit.start_editing(h.edit.get_dir())
    # h.edit.sync()

if __name__ == "__main__":
    main()
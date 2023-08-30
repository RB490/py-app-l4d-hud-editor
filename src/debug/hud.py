"Debug hud"
# pylint: disable=invalid-name, protected-access
import os
import shutil

from hud.hud import Hud
from utils.constants import DEVELOPMENT_DIR


def get_hud_debug_instance():
    """Debug the hud class"""
    # pylint: disable=unused-variable

    debug_hud_dir = os.path.join(DEVELOPMENT_DIR, "debug", "hud", "Workspace", "debug_hud")
    h = Hud()
    h.edit._set_hud_info(debug_hud_dir)
    return h


def debug_hud():
    """Debug the hud class"""
    print("debug_hud")

    my_hud_instanc = get_hud_debug_instance()
    my_hud_instanc.save_as_folder()
    # my_hud_instanc.start_editing(my_hud_instanc.get_dir())


def create_hud_workspace():
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

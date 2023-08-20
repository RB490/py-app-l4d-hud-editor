"Debug hud"
import os
import shutil

from hud.hud import Hud
from utils.constants import DEVELOPMENT_DIR


def get_hud_debug_instance(persistent_data):
    """Debug the hud class"""
    # pylint: disable=unused-variable

    debug_hud_dir = os.path.join(DEVELOPMENT_DIR, "debug", "hud", "Workspace", "debug_hud")
    i = Hud(persistent_data)
    i.hud_dir = debug_hud_dir
    return i


def debug_hud(persistent_data):
    """Debug the hud class"""
    print("debug_hud")

    my_hud_instanc = get_hud_debug_instance(persistent_data)
    my_hud_instanc.save_as_folder()
    # my_hud_instanc.start_editing(my_hud_instanc.get_dir())


def create_hud_workspace():
    # pylint: disable=line-too-long
    """Debugs the hud syncer class"""

    sync_debug_dir = os.path.join(DEVELOPMENT_DIR, "debug", "hud")
    if os.path.isdir(os.path.join(sync_debug_dir, "workspace")):
        shutil.rmtree(os.path.join(sync_debug_dir, "workspace"))

    source_dir_template = os.path.join(sync_debug_dir, "samples", "tiny", "debug_hud")
    target_dir_template = os.path.join(sync_debug_dir, "samples", "large", "game_dir")
    source_dir_workspace = os.path.join(sync_debug_dir, "workspace", "debug_hud")
    target_dir_workspace = os.path.join(sync_debug_dir, "workspace", "game_dir")
    shutil.copytree(source_dir_template, source_dir_workspace)
    shutil.copytree(target_dir_template, target_dir_workspace)
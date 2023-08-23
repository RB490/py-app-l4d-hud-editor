import os
import shutil

from gui.vdf import VDFModifierGUI
from utils.constants import DEVELOPMENT_DIR
from utils.functions import get_backup_path


def debug_vdf_gui(persistent_data):
    """Debug GUI"""

    # vdf file
    vdf_path = os.path.join(
        DEVELOPMENT_DIR, "debug", "vdf", "tiny_hudlayout - [$X360] nested key-value definition.res"
    )
    # vdf_path = os.path.join(DEVELOPMENT_DIR, "debug", "vdf", "large_scoreboard - [$X360] BackgroundImage Control.res")

    # vdf file backup
    vdf_path_backup = get_backup_path(vdf_path)
    shutil.copy2(vdf_path, vdf_path_backup)

    app = VDFModifierGUI(persistent_data, vdf_path_backup)
    app.run()

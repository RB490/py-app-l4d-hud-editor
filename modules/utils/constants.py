"""Global constant variables"""
import os

# # Get the absolute path of the current directory
# current_dir = os.path.abspath(os.path.dirname(__file__))

# # Navigate up one level to retrieve the parent directory of 'modules'
# parent_dir = os.path.abspath(os.path.join(current_dir, os.pardir))

# # Navigate up one more level to retrieve the parent directory of 'utils'
# grandparent_dir = os.path.abspath(os.path.join(parent_dir, os.pardir))

# print(grandparent_dir)

DEBUG_MODE = True
SCRIPT_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
DEVELOPMENT_DIR = os.path.join(SCRIPT_DIR, "Development")
ASSETS_DIR = os.path.join(SCRIPT_DIR, "assets")
IMAGES_DIR = os.path.join(ASSETS_DIR, "images")
NEW_HUD_DIR = os.path.join(ASSETS_DIR, "new hud template")
MODS_DIR = os.path.join(ASSETS_DIR, "Dependencies", "Mods")
MISC_DIR = os.path.join(ASSETS_DIR, "misc")
EDITOR_AUTOEXEC_PATH = os.path.join(MISC_DIR, "hud_editor_autoexec.cfg")
SCRIPT_NAME = "L4D Hud Editor"
SCRIPT_FILE_NAME = os.path.basename(SCRIPT_DIR)
PERSISTENT_DATA_PATH = SCRIPT_NAME + ".json"
PERSISTENT_DATA = []

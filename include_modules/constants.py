"""Global constant variables"""
import os

DEBUG_MODE = True
SCRIPT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DEVELOPMENT_DIR = os.path.join(SCRIPT_DIR, "Development")
ASSETS_DIR = os.path.join(SCRIPT_DIR, "assets")
IMAGES_DIR = os.path.join(ASSETS_DIR, "images")
NEW_HUD_DIR = os.path.join(ASSETS_DIR, "new hud template")
MODS_DIR = os.path.join(ASSETS_DIR, "Dependencies", "Mods")
SCRIPT_NAME = "L4D Hud Editor"
SCRIPT_FILE_NAME = os.path.basename(SCRIPT_DIR)
PERSISTENT_DATA_PATH = SCRIPT_NAME + ".json"
PERSISTENT_DATA = []

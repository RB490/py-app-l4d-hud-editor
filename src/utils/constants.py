"""Global constant variables"""
import os
from enum import Enum, auto

# core
DEBUG_MODE = True
SCRIPT_NAME = "L4D Hud Editor"
SCRIPT_DIR: str = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_ROOT: str = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SCRIPT_FILE_NAME = os.path.basename(PROJECT_ROOT)

# main directories
DEVELOPMENT_DIR = os.path.join(PROJECT_ROOT, "dev")
ASSETS_DIR = os.path.join(PROJECT_ROOT, "assets")
DATA_DIR = os.path.join(PROJECT_ROOT, "data")

# assets
IMAGES_DIR = os.path.join(ASSETS_DIR, "images")
MODS_DIR = os.path.join(ASSETS_DIR, "dependencies", "mods")
MISC_DIR = os.path.join(ASSETS_DIR, "misc")
TUTORIALS_DIR = os.path.join(ASSETS_DIR, "tutorials")

# data
SNIPPETS_DIR = os.path.join(DATA_DIR, "snippets")
NEW_HUD_DIR = os.path.join(DATA_DIR, "new hud template")
EDITOR_AUTOEXEC_PATH = os.path.join(DATA_DIR, "hud_editor_autoexec.cfg")
DUMMY_ADDON_VPK_PATH = os.path.join(DATA_DIR, "dummy_addon_vpk.vpk")
PERSISTENT_DATA_PATH = os.path.join(DATA_DIR, SCRIPT_NAME + ".json")
HUD_DESCRIPTIONS_PATH = os.path.join(DATA_DIR, "hud_file_descriptions.json")

# misc
UNIVERSAL_GAME_MAP = "hud_dev_map"
HOTKEY_SYNC_HUD = "ctrl+s"
HOTKEY_TOGGLE_BROWSER = "F5"
HOTKEY_EXECUTE_AUTOEXEC = "F11"


# data structures
class SyncState(Enum):
    """Enumeration representing sync states"""

    FULLY_SYNCED = auto()
    NOT_SYNCED = auto()


EDITOR_HUD_RELOAD_MODES = {
    "All": "reload_all",
    "Hud": "reload_hud",
    "Menu": "reload_menu",
    "Materials": "reload_materials",
    "Fonts": "reload_fonts",
}

# Object of preset game positions
GAME_POSITIONS = {
    "Custom (Save)": (None),
    "Center": (0.5, 0.5),
    "Top Left": (0, 0),
    "Top Right": (1, 0),
    "Bottom Left": (0, 1),
    "Bottom Right": (1, 1),
    "Top": (0.5, 0),
    "Bottom": (0.5, 1),
    "Left": (0, 0.5),
    "Right": (1, 0.5),
}

# Dictionary of map codes for each map
MAP_CODES = {
    "No Mercy": [
        {"name": "The Apartments", "code": "c8m1_apartment"},
        {"name": "The Subway", "code": "c8m2_subway"},
        {"name": "The Sewer", "code": "c8m3_sewers"},
        {"name": "The Hospital", "code": "c8m4_interior"},
        {"name": "Rooftop Finale", "code": "c8m5_rooftop"},
    ],
    "Crash Course": [
        {"name": "The Alleys", "code": "c2m1_highway"},
        {"name": "The Truck Depot Finale", "code": "c2m5_truckfactory"},
    ],
    "Death Toll": [
        {"name": "The Turnpike", "code": "c4m1_milltown_a"},
        {"name": "The Drains", "code": "c4m2_sugarmill_a"},
        {"name": "The Church", "code": "c4m3_creekbed_a"},
        {"name": "The Town", "code": "c4m4_ranchhouse_a"},
        {"name": "Boathouse Finale", "code": "c4m5_boat"},
    ],
    "Dead Air": [
        {"name": "The Greenhouse", "code": "c5m1_greenhouse"},
        {"name": "The Crane", "code": "c5m2_offices"},
        {"name": "The Construction Site", "code": "c5m3_bldg17"},
        {"name": "The Terminal", "code": "c5m4_terminal"},
        {"name": "Runway Finale", "code": "c5m5_runway"},
    ],
    "Blood Harvest": [
        {"name": "The Woods", "code": "c6m1_riverside"},
        {"name": "The Tunnel", "code": "c6m2_bedlam_a"},
        {"name": "The Bridge", "code": "c6m3_port_a"},
        {"name": "The Train Station", "code": "c6m4_mainstreet"},
        {"name": "Farmhouse Finale", "code": "c6m5_stairway"},
    ],
    "The Sacrifice": [
        {"name": "Docks", "code": "l4d2_docks"},
        {"name": "Barge", "code": "l4d2_barge"},
        {"name": "Port", "code": "l4d2_port"},
        {"name": "Sewer Junction", "code": "l4d2_sewers"},
        {"name": "Sacrificial Boat", "code": "l4d2_cemetery"},
    ],
    "Dead Center": [
        {"name": "Hotel", "code": "c1m1_hotel"},
        {"name": "Mall", "code": "c1m2_streets"},
        {"name": "Atrium", "code": "c1m3_atrium"},
        {"name": "Gun Shop", "code": "c1m4_mall"},
        {"name": "Concert Finale", "code": "c1m5_concert"},
    ],
    "Dark Carnival": [
        {"name": "Garage", "code": "c2m2_fairgrounds"},
        {"name": "Motel", "code": "c2m3_coaster"},
        {"name": "Barns", "code": "c2m4_barns"},
        {"name": "Concert", "code": "c2m5_concert"},
        {"name": "Atrium Finale", "code": "c2m5_atrium"},
    ],
    "Swamp Fever": [
        {"name": "Plank Country", "code": "c3m1_plankcountry"},
        {"name": "The Swamp", "code": "c3m2_swamp"},
        {"name": "Shantytown", "code": "c3m3_shantytown"},
        {"name": "The Plantation", "code": "c3m4_plantation"},
    ],
    "Hard Rain": [
        {"name": "Milltown", "code": "c13m1_milltown"},
        {"name": "Sugar Mill", "code": "c13m2_sugarmill"},
        {"name": "Mill Escape", "code": "c13m3_sugarmill_l4d2"},
        {"name": "Whitaker Farm", "code": "c13m4_lighthouse"},
        {"name": "Town Escape", "code": "c13m5_bridge"},
    ],
    "The Parish": [
        {"name": "Waterfront Market", "code": "c4m1_milltown_a"},
        {"name": "The Boulevard", "code": "c4m2_sugarmill_a"},
        {"name": "The Underground", "code": "c4m3_creekbed_a"},
        {"name": "The Rooftop", "code": "c4m4_ranchhouse_a"},
        {"name": "The Bridge", "code": "c4m5_boat"},
    ],
    "The Passing": [
        {"name": "The Riverbank", "code": "c13m1_l4d_garage"},
        {"name": "The Underground", "code": "c13m2_l4d_subway"},
        {"name": "The Port", "code": "c13m3_l4d_sewer"},
        {"name": "The Truck Depot Finale", "code": "c13m4_l4d_interactive"},
    ],
    "Cold Stream": [
        {"name": "Alpine Creek", "code": "c6m1_riverside"},
        {"name": "South Pine Stream", "code": "c6m2_bedlam_a"},
        {"name": "Memorial Bridge", "code": "c6m3_port_a"},
        {"name": "Cut-throat Creek", "code": "c6m4_mainstreet"},
        {"name": "Truck Depot Finale", "code": "c6m5_stairway"},
    ],
    "The Last Stand": [
        {"name": "The Junkyard", "code": "c14m1_junkyard"},
        {"name": "The Lighthouse", "code": "c14m2_lighthouse"},
    ],
}

# https://www.win.tue.nl/~aeb/linux/kbd/scancodes-1.html
KEY_SCANCODES = {
    "0": 0x0B,
    "1": 0x02,
    "2": 0x03,
    "3": 0x04,
    "4": 0x05,
    "5": 0x06,
    "6": 0x07,
    "7": 0x08,
    "8": 0x09,
    "9": 0x0A,
    "a": 0x1E,
    "b": 0x30,
    "c": 0x2E,
    "d": 0x20,
    "e": 0x12,
    "f": 0x21,
    "g": 0x22,
    "h": 0x23,
    "i": 0x17,
    "j": 0x24,
    "k": 0x25,
    "l": 0x26,
    "m": 0x32,
    "n": 0x31,
    "o": 0x18,
    "p": 0x19,
    "q": 0x10,
    "r": 0x13,
    "s": 0x1F,
    "t": 0x14,
    "u": 0x16,
    "v": 0x2F,
    "w": 0x11,
    "x": 0x2D,
    "y": 0x15,
    "z": 0x2C,
    "f1": 0x3B,
    "f2": 0x3C,
    "f3": 0x3D,
    "f4": 0x3E,
    "f5": 0x3F,
    "f6": 0x40,
    "f7": 0x41,
    "f8": 0x42,
    "f9": 0x43,
    "f10": 0x44,
    "f11": 0x57,
    "f12": 0x58,
    "backspace": 0x0E,
    "tab": 0x0F,
    "enter": 0x1C,
    "shift": 0x2A,
    "ctrl": 0x1D,
    "alt": 0x38,
    "caps_lock": 0x3A,
    "space": 0x39,
    "escape": 0x01,
    "insert": 0x52,
    "delete": 0x53,
    "home": 0x47,
    "end": 0x4F,
    "page_up": 0x49,
    "page_down": 0x51,
    "left_arrow": 0xCB,
    "right_arrow": 0xCD,
    "up_arrow": 0xC8,
    "down_arrow": 0xD0,
    "num_lock": 0x45,
    "numpad_0": 0x52,
    "numpad_1": 0x4F,
    "numpad_2": 0x50,
    "numpad_3": 0x51,
    "numpad_4": 0x4B,
    "numpad_5": 0x4C,
    "numpad_6": 0x4D,
    "numpad_7": 0x47,
    "numpad_8": 0x48,
    "numpad_9": 0x49,
    "numpad_add": 0x4E,
    "numpad_subtract": 0x4A,
    "numpad_multiply": 0x37,
    "numpad_divide": 0xB5,
    "numpad_enter": 0x1C,
    "numpad_decimal": 0x53,
    "left_windows": 0x5B,
    "right_windows": 0x5C,
    "menu": 0x5D,
}

# https://learn.microsoft.com/en-us/windows/win32/inputdev/virtual-key-codes
KEY_MAP = {
    "backspace": 0x08,
    "tab": 0x09,
    "enter": 0x0D,
    "shift": 0x10,
    "ctrl": 0x11,
    "alt": 0x12,
    "pause": 0x13,
    "capslock": 0x14,
    "escape": 0x1B,
    "space": 0x20,
    "pageup": 0x21,
    "pagedown": 0x22,
    "end": 0x23,
    "home": 0x24,
    "leftarrow": 0x25,
    "uparrow": 0x26,
    "rightarrow": 0x27,
    "downarrow": 0x28,
    "printscreen": 0x2C,
    "insert": 0x2D,
    "delete": 0x2E,
    "0": 0x30,
    "1": 0x31,
    "2": 0x32,
    "3": 0x33,
    "4": 0x34,
    "5": 0x35,
    "6": 0x36,
    "7": 0x37,
    "8": 0x38,
    "9": 0x39,
    "a": 0x41,
    "b": 0x42,
    "c": 0x43,
    "d": 0x44,
    "e": 0x45,
    "f": 0x46,
    "g": 0x47,
    "h": 0x48,
    "i": 0x49,
    "j": 0x4A,
    "k": 0x4B,
    "l": 0x4C,
    "m": 0x4D,
    "n": 0x4E,
    "o": 0x4F,
    "p": 0x50,
    "q": 0x51,
    "r": 0x52,
    "s": 0x53,
    "t": 0x54,
    "u": 0x55,
    "v": 0x56,
    "w": 0x57,
    "x": 0x58,
    "y": 0x59,
    "z": 0x5A,
    "num0": 0x60,
    "num1": 0x61,
    "num2": 0x62,
    "num3": 0x63,
    "num4": 0x64,
    "num5": 0x65,
    "num6": 0x66,
    "num7": 0x67,
    "num8": 0x68,
    "num9": 0x69,
    "multiply": 0x6A,
    "add": 0x6B,
    "subtract": 0x6D,
    "decimal": 0x6E,
    "divide": 0x6F,
    "f1": 0x70,
    "f2": 0x71,
    "f3": 0x72,
    "f4": 0x73,
    "f5": 0x74,
    "f6": 0x75,
    "f7": 0x76,
    "f8": 0x77,
    "f9": 0x78,
    "f10": 0x79,
    "f11": 0x7A,
    "f12": 0x7B,
    "numlock": 0x90,
    "scrolllock": 0x91,
    "semicolon": 0xBA,
    "plus": 0xBB,
    "comma": 0xBC,
    "minus": 0xBD,
    "period": 0xBE,
    "forwardslash": 0xBF,
    "graveaccent": 0xC0,
    "leftbracket": 0xDB,
    "backslash": 0xDC,
    "rightbracket": 0xDD,
    "singlequote": 0xDE,
}

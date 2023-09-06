"""Global constant variables"""
import os
from tkinter import PhotoImage
from typing import Dict, List, Optional, Tuple

from shared_utils.shared_utils import generate_version_number_from_git

#####################################################
# Path
#####################################################

# core
DEBUG_MODE: bool = True
VERSION_NO: str = generate_version_number_from_git(major_version=0)
SCRIPT_NAME: str = "Hud Editor for L4D2"
SCRIPT_DIR: str = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_ROOT: str = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SCRIPT_FILE_NAME: str = os.path.basename(PROJECT_ROOT)

# main directories
DEVELOPMENT_DIR: str = os.path.join(PROJECT_ROOT, "dev")
ASSETS_DIR: str = os.path.join(PROJECT_ROOT, "assets")
DATA_DIR: str = os.path.join(PROJECT_ROOT, "data")

# assets
MODS_DIR: str = os.path.join(ASSETS_DIR, "mods")
MISC_DIR: str = os.path.join(ASSETS_DIR, "misc")
TUTORIALS_DIR: str = os.path.join(ASSETS_DIR, "tutorials")
IMAGES_DIR: str = os.path.join(ASSETS_DIR, "images")

# image_dirs
IMAGES_DIR_EXT: str = os.path.join(IMAGES_DIR, "tree_file_extensions")
IMAGES_DIR_128: str = os.path.join(IMAGES_DIR, "png_128x128")
IMAGES_DIR_32: str = os.path.join(IMAGES_DIR, "png_32x32")
IMAGES_DIR_MISC: str = os.path.join(IMAGES_DIR, "misc")

# asset files
VPK_EXE_CREATE: str = os.path.join(ASSETS_DIR, "vpk.exe", "left4dead", "vpk.exe")
VPK_EXE_EXTRACT: str = os.path.join(ASSETS_DIR, "vpk.exe", "nosteam", "vpk.exe")

# image files
APP_ICON: str = os.path.join(ASSETS_DIR, "app.ico")
BIG_CROSS_ICON: str = os.path.join(IMAGES_DIR, "png_128x128", "cross.png")

# data
SNIPPETS_DIR: str = os.path.join(DATA_DIR, "snippets")
NEW_HUD_DIR: str = os.path.join(DATA_DIR, "new_hud_template")
EDITOR_AUTOEXEC_PATH: str = os.path.join(DATA_DIR, "hud_editor_autoexec.cfg")
DUMMY_ADDON_VPK_PATH: str = os.path.join(DATA_DIR, "dummy_addon_vpk.vpk")
PERSISTENT_DATA_PATH: str = os.path.join(DATA_DIR, SCRIPT_NAME + ".json")
HUD_DESCRIPTIONS_PATH: str = os.path.join(DATA_DIR, "hud_file_descriptions.json")

#####################################################
# General
#####################################################

BACKUP_APPEND_STRING: str = ".hud_dev_backup"
UNIVERSAL_GAME_MAP: str = "hud_dev_map"
HOTKEY_SYNC_HUD: str = "CTRL+R"
HOTKEY_EXECUTE_AUTOEXEC: str = "F11"
HOTKEY_EDITOR_MENU: str = "F8"
HOTKEY_TOGGLE_BROWSER: str = "F7"

EDITOR_HUD_RELOAD_MODES: Dict[str, str] = {
    "All": "reload_all",
    "Hud": "reload_hud",
    "Menu": "reload_menu",
    "Materials": "reload_materials",
    "Fonts": "reload_fonts",
}

# Object of preset game positions
GAME_POSITIONS: Dict[str, Optional[Tuple[float, float]]] = {
    "Custom (Save)": None,
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


#####################################################
# Image constants
#####################################################


class ImageConstants:
    """Manage loading and storing images for GUI components."""

    def __init__(self) -> None:
        """Initialize and load images."""
        self._images: Dict[str, PhotoImage] = {}
        self.load_images()

    def load_image(self, image_filename: str) -> PhotoImage:
        """Load and store an image.

        Keeping storing references inside self._images so they don't get garbage collected.

        This class isn't a singleton for the same reason. Because when assigning these images to a gui
        and then deleting the gui the images will get garbage collected and the next gui will fail.
        """
        image = PhotoImage(file=os.path.join(IMAGES_DIR_32, image_filename)).subsample(2, 2)
        self._images[image_filename] = image
        return image

    def get_image(self, filename: str) -> Optional[PhotoImage]:
        """Get a stored image."""
        return self._images.get(filename)

    def load_images(self) -> None:
        """Load and store various images as attributes."""
        self.add_black_circular_button = self.load_image("add_black_circular_button.png")
        self.adding_black_square_button_interface_symbol = self.load_image(
            "adding_black_square_button_interface_symbol.png"
        )
        self.addition_sign = self.load_image("addition_sign.png")
        self.airplane_silhouette = self.load_image("airplane_silhouette.png")
        self.alarm_clock = self.load_image("alarm_clock.png")
        self.arrow_angle_pointing_to_right = self.load_image("arrow_angle_pointing_to_right.png")
        self.arrows_couple_counterclockwise_rotating_symbol = self.load_image(
            "arrows_couple_counterclockwise_rotating_symbol.png"
        )
        self.ascendant_arrow = self.load_image("ascendant_arrow.png")
        self.attach_paperclip_symbol = self.load_image("attach_paperclip_symbol.png")
        self.auriculars_solid_tool_symbol = self.load_image("auriculars_solid_tool_symbol.png")
        self.back_arrow_solid_square_button = self.load_image("back_arrow_solid_square_button.png")
        self.back_black_square_interface_button_symbol = self.load_image(
            "back_black_square_interface_button_symbol.png"
        )
        self.bag_rounded_rectangular_black_tool_shape = self.load_image("bag_rounded_rectangular_black_tool_shape.png")
        self.bell_black_solid_musical_instrument = self.load_image("bell_black_solid_musical_instrument.png")
        self.bell_silhouette_black_shape_interface_symbol_of_alarm = self.load_image(
            "bell_silhouette_black_shape_interface_symbol_of_alarm.png"
        )
        self.black_cellphone_back = self.load_image("black_cellphone_back.png")
        self.black_circular_graphic = self.load_image("black_circular_graphic.png")
        self.black_half_sun = self.load_image("black_half_sun.png")
        self.black_ink_drop_shape = self.load_image("black_ink_drop_shape.png")
        self.buttons = self.load_image("buttons.png")
        self.black_map_folded_paper_symbol = self.load_image("black_map_folded_paper_symbol.png")
        self.black_oval_speech_bubble = self.load_image("black_oval_speech_bubble.png")
        self.black_placeholder_for_maps = self.load_image("black_placeholder_for_maps.png")
        self.black_silhouette_shape_of_an_object_like_a_spoon = self.load_image(
            "black_silhouette_shape_of_an_object_like_a_spoon.png"
        )
        self.black_square_button_with_an_arrow_pointing_out_to_upper_right = self.load_image(
            "black_square_button_with_an_arrow_pointing_out_to_upper_right.png"
        )
        self.black_tag_interface_symbol_in_vertical_position = self.load_image(
            "black_tag_interface_symbol_in_vertical_position.png"
        )
        self.black_winds_socket_tool_symbol = self.load_image("black_winds_socket_tool_symbol.png")
        self.book_black_opened_symbol = self.load_image("book_black_opened_symbol.png")
        self.bookmark_big_black_solid_rounded_interface_symbol = self.load_image(
            "bookmark_big_black_solid_rounded_interface_symbol.png"
        )
        self.bottle_black_container = self.load_image("bottle_black_container.png")
        self.broken_black_ticket_symbol = self.load_image("broken_black_ticket_symbol.png")
        self.buttons = self.load_image("buttons.png")
        self.calendar_events_symbol = self.load_image("calendar_events_symbol.png")
        self.call_black_auricular_interface_symbol = self.load_image("call_black_auricular_interface_symbol.png")
        self.center_text = self.load_image("center_text.png")
        self.chat_black_rectangular_rounded_speech_balloon_interface_symbol = self.load_image(
            "chat_black_rectangular_rounded_speech_balloon_interface_symbol.png"
        )
        self.chat_oval_black_balloons_couple = self.load_image("chat_oval_black_balloons_couple.png")
        self.chat_oval_black_interface_symbol_with_text_lines = self.load_image(
            "chat_oval_black_interface_symbol_with_text_lines.png"
        )
        self.clipboard_black_square_interface_symbol = self.load_image("clipboard_black_square_interface_symbol.png")
        self.clock_black_circular_tool = self.load_image("clock_black_circular_tool.png")
        self.close_arrow_shape_button_interface_symbol = self.load_image(
            "close_arrow_shape_button_interface_symbol.png"
        )
        self.cloud_black_shape = self.load_image("cloud_black_shape.png")
        self.cloud_black_storm_symbol_of_weather_with_hail_dots_falling = self.load_image(
            "cloud_black_storm_symbol_of_weather_with_hail_dots_falling.png"
        )
        self.compass_black_circular_orientation_tool = self.load_image("compass_black_circular_orientation_tool.png")
        self.configuration_gross_black_cogwheel_symbol_of_interface = self.load_image(
            "configuration_gross_black_cogwheel_symbol_of_interface.png"
        )
        self.copy_black_square_symbol = self.load_image("copy_black_square_symbol.png")
        self.counterclockwise_circular_arrow = self.load_image("counterclockwise_circular_arrow.png")
        self.cropping_design_interface_symbol_of_straight_lines = self.load_image(
            "cropping_design_interface_symbol_of_straight_lines.png"
        )
        self.cross = self.load_image("cross.png")
        self.cross_black_circular_button = self.load_image("cross_black_circular_button.png")
        self.cross_square_black_button = self.load_image("cross_square_black_button.png")
        self.cup_trophy_silhouette = self.load_image("cup_trophy_silhouette.png")
        self.diagonal_arrow_entering_in_black_square_button = self.load_image(
            "diagonal_arrow_entering_in_black_square_button.png"
        )
        self.double_horizontal_arrow = self.load_image("double_horizontal_arrow.png")
        self.double_left_arrows_symbol = self.load_image("double_left_arrows_symbol.png")
        self.double_vertical_arrow = self.load_image("double_vertical_arrow.png")
        self.down_arrow = self.load_image("down_arrow.png")
        self.down_arrow_black_circular_button = self.load_image("down_arrow_black_circular_button.png")
        self.down_arrow_black_circular_button_1 = self.load_image("down_arrow_black_circular_button_1.png")
        self.down_arrow_black_square_button = self.load_image("down_arrow_black_square_button.png")
        self.down_arrow_black_square_button_1 = self.load_image("down_arrow_black_square_button_1.png")
        self.down_arrow_symbol = self.load_image("down_arrow_symbol.png")
        self.down_arrow_symbol_in_black_square_button = self.load_image("down_arrow_symbol_in_black_square_button.png")
        self.download_black_cloud_interface_symbol_with_down_arrow_inside = self.load_image(
            "download_black_cloud_interface_symbol_with_down_arrow_inside.png"
        )
        self.download_black_square_interface_button_symbol = self.load_image(
            "download_black_square_interface_button_symbol.png"
        )
        self.download_interface_symbol_of_down_arrow_on_and_in_a_black_square = self.load_image(
            "download_interface_symbol_of_down_arrow_on_and_in_a_black_square.png"
        )
        self.email_black_envelope_front_interface_symbol = self.load_image(
            "email_black_envelope_front_interface_symbol.png"
        )
        self.email_black_envelope_symbol = self.load_image("email_black_envelope_symbol.png")
        self.email_black_opened_back_envelope_interface_symbol = self.load_image(
            "email_black_opened_back_envelope_interface_symbol.png"
        )
        self.equalizer = self.load_image("equalizer.png")
        self.equalizer_black_square_button = self.load_image("equalizer_black_square_button.png")
        self.event_calendar_symbol = self.load_image("event_calendar_symbol.png")
        self.exclamationmark = self.load_image("exclamationmark.png")
        self.exclamationmark_in_circle = self.load_image("exclamationmark_in_circle.png")
        self.expand_button_black_square_interface_symbol = self.load_image(
            "expand_button_black_square_interface_symbol.png"
        )
        self.expand_two_diagonal_arrows_symbol = self.load_image("expand_two_diagonal_arrows_symbol.png")
        self.fast_forward_double_black_arrows_multimedia_symbol = self.load_image(
            "fast_forward_double_black_arrows_multimedia_symbol.png"
        )
        self.fast_forward_double_right_arrows_symbol = self.load_image("fast_forward_double_right_arrows_symbol.png")
        self.file_black_rounded_symbol = self.load_image("file_black_rounded_symbol.png")
        self.file_black_rounded_symbol_1 = self.load_image("file_black_rounded_symbol_1.png")
        self.files_copy_interface_symbol = self.load_image("files_copy_interface_symbol.png")
        self.film_strip_piece_of_two_photograms = self.load_image("film_strip_piece_of_two_photograms.png")
        self.flag_black_cutted_shape = self.load_image("flag_black_cutted_shape.png")
        self.foggy_day = self.load_image("foggy_day.png")
        self.foggy_full_moon_night = self.load_image("foggy_full_moon_night.png")
        self.foggy_night = self.load_image("foggy_night.png")
        self.folder_black_interface_symbol = self.load_image("folder_black_interface_symbol.png")
        self.fork_black_silhouette_of_kitchen_eating_utensil = self.load_image(
            "fork_black_silhouette_of_kitchen_eating_utensil.png"
        )
        self.four_black_buttons_keyboard_of_rounded_squares = self.load_image(
            "four_black_buttons_keyboard_of_rounded_squares.png"
        )
        self.game_alt = self.load_image("game_alt.png")
        self.games_machine = self.load_image("games_machine.png")
        self.giftbox = self.load_image("giftbox.png")
        self.glass_of_cocktail_silhouette = self.load_image("glass_of_cocktail_silhouette.png")
        self.global_symbol_of_black_circle_with_grid = self.load_image("global_symbol_of_black_circle_with_grid.png")
        self.graphic_of_bars_on_screen = self.load_image("graphic_of_bars_on_screen.png")
        self.hot_or_burn_interface_symbol = self.load_image("hot_or_burn_interface_symbol.png")
        self.image_square_interface_button = self.load_image("image_square_interface_button.png")
        self.justify_text = self.load_image("justify_text.png")
        self.keyboard_of_nine_circle_for_digital_devices = self.load_image(
            "keyboard_of_nine_circle_for_digital_devices.png"
        )
        self.knife_shape = self.load_image("knife_shape.png")
        self.left_alignment_interface_symbol = self.load_image("left_alignment_interface_symbol.png")
        self.left_arrow_and_black_square_symbol = self.load_image("left_arrow_and_black_square_symbol.png")
        self.left_arrow_angle_big_gross_symbol = self.load_image("left_arrow_angle_big_gross_symbol.png")
        self.left_arrow_black_button_square = self.load_image("left_arrow_black_button_square.png")
        self.left_arrow_black_circular_button = self.load_image("left_arrow_black_circular_button.png")
        self.left_arrow_curved_black_symbol = self.load_image("left_arrow_curved_black_symbol.png")
        self.left_arrow_in_circular_button_black_symbol = self.load_image(
            "left_arrow_in_circular_button_black_symbol.png"
        )
        self.left_black_arrow_symbol = self.load_image("left_black_arrow_symbol.png")
        self.like_solid_heart_black_symbol_for_interface = self.load_image(
            "like_solid_heart_black_symbol_for_interface.png"
        )
        self.link = self.load_image("link.png")
        self.list_interface_symbol = self.load_image("list_interface_symbol.png")
        self.list_symbol_of_three_items_with_dots = self.load_image("list_symbol_of_three_items_with_dots.png")
        self.locked_circular_black_padlock_interface_security_symbol = self.load_image(
            "locked_circular_black_padlock_interface_security_symbol.png"
        )
        self.login_symbol_of_an_arrow_entering_to_a_black_square = self.load_image(
            "login_symbol_of_an_arrow_entering_to_a_black_square.png"
        )
        self.megaphone_black_amplification_audio_tool_symbol = self.load_image(
            "megaphone_black_amplification_audio_tool_symbol.png"
        )
        self.menu_black_rounded_square_interface_button = self.load_image(
            "menu_black_rounded_square_interface_button.png"
        )
        self.menu_button = self.load_image("menu_button.png")
        self.menu_gross_interface_symbol = self.load_image("menu_gross_interface_symbol.png")
        self.minus_big_symbol = self.load_image("minus_big_symbol.png")
        self.minus_circular_black_button = self.load_image("minus_circular_black_button.png")
        self.minus_solid_black_square_button = self.load_image("minus_solid_black_square_button.png")
        self.mobile_device_black_symbol = self.load_image("mobile_device_black_symbol.png")
        self.monitor_black_tool = self.load_image("monitor_black_tool.png")
        self.moon_phase_black_crescent_shape = self.load_image("moon_phase_black_crescent_shape.png")
        self.movie_symbol_of_video_camera = self.load_image("movie_symbol_of_video_camera.png")
        self.music_amplifier = self.load_image("music_amplifier.png")
        self.music_note_symbol = self.load_image("music_note_symbol.png")
        self.music_solid_rectangular_rounded_button = self.load_image("music_solid_rectangular_rounded_button.png")
        self.music_square_frontal_speaker_amplifying_tool_symbol = self.load_image(
            "music_square_frontal_speaker_amplifying_tool_symbol.png"
        )
        self.music_theme_info_interface_symbol_of_musical_note_with_text_lines = self.load_image(
            "music_theme_info_interface_symbol_of_musical_note_with_text_lines.png"
        )
        self.musical_note = self.load_image("musical_note.png")
        self.musical_note_black_symbol = self.load_image("musical_note_black_symbol.png")
        self.mute_microphone_interface_symbol = self.load_image("mute_microphone_interface_symbol.png")
        self.mute_speaker_symbol_of_interface_with_a_cross = self.load_image(
            "mute_speaker_symbol_of_interface_with_a_cross.png"
        )
        self.new_email_black_back_envelope_symbol_of_interface = self.load_image(
            "new_email_black_back_envelope_symbol_of_interface.png"
        )
        self.notebook_black_tool_symbol = self.load_image("notebook_black_tool_symbol.png")
        self.oval_black_speech_balloon = self.load_image("oval_black_speech_balloon.png")
        self.oval_black_speech_balloon_with_three_dots_inside = self.load_image(
            "oval_black_speech_balloon_with_three_dots_inside.png"
        )
        self.paintbrush_design_tool_interface_symbol = self.load_image("paintbrush_design_tool_interface_symbol.png")
        self.paper_plane_black_folded_shape_of_triangular_arrow = self.load_image(
            "paper_plane_black_folded_shape_of_triangular_arrow.png"
        )
        self.paperclip_in_vertical_position = self.load_image("paperclip_in_vertical_position.png")
        self.pause_multimedia_big_gross_symbol_lines = self.load_image("pause_multimedia_big_gross_symbol_lines.png")
        self.pencil_big_black_writing_tool = self.load_image("pencil_big_black_writing_tool.png")
        self.person_black_user_shape = self.load_image("person_black_user_shape.png")
        self.person_info = self.load_image("person_info.png")
        self.photo_camera_black_tool = self.load_image("photo_camera_black_tool.png")
        self.pin_black_solid_silhouette_of_tool = self.load_image("pin_black_solid_silhouette_of_tool.png")
        self.play_black_triangle_interface_symbol_for_multimedia = self.load_image(
            "play_black_triangle_interface_symbol_for_multimedia.png"
        )
        self.plus_sign_on_zoom_magnifier = self.load_image("plus_sign_on_zoom_magnifier.png")
        self.portfolio_black_symbol = self.load_image("portfolio_black_symbol.png")
        self.printing_button_interface_symbol = self.load_image("printing_button_interface_symbol.png")
        self.prize_badge = self.load_image("prize_badge.png")
        self.questionmark = self.load_image("questionmark.png")
        self.radio_black_tool_symbol = self.load_image("radio_black_tool_symbol.png")
        self.rewind_multimedia_button_symbol_of_two_black_arrows = self.load_image(
            "rewind_multimedia_button_symbol_of_two_black_arrows.png"
        )
        self.right_arrow_angle_black_circular_interface_symbol = self.load_image(
            "right_arrow_angle_black_circular_interface_symbol.png"
        )
        self.right_arrow_black_button = self.load_image("right_arrow_black_button.png")
        self.right_arrow_black_square_button = self.load_image("right_arrow_black_square_button.png")
        self.right_arrow_curved_black_symbol = self.load_image("right_arrow_curved_black_symbol.png")
        self.right_arrow_in_black_circular_button = self.load_image("right_arrow_in_black_circular_button.png")
        self.right_arrow_solid_square_button = self.load_image("right_arrow_solid_square_button.png")
        self.right_arrow_symbol = self.load_image("right_arrow_symbol.png")
        self.right_black_arrow_signal = self.load_image("right_black_arrow_signal.png")
        self.ring_bell_of_hotel_reception = self.load_image("ring_bell_of_hotel_reception.png")
        self.rounded_corners_interface_square_symbol = self.load_image("rounded_corners_interface_square_symbol.png")
        self.sand_clock_silhouette = self.load_image("sand_clock_silhouette.png")
        self.save_black_diskette_interface_symbol = self.load_image("save_black_diskette_interface_symbol.png")
        self.search_magnifier_black_shape = self.load_image("search_magnifier_black_shape.png")
        self.share_black_solid_social_symbol = self.load_image("share_black_solid_social_symbol.png")
        self.shopping_basket_commercial_tool = self.load_image("shopping_basket_commercial_tool.png")
        self.shopping_cart_black_silhouette = self.load_image("shopping_cart_black_silhouette.png")
        self.shopping_cart_silhouette = self.load_image("shopping_cart_silhouette.png")
        self.shuffle_two_arrows_symbol = self.load_image("shuffle_two_arrows_symbol.png")
        self.solid_ascendant_arrow_symbol = self.load_image("solid_ascendant_arrow_symbol.png")
        self.solid_black_sun_symbol = self.load_image("solid_black_sun_symbol.png")
        self.sort_ascending_interface_symbol = self.load_image("sort_ascending_interface_symbol.png")
        self.sort_down_interface_symbol = self.load_image("sort_down_interface_symbol.png")
        self.speaker = self.load_image("speaker.png")
        self.speaker_audio_tool = self.load_image("speaker_audio_tool.png")
        self.speaker_black_audio_interface_symbol = self.load_image("speaker_black_audio_interface_symbol.png")
        self.square_black_geometric_shape = self.load_image("square_black_geometric_shape.png")
        self.square_shape_with_dots_on_corners = self.load_image("square_shape_with_dots_on_corners.png")
        self.squares_stack = self.load_image("squares_stack.png")
        self.star_black_fivepointed_shape_symbol = self.load_image("star_black_fivepointed_shape_symbol.png")
        self.store_commercial_symbol = self.load_image("store_commercial_symbol.png")
        self.storm_black_cloud_symbol = self.load_image("storm_black_cloud_symbol.png")
        self.storm_black_cloud_with_a_lightning_bolt_shape_inside = self.load_image(
            "storm_black_cloud_with_a_lightning_bolt_shape_inside.png"
        )
        self.switch_black_solid_symbol = self.load_image("switch_black_solid_symbol.png")
        self.switch_black_tool_symbol = self.load_image("switch_black_tool_symbol.png")
        self.tag_black_symbol = self.load_image("tag_black_symbol.png")
        self.target_black_circular_symbol = self.load_image("target_black_circular_symbol.png")
        self.three_bars_graphic_interface_symbol = self.load_image("three_bars_graphic_interface_symbol.png")
        self.timer_black_tool_symbol = self.load_image("timer_black_tool_symbol.png")
        self.trash_can_black_symbol = self.load_image("trash_can_black_symbol.png")
        self.travel_bag_of_vertical_black_design = self.load_image("travel_bag_of_vertical_black_design.png")
        self.tv_monitor = self.load_image("tv_monitor.png")
        self.two_arrows = self.load_image("two_arrows.png")
        self.two_arrows_in_black_square_button = self.load_image("two_arrows_in_black_square_button.png")
        self.two_arrows_triangles_pointing_to_sides_with_a_slash_line_in_the_middle = self.load_image(
            "two_arrows_triangles_pointing_to_sides_with_a_slash_line_in_the_middle.png"
        )
        self.two_black_drops_of_different_sizes = self.load_image("two_black_drops_of_different_sizes.png")
        self.two_clockwise_circular_rotating_arrows_circle = self.load_image(
            "two_clockwise_circular_rotating_arrows_circle.png"
        )
        self.two_opposite_diagonal_arrows_in_black_square = self.load_image(
            "two_opposite_diagonal_arrows_in_black_square.png"
        )
        self.unlocked_padlock = self.load_image("unlocked_padlock.png")
        self.up_arrow_black_square_button = self.load_image("up_arrow_black_square_button.png")
        self.up_arrow_black_square_button_1 = self.load_image("up_arrow_black_square_button_1.png")
        self.up_arrow_black_square_button_interface_symbol = self.load_image(
            "up_arrow_black_square_button_interface_symbol.png"
        )
        self.up_arrow_black_triangle_symbol = self.load_image("up_arrow_black_triangle_symbol.png")
        self.up_arrow_button = self.load_image("up_arrow_button.png")
        self.up_arrow_entering_in_black_square = self.load_image("up_arrow_entering_in_black_square.png")
        self.up_arrow_solid_black_square_button = self.load_image("up_arrow_solid_black_square_button.png")
        self.up_arrow_solid_circular_button = self.load_image("up_arrow_solid_circular_button.png")
        self.upload_to_internet_cloud = self.load_image("upload_to_internet_cloud.png")
        self.upload_tray_with_up_arrow_interface_symbol = self.load_image(
            "upload_tray_with_up_arrow_interface_symbol.png"
        )
        self.verification_checkmark_symbol = self.load_image("verification_checkmark_symbol.png")
        self.verify_black_square_interface_button_symbol = self.load_image(
            "verify_black_square_interface_button_symbol.png"
        )
        self.verify_circular_black_button_symbol = self.load_image("verify_circular_black_button_symbol.png")
        self.voice_amplification_or_recording_interface_symbol_of_a_microphone = self.load_image(
            "voice_amplification_or_recording_interface_symbol_of_a_microphone.png"
        )
        self.voice_interface_symbol_of_microphone_silhouette = self.load_image(
            "voice_interface_symbol_of_microphone_silhouette.png"
        )
        self.vs_code = self.load_image("vs_code.png")
        self.wallet_black_symbol = self.load_image("wallet_black_symbol.png")
        self.weekly_calendar_black_event_interface_symbol = self.load_image(
            "weekly_calendar_black_event_interface_symbol.png"
        )
        self.window_black_rounded_square_interface_symbol = self.load_image(
            "window_black_rounded_square_interface_symbol.png"
        )
        self.winds_weather_symbol = self.load_image("winds_weather_symbol.png")
        self.wrench_black_silhouette = self.load_image("wrench_black_silhouette.png")
        self.pencil_black_square = self.load_image("pencil_black_square.png")
        self.zoom_magnifier_with_minus_symbol = self.load_image("zoom_magnifier_with_minus_symbol.png")


# Dictionary of map codes for each map
MAP_CODES: Dict[str, List[Dict[str, str]]] = {
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
KEY_SCANCODES: Dict[str, int] = {
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

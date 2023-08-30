"Modify video.txt"
# pylint: disable=invalid-name, broad-exception-caught
import os

import vdf  # type: ignore


class VideoSettingsModifier:
    "Modify video.txt"

    def __init__(self, config_dir):
        "Modify video.txt init"
        self.config_dir = config_dir
        self.video_settings_path = os.path.join(config_dir, "video.txt")
        self.default_settings = {
            "setting.cpu_level": "2",
            "setting.gpu_level": "0",
            "setting.mat_antialias": "4",
            "setting.mat_aaquality": "0",
            "setting.mat_forceaniso": "16",
            "setting.mat_vsync": "0",
            "setting.mat_triplebuffered": "0",
            "setting.mat_grain_scale_override": "0",
            "setting.mat_monitorgamma": "1.800000",
            "setting.gpu_mem_level": "2",
            "setting.mem_level": "2",
            "setting.mat_queue_mode": "-1",
            "setting.defaultres": "1024",
            "setting.defaultresheight": "768",
            "setting.aspectratiomode": "0",
            "setting.fullscreen": "0",
            "setting.nowindowborder": "0",
        }

    def load_video_settings(self):
        """Load video settings or fall back to default"""
        try:
            if os.path.exists(self.video_settings_path):
                return vdf.load(open(self.video_settings_path, encoding="utf-8"))
        except Exception as e:
            print(f"Error loading video settings: {e}")

        # Return default settings if loading fails
        return {"VideoConfig": self.default_settings.copy()}

    def save_video_settings(self, video_settings):
        "Save"
        with open(self.video_settings_path, "w", encoding="utf-8") as f_handle:
            vdf.dump(video_settings, f_handle, pretty=True)

    def modify_video_setting(self, setting_key, setting_value):
        "Modify a specific key value"
        video_settings = self.load_video_settings()
        if video_settings is not None:
            video_settings["VideoConfig"][setting_key] = setting_value
            self.save_video_settings(video_settings)

    def set_fullscreen(self, fullscreen_value):
        "Set fullscreen"
        self.modify_video_setting("setting.fullscreen", fullscreen_value)

    def set_nowindowborder(self, nowindowborder_value):
        "Set window border"
        self.modify_video_setting("setting.nowindowborder", nowindowborder_value)

    def get_nowindowborder(self):
        "Get borderless (setting.nowindowborder)"
        video_settings = self.load_video_settings()
        if video_settings is not None:
            return video_settings["VideoConfig"]["setting.nowindowborder"]
        return None

    def get_fullscreen(self):
        "Get fullscreen (setting.fullscreen)"
        video_settings = self.load_video_settings()
        if video_settings is not None:
            return video_settings["VideoConfig"]["setting.fullscreen"]
        return None

    def get_width(self):
        "Get width (setting.defaultres)"
        video_settings = self.load_video_settings()
        if video_settings is not None:
            return video_settings["VideoConfig"]["setting.defaultres"]
        return None

    def get_height(self):
        "Get height (setting.defaultresheight)"
        video_settings = self.load_video_settings()
        if video_settings is not None:
            return video_settings["VideoConfig"]["setting.defaultresheight"]
        return None

import os

import vdf  # type: ignore


class VideoSettingsModifier:
    "Modify video.txt"

    def __init__(self, config_dir):
        self.config_dir = config_dir
        self.video_settings_path = os.path.join(config_dir, "video.txt")

    def load_video_settings(self):
        "Load"
        if os.path.exists(self.video_settings_path):
            return vdf.load(open(self.video_settings_path, encoding="utf-8"))
        return None

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

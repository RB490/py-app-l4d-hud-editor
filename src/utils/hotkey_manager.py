from pynput import keyboard


class HotkeyManager:
    def __init__(self):
        self.active_hotkeys = {}
        self.listener = keyboard.Listener(on_press=self.on_key_press)
        self.listener.start()

    def add_hotkey(self, key_combo, callback):
        if isinstance(key_combo, list) and len(key_combo) > 0:
            normalized_combo = frozenset(key_combo)
            self.active_hotkeys[normalized_combo] = callback

    def on_key_press(self, key):
        for combo, callback in self.active_hotkeys.items():
            if all(k in key for k in combo):
                callback()

    def start(self):
        self.listener.join()


def hotkey_manager_example():
    def my_callback():
        print("Hotkey pressed!")

    hotkey_manager = HotkeyManager()
    hotkey_manager.add_hotkey([keyboard.Key.ctrl, keyboard.KeyCode.from_char("a")], my_callback)
    hotkey_manager.add_hotkey([keyboard.Key.alt, keyboard.KeyCode.from_char("b")], my_callback)

    hotkey_manager.start()

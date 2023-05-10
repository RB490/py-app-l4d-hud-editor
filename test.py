from pynput import keyboard


def on_f4():
    print("F4 pressed")


def on_f5():
    print("F5 pressed")


# Register hotkeys using pynput
listener = keyboard.GlobalHotKeys({"<f1>": on_f4, "<f5>": on_f5})
listener.start()

# Keep the script running
input("Press Enter to exit...\n")

# Stop the listener when done
listener.stop()

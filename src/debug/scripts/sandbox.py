import time
import threading

import keyboard

def longer_duration_method():
    "debug hotkey"
    print("hotkey_debugging_method!")
    print("hotkey_debugging_method! #1")
    time.sleep(1)
    print("hotkey_debugging_method! #2")

def run_longer_duration_method_in_thread():
    thread = threading.Thread(target=longer_duration_method)
    thread.start()

# Simulate the issue without threading
print("Simulating the issue without threading:")
keyboard.add_hotkey('ctrl+s', longer_duration_method)

# Simulate the solution using threading
print("\nSimulating the solution using threading:")
run_longer_duration_method_in_thread()
keyboard.add_hotkey('ctrl+f', run_longer_duration_method_in_thread)
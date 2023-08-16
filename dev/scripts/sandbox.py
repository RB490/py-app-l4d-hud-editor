from ahk import AHK


def move_window_with_ahk(window_title, new_x, new_y):
    "Move window: https://pypi.org/project/ahk/"
    ahk = AHK()

    try:
        win = ahk.find_window(title=window_title)  # Find the opened window
        win.move(new_x, new_y)
    except Exception:
        print("Failed to move window using AHK")

    # ahk.run_script(f"WinMove, {window_title}, , {new_x}, {new_y}")


# Example usage
window_title = "Untitled - Notepad"  # Replace with the title of the window you want to move
# window_title = "notepad.exe"  # Replace with the title of the window you want to move
new_x = 100
new_y = 100

move_window_with_ahk(window_title, new_x, new_y)

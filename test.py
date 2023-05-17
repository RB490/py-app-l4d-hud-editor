import tkinter as tk


def get_mouse_position_on_click():
    """
    Returns the x, y coordinates of where the user clicks the mouse on the screen.

    This function creates a fullscreen window that listens for a mouse click event.
    When clicked, it destroys the window and returns the (x,y) coordinates of the click.
    If the user cancels the operation or closes the window, the function returns (None,None).
    """
    mouse_x, mouse_y = None, None  # Declare x, y variables outside on_click function
    root = tk.Tk()
    root.attributes("-fullscreen", True)  # make window fullscreen
    root.attributes("-topmost", True)  # keep window on top
    root.attributes("-alpha", 0.1)  # set transparency to 0.5 (125/255)
    root.overrideredirect(True)  # remove window decorations

    def on_click(event):
        pos_x, pos_y = event.x_root, event.y_root
        print(f"Mouse clicked at ({pos_x}, {pos_y})")
        root.destroy()  # destroy the window when mouse is clicked

    root.bind("<ButtonPress>", on_click)
    root.mainloop()

    print("returning after mainloop")

    return (mouse_x, mouse_y)  # Return the x, y coordinates after the mainloop ends


print(get_mouse_position_on_click())

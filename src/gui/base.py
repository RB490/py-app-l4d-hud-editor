# pylint: disable=broad-exception-caught
import tkinter as tk


class BaseGUI:
    def __init__(self, is_toplevel_gui=False):
        self.is_hidden = None
        self.is_resizable = True

        if is_toplevel_gui:
            self.root = tk.Toplevel()
        else:
            self.root = tk.Tk()
        self.root.title = "BaseGUI"
        self.hide()
        self.root.protocol("WM_DELETE_WINDOW", self.on_close)
        self.root.minsize(300, 200)

    def run(self):
        self.show()
        self.root.mainloop()

    def hide(self):
        self.root.withdraw()
        self.is_hidden = True

    def minimize(self):
        """Minimize the window (iconify)."""
        self.root.iconify()

    def show(self):
        self.root.deiconify()
        self.is_hidden = False

    def destroy(self):
        self.root.destroy()

    def set_window_geometry(self, geometry):
        try:
            self.root.geometry(geometry)
        except Exception:
            self.root.geometry("1000x1000+100+100")

    def get_window_geometry(self):
        """Get window geometry if GUI is loaded and visible"""
        if self.root and self.root.winfo_viewable():
            geometry = self.root.geometry()
            print(f"{self.root.title} geometry: {geometry}")
            return self.root.geometry()
        else:
            print("GUI is not loaded or visible. Returning default geometry.")
            return "1000x1000+100+100"

    def set_always_on_top(self, status):
        """Set 'always on top' status of the window"""
        if self.root:
            if status:
                self.root.attributes("-topmost", True)
            else:
                self.root.attributes("-topmost", False)
        else:
            print("GUI is not loaded.")

    def toggle_resizability(self):
        """Toggle the resizability of the window."""
        self.is_resizable = not self.is_resizable
        self.root.resizable(self.is_resizable, self.is_resizable)

    def toggle_visibility(self):
        """
        Toggles the visibility of the window between visible and hidden.
        """
        if self.is_hidden:
            self.show()
        else:
            self.hide()

    def set_hotkey(self, key_combination, callback):
        """
        Set a hotkey that triggers a callback function when the specified key combination is pressed.

        Args:
            key_combination (str): A string representing the key combination (e.g., "Ctrl+C").
            callback (function): The callback function to be triggered when the hotkey is pressed.
        """
        self.root.bind(key_combination, callback)

    def remove_hotkey(self, key_combination):
        """
        Remove the hotkey associated with the specified key combination.

        Args:
            key_combination (str): The key combination to remove (e.g., "Ctrl+C").
        """
        self.root.unbind(key_combination)

    def on_close(self):
        # pylint: disable=no-member
        self.save_window_geometry()
        self.hide()

"""BaseGUI"""
# pylint: disable=broad-exception-caught
import tkinter as tk


class BaseGUI:
    """BaseGUI"""

    def __init__(self, is_modal_dialog=False):
        """
        Initialize the BaseGUI.

        Args:
            is_modal_dialog (bool, optional): True if the GUI is a modal dialog, False otherwise.
        """
        self.is_hidden = None
        self.is_resizable = True

        # self.root = tk.Tk()
        # self.root = tk.Toplevel()
        if is_modal_dialog:
            self.root = tk.Toplevel()
        else:
            self.root = tk.Tk()
        self.root.title("BaseGUI")
        self.hide()
        self.root.protocol("WM_DELETE_WINDOW", self.on_close)
        self.root.minsize(300, 200)

    def hide(self):
        """Hide the window."""
        self.root.withdraw()
        self.is_hidden = True

    def minimize(self):
        """Minimize the window (iconify)."""
        self.root.iconify()

    def show(self):
        """Show the window."""
        self.root.deiconify()
        self.is_hidden = False
        self.root.mainloop()

    def destroy(self):
        """Destroy the window."""
        self.root.destroy()

    def set_window_geometry(self, geometry):
        """
        Set the window geometry.

        Args:
            geometry (str): The geometry string (e.g., "800x600+100+100").
        """
        try:
            self.root.geometry(geometry)
            print(f"Set {self.root.title} to '{geometry}'!")
        except Exception:
            print(f"Set {self.root.title} to default '1000x1000+100+100'!")
            self.root.geometry("1000x1000+100+100")

    def get_window_geometry(self):
        """Get window geometry if GUI is loaded and visible"""
        if self.root and self.root.winfo_viewable():
            geometry = self.root.geometry()
            print(f"{self.root.title} geometry: {geometry}")
            return geometry
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
        """Toggle window resizability."""
        self.is_resizable = not self.is_resizable
        self.root.resizable(self.is_resizable, self.is_resizable)

    def toggle_visibility(self):
        """Toggle window visibility between visible and hidden."""
        if self.is_hidden:
            self.show()
        else:
            self.hide()

    def set_hotkey(self, key_combination, callback, widget=None):
        """
        Set a hotkey that triggers a callback function.

        Args:
            key_combination (str): The key combination (e.g., "Ctrl+C").
            callback (function): The callback function.
            widget: The widget to bind the hotkey to (default: self.root).
        """
        target_widget = widget or self.root
        target_widget.bind(key_combination, callback)

    def remove_hotkey(self, key_combination):
        """
        Remove a hotkey associated with a key combination.

        Args:
            key_combination (str): The key combination to remove (e.g., "Ctrl+C").
        """
        self.root.unbind(key_combination)

    def on_close(self):
        """Callback function before the window is closed."""
        # pylint: disable=no-member
        self.save_window_geometry()
        self.hide()

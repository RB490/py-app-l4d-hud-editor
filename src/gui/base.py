"""BaseGUI"""
# pylint: disable=broad-exception-caught
import tkinter as tk


class BaseGUI:
    """BaseGUI"""

    def __init__(self, parent_toplevel_root=None):
        """
        Initialize the BaseGUI.

        Args:
            parent_root (tkinter main gui instance, optional): True if the GUI is a modal dialog, False otherwise.
        """
        self.is_hidden = None
        self.is_resizable = True
        self.is_running = False
        self.parent_toplevel_root = parent_toplevel_root if parent_toplevel_root else None

        if self.parent_toplevel_root:
            self.root = self.parent_toplevel_root
        else:
            self.root = tk.Tk()

        self.root.title("BaseGUI")
        self.hide()
        self.root.protocol("WM_DELETE_WINDOW", self.__on_close_internal)
        self.root.minsize(300, 200)

    def hide(self):
        """Hide the window."""
        self.__call_save_window_geometry()
        self.root.withdraw()
        self.is_hidden = True

    def minimize(self):
        """Minimize the window (iconify)."""
        self.__call_save_window_geometry()
        self.root.iconify()

    def show(self, hide=False):
        """Show the window."""
        self.root.deiconify()
        self.is_hidden = False
        if hide:
            self.hide()
        if not self.is_running:
            self.run()

    def run(self):
        """Run mainloop()"""
        if self.is_running:
            raise ValueError(f"Called GUI {self.root.title()} Run() while already running!")

        self.is_running = True
        print(f"Running GUI {self.root.title()}")
        if not self.parent_toplevel_root:
            self.root.mainloop()

    def destroy(self):
        """Destroy the window."""
        self.__call_save_window_geometry()
        self.root.update()  # fixes can't invoke "event" command: application has been destroyed error
        self.root.destroy()

    def set_fullscreen(self, fullscreen):
        """
        Set the window to full-screen mode.

        Args:
            fullscreen (bool): True to enable full-screen, False to disable.
        """
        self.is_hidden = False
        if fullscreen:
            if not self.parent_toplevel_root:
                self.root.attributes("-fullscreen", True)
            self.root.state("zoomed")  # Maximizes the window to full-screen
            self.root.overrideredirect(True)  # Hide window decorations
        else:
            if not self.parent_toplevel_root:
                self.root.attributes("-fullscreen", False)
            self.root.overrideredirect(False)  # Restore window decorations

    def set_transparency(self, transparency):
        """
        Set the window transparency.

        Args:
            transparency (float): The transparency value (0.0 to 1.0).
        """
        self.root.attributes("-alpha", transparency)
        print(f"{self.root.title()} GUI Transparency set to {transparency}")

    def set_decorations(self, show_decorations):
        """
        Set window decorations on or off.

        Args:
            show_decorations (bool): True to show decorations, False to hide.
        """
        self.root.overrideredirect(not show_decorations)
        if show_decorations:
            self.root.attributes("-fullscreen", False)
            print(f"{self.root.title()} GUI Window decorations are now visible.")
        else:
            print(f"{self.root.title()} GUI Window decorations are now hidden.")

    def set_window_geometry(self, geometry):
        """
        Set the window geometry.

        Args:
            geometry (str): The geometry string (e.g., "800x600+100+100").
        """
        try:
            self.root.geometry(geometry)
            print(f"Set {self.root.title()} GUI to '{geometry}'!")
        except Exception:
            print(f"Set {self.root.title()} GUI to default '1000x1000+100+100'!")
            self.root.geometry("1000x1000+100+100")

    def get_window_geometry(self):
        """Get window geometry if GUI is loaded and visible"""

        if self.is_running:
            geometry = self.root.geometry()
            print(f"{self.root.title()} GUI geometry: {geometry}")
            return geometry
        else:
            print(f"{self.root.title()} GUI is running. Returning default geometry.")
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

    def __call_save_window_geometry(self):
        try:
            if self.is_running:
                if hasattr(self, "save_window_geometry") and callable(getattr(self, "save_window_geometry")):
                    self.save_window_geometry()
                else:
                    print(f"GUI {self.root.title()} GUI does not have a save_window_geometry method to call!")
        except Exception as e_info:
            print(f"An error occurred: {e_info}")

    def __on_close_internal(self):
        """Callback function before the window is closed."""
        # pylint: disable=no-member
        self.__call_save_window_geometry()
        self.hide()

        # call the on_close method of the child gui
        if hasattr(self, "on_close") and callable(getattr(self, "on_close")):
            self.on_close()
        else:
            print(f"Child GUI {self.root.title()} does not have an 'on_close' method to call!")

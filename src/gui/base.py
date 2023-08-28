"""BaseGUI"""
# pylint: disable=broad-exception-caught, logging-fstring-interpolation
import logging
import tkinter as tk

from shared_utils.logging_manager import LoggerManager

logger_manager = LoggerManager(__name__, level=logging.WARNING)
# logger_manager = LoggerManager(__name__, level=logging.CRITICAL + 1)  # turns off
logger = logger_manager.get_logger()


class BaseGUI:
    """BaseGUI"""

    program_mainloop_started = False

    def __init__(self, parent_root=None):
        """
        Initialize the BaseGUI.

        Args:
            parent_root (tkinter main gui instance, optional): True if the GUI is a modal dialog, False otherwise.
        """
        self.is_hidden = None
        self.is_resizable = True
        self.has_been_run = False
        self.parent_root = parent_root if parent_root else None

        if self.parent_root:
            self.root = tk.Toplevel(self.parent_root)
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

    def maximize(self):
        """Maximize the window."""
        self.__call_save_window_geometry()
        self.root.state("zoomed")  # Maximizes the window

    def show(self, hide=False):
        """Show the window."""
        self.root.deiconify()
        self.is_hidden = False
        if hide:
            self.hide()
        if not self.has_been_run:
            self.run()

    def has_ran(self):
        """Check if GUI has been ran once"""
        if self.has_been_run:
            return True
        else:
            return False

    def get_mainloop_started(self):
        """Check if mainloop was started"""
        return BaseGUI.program_mainloop_started

    def set_mainloop_started(self, bool_value):
        """Check if mainloop was started"""
        BaseGUI.program_mainloop_started = bool_value
        return

    def run(self):
        """Run mainloop()"""
        if self.has_been_run:
            raise ValueError(f"Called GUI {self.root.title()} Run() while already running!")

        self.has_been_run = True
        logger.info(f"Running GUI {self.root.title()}")

        # toplevel gui's don't need a mainloop because they get handled by the main mainloop
        if not self.parent_root:
            self.set_mainloop_started(True)
            self.root.mainloop()

    def destroy(self):
        """Destroy the window."""
        self.__call_save_window_geometry()
        self.root.update()  # fixes can't invoke "event" command: application has been destroyed error
        self.root.destroy()

    def set_fullscreen(self, fullscreen):
        """
        Set the window to full-screen mode. Will/might disable alt+tab

        Args:
            fullscreen (bool): True to enable full-screen, False to disable.
        """
        self.is_hidden = False
        if fullscreen:
            if not self.parent_root:
                self.root.attributes("-fullscreen", True)
            self.root.state("zoomed")  # Maximizes the window to full-screen
            self.root.overrideredirect(True)  # Hide window decorations
        else:
            if not self.parent_root:
                self.root.attributes("-fullscreen", False)
            self.root.overrideredirect(False)  # Restore window decorations

    def set_transparency(self, transparency):
        """
        Set the window transparency.

        Args:
            transparency (float): The transparency value (0.0 to 1.0).
        """
        self.root.attributes("-alpha", transparency)
        logger.info(f"{self.root.title()} GUI Transparency set to {transparency}")

    def set_decorations(self, show_decorations):
        """
        Set window decorations on or off.

        Args:
            show_decorations (bool): True to show decorations, False to hide.
        """
        self.root.overrideredirect(not show_decorations)
        if show_decorations:
            self.root.attributes("-fullscreen", False)
            logger.info(f"{self.root.title()} GUI Window decorations are now visible.")
        else:
            logger.info(f"{self.root.title()} GUI Window decorations are now hidden.")

    def set_window_geometry(self, geometry):
        """
        Set the window geometry.

        Args:
            geometry (str): The geometry string (e.g., "800x600+100+100").
        """
        try:
            self.root.geometry(geometry)
            logger.info(f"Set {self.root.title()} GUI to '{geometry}'!")
        except Exception:
            logger.exception(f"Error setting {self.root.title()} GUI geometry")
            self.root.geometry("1000x1000+100+100")

    def get_window_geometry(self):
        """Get window geometry if GUI is loaded and visible"""

        if self.has_been_run:
            geometry = self.root.geometry()
            logger.info(f"{self.root.title()} GUI geometry: {geometry}")
            return geometry
        else:
            logger.warning(f"{self.root.title()} GUI is NOT running. Returning default geometry.")
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
        logger.info(f"{self.root.title()} GUI visibility toggled.")

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
            if self.has_been_run:
                if hasattr(self, "save_window_geometry") and callable(getattr(self, "save_window_geometry")):
                    self.save_window_geometry()
                    logger.info(f"Called save_window_geometry for {self.root.title()} GUI.")
                else:
                    logger.debug(f"GUI {self.root.title()} does not have a save_window_geometry method to call!")
        except Exception as e_info:
            logger.error(f"Error occurred while calling save_window_geometry for {self.root.title()} GUI: {e_info}")

    def __on_close_internal(self):
        """Callback function before the window is closed."""
        # pylint: disable=no-member
        self.__call_save_window_geometry()
        self.hide()
        if hasattr(self, "on_close") and callable(getattr(self, "on_close")):
            self.on_close()
        else:
            logger.debug(f"Child GUI {self.root.title()} does not have an 'on_close' method to call!")

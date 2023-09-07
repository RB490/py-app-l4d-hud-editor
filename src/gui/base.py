"""BaseGUI"""
# pylint: disable=broad-exception-caught, logging-fstring-interpolation
import tkinter as tk
from typing import Callable, Optional, Union

from loguru import logger


# Define constants for GUI types
class GUITypes:
    """Enumeration of the different GUI types"""

    MAIN = "main"  # mainloop() aka the one main gui in the program which also handles events for the sub guis
    SUB = "sub"  # sub gui aka any other gui other than the main
    MODAL = "modal"  # uses .update()


class BaseGUI:
    """BaseGUI"""

    program_mainloop_started: bool = False

    def __init__(self, gui_type: Union[GUITypes, str] = GUITypes.MAIN, parent_root: Optional[tk.Tk] = None) -> None:
        """
        Initialize the BaseGUI.

        Args:
            parent_root (tkinter main gui instance, optional): True if the GUI is a modal dialog, False otherwise.
        """
        self.gui_type = gui_type
        self.is_destroyed: bool = False
        self.is_hidden: bool = True
        self.is_resizable: bool = True
        self.has_been_run_status: bool = False
        self.parent_root = parent_root if parent_root else None
        self.root: Union[tk.Tk, tk.Toplevel]

        if self.gui_type == GUITypes.MAIN or self.gui_type == GUITypes.MODAL:
            self.root = tk.Tk()
        elif self.gui_type == GUITypes.SUB:
            if self.parent_root is None:
                raise ValueError("For GUITypes.SUB, parent_root must be supplied.")
            self.root = tk.Toplevel(self.parent_root)
        else:
            raise ValueError("Invalid gui_type.")

        self.window_handle = self.root.winfo_id()
        self.root.title("BaseGUI")
        self.hide()
        self.root.protocol("WM_DELETE_WINDOW", self.__on_close_internal)
        self.root.minsize(50, 50)

    def hide(self) -> None:
        """Hide the window."""
        self.__call_save_window_geometry()
        self.root.withdraw()
        self.is_hidden = True
        self.__call_method_if_exists("on_hide")

    def minimize(self) -> None:
        """Minimize the window (iconify)."""
        self.__call_save_window_geometry()
        self.root.iconify()

    def maximize(self) -> None:
        """Maximize the window."""
        self.__call_save_window_geometry()
        self.root.state("zoomed")  # Maximizes the window

    def run(self) -> None:
        """Run the mainloop."""
        if self.has_been_run_status:
            raise ValueError(f"Called {self.get_quoted_title()} Run() while already running!")

        self.has_been_run_status = True
        logger.debug(f"Running {self.get_quoted_title()} with gui_type: {self.gui_type}")

        # Toplevel GUIs don't need a mainloop because they get handled by the main mainloop
        if self.gui_type == GUITypes.MAIN:
            self.set_mainloop_started(True)
            self.root.mainloop()
            logger.info("Started main loop!")
        elif self.gui_type == GUITypes.MODAL:
            self.root.update()

    def show(self, hide: bool = False, callback: str = "") -> None:
        """
        Show the window.

        Purpose for callback can be to open a sub GUI (which relies on the main gui mainloop)

        Args:
            hide (bool, optional): If True, hide the window after showing. Defaults to False.
        """
        self.root.deiconify()
        self.is_hidden = False

        self.root.after(0, lambda: self.__delayed_show(callback))
        if hide:
            self.hide()
        if not self.has_been_run_status:
            self.run()

    def has_been_run(self):
        """Has GUI been ran?"""
        return self.has_been_run_status

    def set_title(self, title):
        """Set title"""
        self.root.title(title)

    def get_title(self):
        """Get title"""
        self.root.title()

    def is_visible(self):
        """Is visible?"""
        return not self.is_hidden

    def bring_to_front(self):
        """Bring GUI to front"""
        # Lift the window to the top
        self.root.lift()

        # Make the window topmost (works on some systems)
        previous_status = self.root.attributes("-topmost")
        self.root.attributes("-topmost", True)
        self.root.attributes("-topmost", False)
        self.root.attributes("-topmost", previous_status)

        # Set focus to the entire window
        self.root.focus_force()

    def __delayed_show(self, callback: str = ""):
        """After mainloop()"""
        logger.debug("Running __delayed_show")
        if not self.is_hidden:
            self.bring_to_front()
        self.__call_method_if_exists("on_show")
        if callback:
            self.__call_method_if_exists(callback)

    def focus_treeview(self, tree, *event):
        """Focus the first row of a treeview"""
        # pylint: disable=unused-argument
        tree.focus_set()
        children = tree.get_children()
        if children:
            tree.focus(children[0])
            tree.selection_set(children[0])
        return "break"  # Prevent the default tab behavior (inserting a tab character)

    def show_post_menu(self, menu, x, y):
        """
        Show a menu at the specified coordinates.

        Args:
            menu: The tkinter.Menu instance to post.
            x (int): The x-coordinate.
            y (int): The y-coordinate.
        """
        self.show()
        menu.post(x, y)

    def get_mainloop_started(self) -> bool:
        """Check if the mainloop was started."""
        return BaseGUI.program_mainloop_started

    def set_mainloop_started(self, bool_value: bool) -> None:
        """
        Set the status of whether the mainloop was started.

        Args:
            bool_value (bool): True if the mainloop was started, False otherwise.
        """
        BaseGUI.program_mainloop_started = bool_value

    def get_hwnd(self):
        """Retrieve HWND"""
        logger.debug(f"{self.get_quoted_title()} HWND = {self.window_handle}")
        return self.window_handle

    def destroy(self) -> None:
        """Destroy the window."""
        if not self.is_destroyed:
            self.__call_save_window_geometry()
            self.__call_method_if_exists("on_destroy")  # call this before the actual destroy can't invoke "wm" command
            self.root.update()  # Fixes "can't invoke 'event' command: application has been destroyed" error
            self.root.destroy()
            self.is_destroyed = True

    def set_fullscreen(self, fullscreen: bool) -> None:
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

    def set_transparency(self, transparency: float) -> None:
        """
        Set the window transparency.

        Args:
            transparency (float): The transparency value (0.0 to 1.0).
        """
        self.root.attributes("-alpha", transparency)
        logger.debug(f"{self.get_quoted_title()} Transparency set to {transparency}")

    def set_decorations(self, show_decorations: bool) -> None:
        """
        Set window decorations on or off.

        Args:
            show_decorations (bool): True to show decorations, False to hide.
        """
        self.root.overrideredirect(not show_decorations)
        if show_decorations:
            self.root.attributes("-fullscreen", False)
            logger.debug(f"{self.get_quoted_title()} Window decorations are now visible.")
        else:
            logger.debug(f"{self.get_quoted_title()} Window decorations are now hidden.")

    def set_window_geometry(self, geometry: str) -> None:
        """
        Set the window geometry.

        Args:
            geometry (str): The geometry string (e.g., "800x600+100+100").
        """
        try:
            self.root.geometry(geometry)
            logger.debug(f"Set {self.get_quoted_title()} to '{geometry}'!")
        except Exception:
            logger.exception(f"Error setting {self.get_quoted_title()} geometry")
            self.root.geometry("1000x1000+100+100")

    def get_quoted_title(self):
        """Get pretty quoted title for displaying logging statements"""
        quoted_title = f"'{self.root.title()}'"
        return quoted_title

    def get_window_geometry(self) -> str:
        """Get window geometry if GUI is loaded and visible"""

        if self.has_been_run_status:
            geometry = self.root.geometry()
            logger.debug(f"{self.get_quoted_title()} geometry: {geometry}")
            return geometry
        else:
            logger.warning(f"{self.get_quoted_title()} is NOT running. Returning default geometry.")
            return "1000x1000+100+100"

    def set_always_on_top(self, status: bool) -> None:
        """Set 'always on top' status of the window"""
        if self.root:
            if status:
                self.root.attributes("-topmost", True)
            else:
                self.root.attributes("-topmost", False)
        else:
            logger.debug(f"{self.get_quoted_title()} always on top: GUI is not loaded")
        logger.debug(f"{self.get_quoted_title()} always on top: {status}")

    def set_resizable(self, is_resizable):
        """Set window resizability."""
        self.is_resizable = is_resizable
        self.root.resizable(is_resizable, is_resizable)

    def toggle_visibility(self):
        """Toggle window visibility between visible and hidden."""
        if self.is_hidden:
            self.show()
        else:
            self.hide()
        logger.debug(f"{self.get_quoted_title()} visibility toggled.")

    def set_hotkey(self, key_combination: str, callback: Callable, widget: Optional[tk.Widget] = None) -> None:
        """
        Set a hotkey that triggers a callback function.

        Args:
            key_combination (str): The key combination (e.g., "Ctrl+C").
            callback (callable): The callback function.
            widget (Optional[tk.Widget]): The widget to bind the hotkey to (default: self.root).
        """
        target_widget = widget or self.root
        target_widget.bind(key_combination, callback)

    def remove_hotkey(self, key_combination: str) -> None:
        """
        Remove a hotkey associated with a key combination.

        Args:
            key_combination (str): The key combination to remove (e.g., "Ctrl+C").
        """
        self.root.unbind(key_combination)

    def __on_close_internal(self) -> None:
        """Callback function before the window is closed."""
        self.hide()
        self.__call_save_window_geometry()
        self.__call_method_if_exists("on_close")

    def __call_save_window_geometry(self) -> None:
        if self.has_been_run_status:
            self.__call_method_if_exists("save_window_geometry")

    def __call_method_if_exists(self, method_name: str) -> None:
        if hasattr(self, method_name) and callable(getattr(self, method_name)):
            method = getattr(self, method_name)
            method()
            logger.debug(f"Called {method_name} for {self.get_quoted_title()}.")
        else:
            logger.debug(f"{self.get_quoted_title()} does not have a {method_name} method to call!")

    def show_menu_on_button(self, button, menu):
        """Display a context menu near the specified button."""
        x, y, _, _ = button.bbox("all")

        # Calculate the new position for the context menu
        new_x = button.winfo_rootx() + x
        new_y = button.winfo_rooty() + y + button.winfo_height()

        # Display the context menu
        logger.debug(f"Showing context menu @ x:{new_x} y:{new_y}")
        menu.post(new_x, new_y)


def example_create_main_and_sub_gui():
    """Example"""
    # Create a main GUI window
    main_gui = BaseGUI(gui_type=GUITypes.MAIN)
    main_gui.set_window_geometry("800x600")  # Set the window size
    main_gui.set_resizable(True)  # Allow the window to be resized

    # Define a callback function to show the sub GUI
    def show_sub_gui():
        sub_gui.show()

    # Create a button in the main GUI that opens the sub GUI
    button = tk.Button(main_gui.root, text="Open Sub GUI", command=show_sub_gui)
    button.pack()

    # Create a sub GUI window with the main GUI as its parent
    sub_gui = BaseGUI(gui_type=GUITypes.SUB, parent_root=main_gui.root)
    sub_gui.set_window_geometry("400x300")  # Set the sub GUI window size

    # Create a button in the sub GUI to close it
    sub_button = tk.Button(sub_gui.root, text="Close Sub GUI", command=sub_gui.hide)
    sub_button.pack()

    # Show the main GUI
    main_gui.show()

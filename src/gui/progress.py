"""A progress GUI window for installation."""
import tkinter as tk

from utils.constants import APP_ICON


class ProgressGUI:
    """A class representing a progress GUI window for installation."""

    def __init__(self, total_steps, initial_width, maximum_width):
        """Initialize the progress GUI with the specified parameters.

        Args:
            total_steps (int): The total number of steps in the installation process.
            initial_width (int): The initial width of the GUI window.
            maximum_width (int): The maximum width the GUI window can have.
        """
        self.root = tk.Tk()
        self.root.title("Installation Progress")
        self.root.iconbitmap(APP_ICON)
        self.height = 70
        self.root.geometry(f"{initial_width}x{self.height}")
        self.root.resizable(True, False)  # resizable in width but not in height

        self.total_steps = total_steps
        self.current_step = 0
        self.step_info_label_xpadding = 15
        self.max_label_length = maximum_width
        self.avg_char_width = None

        self._init_gui()

    def _init_gui(self):
        """Initialize the GUI elements and layout."""
        self.step_info_label = tk.Label(
            self.root,
            text="",
            font=("Helvetica", 14),
            wraplength=99999999,
        )
        self.step_info_label.pack(padx=self.step_info_label_xpadding, pady=(10, 0))

        self.steps_remaining_label = tk.Label(self.root, text="")
        self.steps_remaining_label.pack(padx=10, pady=(0, 10))

        self._calculate_avg_char_width()
        self._update_minimum_width()

    def _calculate_avg_char_width(self):
        """Calculate the average character width based on the font."""
        font = self.step_info_label.cget("font")
        canvas = tk.Canvas(self.root)
        avg_char_width_item = canvas.create_text(0, 0, font=font, text="x")
        char_bbox = canvas.bbox(avg_char_width_item)
        self.avg_char_width = char_bbox[2] - char_bbox[0]
        canvas.destroy()

    def _update_minimum_width(self):
        """Update the minimum width of the GUI window."""
        minimum_width = int(self.max_label_length * 20)
        current_width = self.root.winfo_width()

        if current_width < minimum_width:
            self.root.geometry(f"{minimum_width}x{self.height}")
        else:
            self.root.minsize(minimum_width, self.height)

    def update_progress(self, step_information):
        """Update the progress GUI with new step information.

        Args:
            step_information (str): The information about the current step.
        """
        self.current_step += 1

        # visually cutoff text longer than would fit in the gui by adding '...'
        available_width = self.root.winfo_width() - (self.step_info_label_xpadding * 2)
        max_chars = int(available_width / self.avg_char_width)
        displayed_text = (
            step_information[:max_chars] + "..." if len(step_information) > max_chars else step_information
        )

        # print(f"len(step_information) = {len(step_information)}")
        # print(f"max_chars = {max_chars}")
        # print(f"available_width = {available_width}")
        # print(f"displayed_text = {displayed_text}")

        # update the gui
        self.step_info_label.config(text=displayed_text)
        self.steps_remaining_label.config(text=f"Step {self.current_step} of {self.total_steps}")
        self._update_minimum_width()
        self.root.update()

    def close(self):
        """Close the progress GUI window."""
        self.root.destroy()

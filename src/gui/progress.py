"""A progress GUI window for installation."""
# pylint: disable=broad-exception-raised
import tkinter as tk

from gui.base import BaseGUI
from shared_utils.shared_utils import show_message
from utils.constants import APP_ICON


class ProgressGUI(BaseGUI):
    """A class representing a progress GUI window for installation."""

    def __init__(self, action_description: str, initial_width: int, max_label_length: int, total_steps: int) -> None:
        """
        Initialize the progress GUI with the specified parameters.

        Args:
            action_description (str): The description of the action.
            initial_width (int): The initial width of the GUI window.
            max_label_length (int): The maximum label length.
            total_steps (int): The total number of steps in the installation process.
        """
        super().__init__(gui_type="modal")
        self.root.title(action_description)
        self.root.iconbitmap(APP_ICON) # type: ignore
        self.root.protocol("WM_DELETE_WINDOW", self.close)
        self.height = 125
        self.root.geometry(f"{initial_width}x{self.height}")
        self.root.resizable(True, False)  # resizable in width but not in height

        self.action_description = action_description
        self.total_steps = total_steps
        self.current_step = 0
        self.step_info_label_xpadding = 15
        self.max_label_length = max_label_length
        self.longest_label_length = 10
        self.avg_char_width: float = 0

        self.__create_widgets()

    def __create_widgets(self) -> None:
        """Initialize the GUI elements and layout."""
        self.action_description_label = tk.Label(
            self.root,
            text=self.action_description,
            font=("Helvetica", 20),
            wraplength=99999999,
            padx=self.step_info_label_xpadding,
            pady=10,  # Use a single value for padding at the top
        )
        self.action_description_label.pack(fill="both", expand=True)

        self.step_info_label = tk.Label(
            self.root,
            text="",
            font=("Helvetica", 14),
            wraplength=99999999,
        )
        self.step_info_label.pack(fill="both", expand=True, padx=self.step_info_label_xpadding, pady=(10, 0))

        self.steps_remaining_label = tk.Label(self.root, text="")
        self.steps_remaining_label.pack(padx=10, pady=(0, 10))

        self._calculate_avg_char_width()
        self._update_minimum_width()

    def _calculate_avg_char_width(self) -> None:
        """Calculate the average character width based on the font."""
        font = self.step_info_label.cget("font")
        canvas = tk.Canvas(self.root)
        avg_char_width_item = canvas.create_text(0, 0, font=font, text="x")
        char_bbox = canvas.bbox(avg_char_width_item)
        self.avg_char_width = char_bbox[2] - char_bbox[0]
        canvas.destroy()

    def _update_minimum_width(self) -> None:
        """Update the minimum width of the GUI window."""
        if self.longest_label_length > self.max_label_length:
            minimum_width = int(self.longest_label_length * self.avg_char_width)
        else:
            minimum_width = int(self.longest_label_length * 20)
        current_width = self.root.winfo_width()

        if current_width < minimum_width:
            self.root.geometry(f"{minimum_width}x{self.height}")
        else:
            self.root.minsize(minimum_width, self.height)

    def update_progress(self, step_information: str) -> None:
        """Update the progress GUI with new step information.

        Args:
            step_information (str): The information about the current step.
        """
        # GUI has been closed, so return without updating (2x check=self.root.winfo_exists fails when it doesn't exist)
        try:
            if not self.root.winfo_exists():
                raise Exception(f"{self.action_description} cancelled!")
        except Exception as e_inf:
            raise Exception(f"{self.action_description} cancelled!") from e_inf

        self.current_step += 1

        # Update longest_step_info if the current step_information is longer
        if len(step_information) > self.longest_label_length:
            self.longest_label_length = len(step_information)

        # visually cutoff text longer than would fit in the gui by adding '...'
        available_width = self.root.winfo_width() - (self.step_info_label_xpadding * 2)
        max_chars = int(available_width / self.avg_char_width)
        displayed_text = (
            step_information[:max_chars] + "..." if len(step_information) > max_chars else step_information
        )

        print()
        print(f"Step #{self.current_step}")
        print(f"self.longest_step_info() = {self.longest_label_length}")
        print(f"self.root.winfo_width() = {self.root.winfo_width()}")
        print(f"len(step_information) = {len(step_information)}")
        print(f"max_chars = {max_chars}")
        print(f"available_width = {available_width}")
        print(f"displayed_text = {displayed_text}")
        print()

        # update the gui
        self.step_info_label.config(text=displayed_text)
        self.steps_remaining_label.config(text=f"Step {self.current_step} of {self.total_steps}")
        self._update_minimum_width()
        self.root.update()

    def close(self) -> None:
        """Close the progress GUI window."""
        result = show_message(f"Are you sure you want to stop {self.action_description.lower()}?", "yesno")
        if not result:
            return
        self.root.destroy()

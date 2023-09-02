# pylint: disable= line-too-long, missing-module-docstring
import logging


class LoggingManager:
    """
    LoggerManager class that manages a logger instance.

    Methods:
    - __init__(name, level): Initializes the logger instance and sets up logging.
    - setup_logging(level): Configures the logger with a console handler and sets the logging format.
    - get_logger(): Returns the logger instance.
    """

    def __init__(self, name, level=logging.DEBUG):
        """Initialize logger and setup logging during object creation."""
        self.logger_name = name
        self.setup_logging(level)

    def setup_logging(self, level):
        """Configures the logger with a console handler and sets the logging format."""
        self.logger = logging.getLogger(self.logger_name)
        self.logger.setLevel(level)
        console_handler = logging.StreamHandler()
        console_handler.setLevel(level)

        formatter = logging.Formatter("%(name)s (%(levelname)s): %(message)s")
        # game.dir_id_handler (DEBUG): ID Path: E:\games\steam\steamapps\common\Left 4 Dead 2\_hud_editor_id_file__dev_directory.DoNotDelete

        # formatter = logging.Formatter("%(asctime)s - %(name)s (%(levelname)s): %(message)s")
        # 2023-08-28 23:38:12,040 - game.dir_id_handler (DEBUG): ID Path: E:\games\steam\steamapps\common\Left 4 Dead 2\_hud_editor_id_file__dev_directory.DoNotDelete

        # formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
        # 2023-08-28 23:38:59,448 - game.dir_id_handler - DEBUG - ID Path: E:\games\steam\steamapps\common\Left 4 Dead 2\_hud_editor_id_file__dev_directory.DoNotDelete

        console_handler.setFormatter(formatter)
        self.logger.addHandler(console_handler)

    def get_logger(self):
        """Returns the logger instance."""
        return self.logger


def logging_class_usage_example():
    """
    Example of using the LoggerManager to log messages.
    """
    # logging_manager = LoggerManager(__name__, level=logging.INFO)  # Pass the desired logging level
    # logging_manager = LoggerManager(__name__, level=logging.CRITICAL)  # Pass the desired logging level
    # logging_manager = LoggerManager(__name__, level=logging.CRITICAL + 1)  # Pass the desired logging level
    # Get the logger instance
    logging_manager = LoggingManager(__name__, level=logging.WARNING)
    log = logging_manager.get_logger()

    # Log messages at different levels
    log.debug("This is a debug message")
    log.info("This is an info message")
    log.warning("This is a warning message")
    log.error("This is an error message")
    log.critical("This is a critical message")
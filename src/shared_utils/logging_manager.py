# pylint: disable= line-too-long, missing-module-docstring
import logging


def get_logger(name, log_level=logging.INFO):
    """
    Get a logger with the specified name and logging level.

    Args:
        name (str): The name of the logger.
        log_level (int): The logging level (default is logging.INFO).

    Returns:
        logger (logging.Logger): The logger instance.
    """
    internal_logger = logging.getLogger(name)
    internal_logger.setLevel(log_level)

    # formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    formatter = logging.Formatter("%(name)s (%(levelname)s): %(message)s")

    # Create a console handler and set the log level
    ch = logging.StreamHandler()
    ch.setLevel(log_level)
    ch.setFormatter(formatter)

    # Add the console handler to the logger only if it has no handlers
    if not internal_logger.hasHandlers():
        internal_logger.addHandler(ch)

    return internal_logger


# # Example usage:
if __name__ == "__main__":
    # Only create and use the logger if this module is run as the main script
    logger_showcase = logger = get_logger(__name__, log_level=logging.INFO)
    logger_showcase.debug("This is a debug message")
    logger_showcase.info("This is an info message")
    logger_showcase.warning("This is a warning message")
    logger_showcase.error("This is an error message")
    logger_showcase.critical("This is a critical message")

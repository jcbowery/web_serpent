"""Module for default logger"""

import logging


def setup_logger(
    name: str,
    log_level: str = "INFO",
    log_format: str = "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
):
    """
    Set up a generic logger.

    :param name: The name of the logger (usually the module or file name)
    :param log_level: The logging level (e.g., DEBUG, INFO, WARNING, ERROR, CRITICAL)
    :param log_format: The format for log messages
    :return: A logger instance
    """
    # Create logger
    logger = logging.getLogger(name)

    # Set log level
    logger.setLevel(log_level.upper())

    # Create a console handler and set level
    console_handler = logging.StreamHandler()
    console_handler.setLevel(log_level.upper())

    # Create a formatter and set it for the handler
    formatter = logging.Formatter(log_format)
    console_handler.setFormatter(formatter)

    # Add handler to the logger
    logger.addHandler(console_handler)

    return logger


LOGGER = setup_logger("selenium logger")

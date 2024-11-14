"""Module for enums
"""

from enum import Enum

class BrowserType(Enum):
    """Browser choices for selenium driver
    """
    CHROME = 'chrome'
    FIREFOX = 'firefox'
    SAFARI = 'safari'

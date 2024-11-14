"""Class for Browser Functionalities
"""
from logging import Logger
from typing import Optional

from selenium.webdriver.remote.webdriver import WebDriver

class Browser:
    """The Browser Class
    """
    def __init__(self, driver: WebDriver, logger: Optional[Logger]):
        self._driver = driver
        self._logger = logger

    def refresh(self):
        """refresh the page
        """
        self._logger.info("Refreshing Browser")
        try:
            self._driver.refresh()
        except Exception as e:
            self._logger.error(f"Error occured: {e}")
            raise

    def go_back(self):
        """go back a page
        """
        self._logger.info("Going back a page")
        try:
            self._driver.back()
        except Exception as e:
            self._logger.error(f"Error while going back: {e}")
            raise

    def go_forward(self):
        """for forward a page
        """
        self._logger.info("Going forward a page")
        try:
            self._driver.forward()
        except Exception as e:
            self._logger.error(f"Error while going forward: {e}")
            raise

    def get_title(self) -> str:
        """get the title of the current page

        Returns:
            str: title of page
        """
        self._logger.info("Returning Page Title")
        return self._driver.title

    def get_url(self):
        """get the url of the current page

        Returns:
            str: url of current page
        """
        self._logger.info("Grabbing current url")
        return self._driver.current_url

    def navigate_to(self, url: str):
        """navigate to a given url

        Args:
            url (str): url to navigate to
        """
        self._logger.info(f"Navigating to {url}")
        try:
            self._driver.get(url)
        except Exception as e:
            self._logger.error(f"Error while navigating to page: {e}")
            raise

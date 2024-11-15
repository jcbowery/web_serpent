"""Tests for the Browser Class
"""

import pytest

from webserpent.enums import BrowserType
from webserpent.selenium.browser import Browser

def test_refresh_no_error(mock_driver_manager, mock_driver, mock_logger):
    """testing that refresh method
    """
    mock_driver_manager.get_driver.return_value = mock_driver
    browser = Browser(BrowserType.CHROME, driver_manager=mock_driver_manager, logger=mock_logger)

    browser.refresh()

    mock_driver.refresh.assert_called_once()
    mock_logger.info.assert_called_once()

def test_refresh_with_error(mock_driver_manager, mock_driver, mock_logger):
    """testing refresh method error path
    """
    mock_driver_manager.get_driver.return_value = mock_driver
    mock_driver.refresh.side_effect = ValueError("an error was thrown")
    browser = Browser(BrowserType.CHROME, driver_manager=mock_driver_manager, logger=mock_logger)

    with pytest.raises(ValueError):
        browser.refresh()

    mock_logger.error.assert_called_once()

def test_go_back_no_error(mock_driver_manager, mock_driver, mock_logger):
    """testing go_back method
    """
    mock_driver_manager.get_driver.return_value = mock_driver
    browser = Browser(BrowserType.CHROME, driver_manager=mock_driver_manager, logger=mock_logger)

    browser.go_back()

    mock_driver.back.assert_called_once()
    mock_logger.info.assert_called_once()

def test_go_back_with_error(mock_driver_manager, mock_driver, mock_logger):
    """testing go_back error path
    """
    mock_driver_manager.get_driver.return_value = mock_driver
    mock_driver.back.side_effect = ValueError("an error was thrown")
    browser = Browser(BrowserType.CHROME, driver_manager=mock_driver_manager, logger=mock_logger)

    with pytest.raises(ValueError):
        browser.go_back()

    mock_logger.error.assert_called_once()

def test_go_forward_no_error(mock_driver_manager, mock_driver, mock_logger):
    """testing go_forward method
    """
    mock_driver_manager.get_driver.return_value = mock_driver
    browser = Browser(BrowserType.CHROME, driver_manager=mock_driver_manager, logger=mock_logger)

    browser.go_forward()

    mock_driver.forward.assert_called_once()
    mock_logger.info.assert_called_once()

def test_go_forward_with_error(mock_driver_manager, mock_driver, mock_logger):
    """testing fo_forward error path
    """
    mock_driver_manager.get_driver.return_value = mock_driver
    mock_driver.forward.side_effect = ValueError("an error was thrown")
    browser = Browser(BrowserType.CHROME, driver_manager=mock_driver_manager, logger=mock_logger)

    with pytest.raises(ValueError):
        browser.go_forward()

    mock_logger.error.assert_called_once()

def test_get_title(mock_driver_manager, mock_driver, mock_logger):
    """testing get_title
    """
    mock_driver_manager.get_driver.return_value = mock_driver
    mock_driver.title = "The title"
    browser = Browser(BrowserType.CHROME, driver_manager=mock_driver_manager, logger=mock_logger)

    title = browser.get_title()

    assert title == "The title"
    mock_logger.info.assert_called_once()

def test_get_url(mock_driver_manager, mock_driver, mock_logger):
    """ testing get_url
    """
    mock_driver_manager.get_driver.return_value = mock_driver
    mock_driver.current_url = "www.url.com"
    browser = Browser(BrowserType.CHROME, driver_manager=mock_driver_manager, logger=mock_logger)

    url = browser.get_url()

    assert url == "www.url.com"
    mock_logger.info.assert_called_once()

def test_navigate_to(mock_driver_manager, mock_driver, mock_logger):
    """testing navigate_to
    """
    mock_driver_manager.get_driver.return_value = mock_driver
    browser = Browser(BrowserType.CHROME, driver_manager=mock_driver_manager, logger=mock_logger)
    browser.navigate_to("www.url.com")

    mock_logger.info.assert_called_once()
    mock_driver.get.assert_called_once()

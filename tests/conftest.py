from unittest.mock import MagicMock
import pytest

@pytest.fixture
def mock_driver():
    driver = MagicMock()
    yield driver

@pytest.fixture
def mock_logger():
    logger = MagicMock()
    yield logger

@pytest.fixture
def mock_driver_manager():
    dm = MagicMock()
    yield dm

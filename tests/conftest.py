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

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pytest

@pytest.fixture
def get_driver():
    driver = webdriver.Remote(command_executor='http://127.0.0.1:9515')
    yield driver
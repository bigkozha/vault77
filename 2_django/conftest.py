from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import pytest
import os

@pytest.fixture()
def get_driver():
    if os.environ.get('GITHUB_ACTIONS'):
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
    else:
        driver = webdriver.Remote(command_executor='http://127.0.0.1:9515')
    yield driver
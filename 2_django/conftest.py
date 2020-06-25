import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture()
def get_driver():
    if os.environ.get('GITHUB_ACTIONS'):
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        driver = webdriver.Chrome(chrome_options=chrome_options)
    else:
        driver = webdriver.Remote(command_executor='http://127.0.0.1:9515')
    yield driver

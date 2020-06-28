import os

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from counter.models import Counter


@pytest.yield_fixture(scope="session")
def driver():
    if os.environ.get('GITHUB_ACTIONS'):
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        with webdriver.Chrome(chrome_options=chrome_options) as driver:
            yield driver
    else:
        with webdriver.Remote(command_executor='http://127.0.0.1:9515') as driver:
            yield driver


@pytest.fixture()
def counter():
    instance, created = Counter.objects.get_or_create(id=1)
    instance.value += 1
    instance.save()
    return instance

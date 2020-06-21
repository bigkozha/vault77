from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pytest
import pytest
from counter.models import Counter

@pytest.yield_fixture(scope="session")
def get_driver():
    with webdriver.Remote(command_executor='http://127.0.0.1:9515') as driver:
        yield driver

@pytest.fixture()
def get_counter():
    instance, created = Counter.objects.get_or_create(id=1)
    instance.value += 1
    instance.save()
    return instance
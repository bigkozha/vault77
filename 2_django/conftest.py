import os
import pytest
import pytest
from counter.models import Counter

@pytest.yield_fixture(scope="session")
def driver():
    with webdriver.Remote(command_executor='http://127.0.0.1:9515') as driver:
        yield driver

@pytest.fixture()
def counter():
    instance, created = Counter.objects.get_or_create(id=1)
    instance.value += 1
    instance.save()
    return instance

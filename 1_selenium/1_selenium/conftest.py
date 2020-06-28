import pytest


@pytest.fixture
def expected_query_word():
    return 'nuraly zhanbyrbayev'


@pytest.fixture
def expected_title_google():
    return 'Google'


@pytest.fixture
def expected_search_result():
    return [
        'Nuraly Zhanbyrbayev - Kazakhstan | Professional Profile ...', 'Nuraly Zhanbyrbayev (@z.nuraly) • Instagram photos and videos',
        'Нуралы Жанбырбаев | Facebook', 'Нуралы Жанбырбаев | Facebook', 'Nuraly Zhanbyrbayev - Middle .NET Developer - Upwork ...']

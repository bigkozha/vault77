import pytest


@pytest.fixture
def mock_query_word():
    return 'nuraly zhanbyrbayev'


@pytest.fixture
def mock_title_google():
    return 'Google'


@pytest.fixture
def mock_search_result():
    return ['Link 1', 'Link 2', 'Link 3', 'Link 4', 'Link 5', 'Link 6']

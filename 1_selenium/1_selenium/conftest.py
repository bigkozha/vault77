import pytest


@pytest.fixture
def mock_tuple():
    return (mock_query_word, mock_title_google, mock_search_result)


def mock_query_word():
    return 'nuraly zhanbyrbayev'


def mock_title_google():
    return 'Google'


def mock_search_result():
    return ['Link 1', 'Link 2', 'Link 3', 'Link 4', 'Link 5', 'Link 6']

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


def test_google(mock_query_word, mock_title_google, mock_search_result):
    query_word = mock_query_word
    driver = webdriver.Remote(command_executor='127.0.0.1:9515')

    driver.get('https://google.kz')
    assert 'Google' == mock_title_google

    # get search results
    search_result = driver.find_element_by_name('q')
    search_result.send_keys(query_word)
    search_result.send_keys(Keys.RETURN)

    # get first 5 links text
    first_five_links = mock_search_result[:5]
    assert(len(first_five_links) == 5)
    assert(None not in first_five_links)\

    driver.close()

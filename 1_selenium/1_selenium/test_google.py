from selenium import webdriver
from selenium.webdriver.common.keys import Keys


def test_google(mock_tuple):
    search_result_class_name = '.LC20lb.DKV0Md'
    query_word = mock_tuple[0]()

    driver = webdriver.Remote(command_executor='127.0.0.1:9515')
    driver.get('https://google.kz')
    assert 'Google' == mock_tuple[1]()

    # get search results
    search_box = driver.find_element_by_name('q')
    search_box.send_keys(query_word)
    search_box.send_keys(Keys.RETURN)

    # get first 5 links text
    first_five_links = mock_tuple[2]()[:5]
    assert(len(first_five_links) == 5)
    assert(None not in first_five_links)

    driver.close()

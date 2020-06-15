from selenium import webdriver
from selenium.webdriver.common.keys import Keys


def test_google(expected_query_word, expected_title_google, expected_search_result):
    search_result_class_name = '.LC20lb.DKV0Md'
    query_word = expected_query_word
    driver = webdriver.Remote(command_executor='127.0.0.1:9515')

    driver.get('https://google.kz')
    assert 'Google' == expected_title_google

    # get search results
    search_result = driver.find_element_by_name('q')
    search_result.send_keys(query_word)
    search_result.send_keys(Keys.RETURN)

    # get first 5 links text
    first_five_links = driver.find_elements_by_css_selector(search_result_class_name)[:5]
    expeceted_five_links = expected_search_result
    assert(len(first_five_links) == 5)
    assert(None not in first_five_links)

    for i in range(5):
        assert first_five_links[i].text == expeceted_five_links[i]

    driver.close()

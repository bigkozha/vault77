import pytest



def test_basic(live_server, get_driver):
    with get_driver as driver:
        driver.get(live_server.url)
    
        counter = driver.find_element_by_id('counter')
        assert '1' == counter.text
        driver.refresh()
        counter = driver.find_element_by_id('counter')
        assert '2' == counter.text
        driver.close()
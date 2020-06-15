from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def test_basic():
    driver = webdriver.Remote(command_executor='http://127.0.0.1:9515')
    driver.get('http://127.0.0.1:8000/')
    
    counter = driver.find_element_by_id('counter')
    assert '1' == counter.text
    driver.refresh()
    counter = driver.find_element_by_id('counter')
    assert '2' == counter.text
    driver.close()
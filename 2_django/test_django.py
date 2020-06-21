import pytest


def test_basic(live_server, get_driver):
    driver = get_driver
    driver.get(live_server.url)
    counter = driver.find_element_by_id('counter')
    assert '0' == counter.text


def test_increment(live_server, get_driver, get_counter):
    driver = get_driver
    driver.get(live_server.url + '/increment')
    counter = driver.find_element_by_id('counter')
    assert '2' == counter.text


def test_decrement(live_server, get_driver, get_counter):
    driver = get_driver
    driver.get(live_server.url + '/decrement')
    counter = driver.find_element_by_id('counter')
    assert '0' == counter.text


def test_decrement_instance_value_zero(live_server, get_driver, get_counter):
    instance = get_counter
    instance.value = 0
    instance.save()

    driver = get_driver
    driver.get(live_server.url + '/decrement')
    assert 'error' in driver.current_url

import pytest


def test_basic(live_server, driver):
    driver.get(live_server.url)
    elem_counter = driver.find_element_by_id('counter')
    assert '0' == elem_counter.text


def test_increment(live_server, driver, counter):
    driver.get(live_server.url + '/increment')
    elem_counter = driver.find_element_by_id('counter')
    assert '2' == elem_counter.text


def test_decrement(live_server, driver, counter):
    driver.get(live_server.url + '/decrement')
    elem_counter = driver.find_element_by_id('counter')
    assert '0' == elem_counter.text


def test_decrement_instance_value_zero(live_server, driver, counter):
    counter.value = 0
    counter.save()

    driver.get(live_server.url + '/decrement')
    assert 'error' in driver.current_url

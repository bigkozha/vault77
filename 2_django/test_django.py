from counter.models import Counter


def test_basic(live_server, get_driver):
    with get_driver as driver:
        driver.get(live_server.url)

        counter = driver.find_element_by_id('counter')
        assert '0' == counter.text


def test_increment(live_server, get_driver):
    instance, created = Counter.objects.get_or_create(id=1)
    instance.value += 1
    instance.save()
    assert 1 == instance.value

    with get_driver as driver:
        driver.get(live_server.url + '/increment')
        counter = driver.find_element_by_id('counter')
        assert '2' == counter.text


def test_decrement(live_server, get_driver):
    instance, created = Counter.objects.get_or_create(id=1)
    instance.value += 1
    instance.save()
    assert 1 == instance.value

    with get_driver as driver:
        driver.get(live_server.url + '/decrement')
        counter = driver.find_element_by_id('counter')
        assert '0' == counter.text


def test_decrement_instance_value_zero(live_server, get_driver):
    instance, created = Counter.objects.get_or_create(id=1)
    instance.value = 0
    instance.save()
    assert 0 == instance.value
    
    with get_driver as driver:
        driver.get(live_server.url + '/decrement')
        assert 'error' in driver.current_url

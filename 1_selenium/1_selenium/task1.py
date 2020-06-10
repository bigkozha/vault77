from selenium import webdriver
from selenium.webdriver.common.keys import Keys

LINK_CLASS_NAME = '.LC20lb.DKV0Md'
QUERY_WORD = 'nuraly zhanbyrbayev'

driver = webdriver.Remote(command_executor='127.0.0.1:9515')
driver.get('https://google.kz')
assert 'Google' in driver.title

#get search results
elementQ = driver.find_element_by_name('q')
elementQ.send_keys(QUERY_WORD)
elementQ.send_keys(Keys.RETURN)

#get first 5 links text 
first_five_links = driver.find_elements_by_css_selector(LINK_CLASS_NAME)[:5]
assert(len(first_five_links) == 5)
assert(None not in first_five_links)

for link in first_five_links:
    print(link.text)

driver.close()
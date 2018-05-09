from selenium import webdriver
from selenium.common.exceptions import TimeoutException, NoSuchElementException

driver = webdriver.Chrome()

try:
	driver.get('http://www.baidu.com')
except TimeoutException:
	print('time out')

try:
	driver.find_element_by_id('hello')
except NoSuchElementException:
	print('no such element')

driver.close()

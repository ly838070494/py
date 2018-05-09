from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get('http://www.baidu.com')
input = driver.find_element_by_id('kw')
input.clear()
input.send_keys('python')
input.send_keys(Keys.ENTER)
time.sleep(5)
driver.quit()


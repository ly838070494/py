from selenium import webdriver

import time

browser = webdriver.Chrome()
browser.get("http://www.taobao.com")
time.sleep(3)
input_str = browser.find_element_by_id('q')
input_str.send_keys("ipad")
time.sleep(10)
input_str.clear()
input_str.send_keys("MakBook pro")
button = browser.find_element_by_class_name('btn-search')
button.click()
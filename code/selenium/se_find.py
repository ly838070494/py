from selenium import webdriver

driver = webdriver.Chrome()
driver.get('http://www.taobao.com')

input_first = driver.find_element_by_id('q')
input_second = driver.find_element_by_css_selector('#q')
print(input_first)
print(input_second)
driver.close()
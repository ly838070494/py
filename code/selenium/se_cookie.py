from selenium import webdriver

driver = webdriver.Chrome()
driver.get('http://www.zhihu.com/explore')
print(driver.get_cookies())
driver.add_cookie({'name':'name', 'domain':'www.zhihu.com', 'value':'zhaofen'})
print(driver.get_cookies())
driver.delete_all_cookies()
print(driver.get_cookies())
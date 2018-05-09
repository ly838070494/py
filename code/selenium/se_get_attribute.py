from selenium import webdriver

driver = webdriver.Chrome()
driver.get('http://www.zhihu.com/explore')
logo = driver.find_element_by_id('zh-top-link-logo')
print(logo)

print(logo.get_attribute('class'))
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('http://www.taobao.com')
#单个元素
#input = driver.find_element(By.ID, 'q')
#input = driver.find_element(By.NAME, 'q')

#多个元素
inputs = driver.find_elements(By.CSS_SELECTOR, '.service-bd li')

print(inputs)
driver.close()
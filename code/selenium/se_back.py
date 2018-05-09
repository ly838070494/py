import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.get('http://www.baidu.com')
driver.get('http://www.zhihu.com/explore')
driver.get('http://www.taobao.com')
driver.back()
time.sleep(3)
driver.forward()
time.sleep(5)
driver.close()
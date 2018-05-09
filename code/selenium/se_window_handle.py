import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.get('http://www.baidu.com')
driver.execute_script('window.open()') #打开选项卡
print(driver.window_handles) #查看选项卡
driver.switch_to_window(driver.window_handles[1])
driver.get('http://www.taobao.com')
time.sleep(3)
driver.switch_to_window(driver.window_handles[0])
driver.get('http://www.zhihu.com/explore')

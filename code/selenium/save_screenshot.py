from selenium import webdriver
driver = webdriver.Chrome()
driver.get('http://www.baidu.com')
driver.save_screenshot('screen.png')
driver.quit()
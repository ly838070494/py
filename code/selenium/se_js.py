from selenium import webdriver

driver = webdriver.Chrome()
driver.get('http://www.zhihu.com/explore')
driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')
driver.execute_script('alert("To Bottom")')

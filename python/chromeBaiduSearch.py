# -*- coding: utf-8 -*-
from selenium import webdriver
driver = webdriver.Chrome()
driver.get('http://www.baidu.com/')

#<input type="submit" id="su" value="百度一下" class="bg s_btn">
#<input id="kw" name="wd" class="s_ipt" value="" maxlength="255" autocomplete="off">

driver.find_element_by_id("kw").send_keys("python")
driver.find_element_by_id("su").submit()

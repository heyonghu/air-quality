#!/usr/bin/env python
#-*- coding:utf-8 -*-
#python 3

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

link='https://air-quality.com/place/china/shanghai/4e4d63c9?lang=zh-Hans&standard=aqi_cn'
driver = webdriver.PhantomJS()
driver.implicitly_wait(10)
driver.get(link)

action = ActionChains(driver)
element1=driver.find_element_by_xpath('//*[@id="item_0"]')
element2=driver.find_element_by_xpath('//*[@id="item_1"]')
element3=driver.find_element_by_xpath('//*[@id="item_14"]')
element=driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[8]/div[4]')
for i in range(0,71):
    #action.move_to_element(locals()[name]).perform()
    action.move_to_element(driver.find_element_by_id('item_'+str(i))).perform()
    #目前这个会报错：1.用xpath找到的和页面上显示的最早时间不一致；2.不能用71最为最大值，需要自动去判断
    value=element.text
    print(value)



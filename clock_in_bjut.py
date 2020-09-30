# -*- coding: utf-8 -*-
'''
Created on 2020-09-30-08:37:37
@Author:qianc
'''

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains


def login():
    url = 'https://itsapp.bjut.edu.cn/uc/wap/login?redirect=https%3A%2F%2Fitsapp.bjut.edu.cn%2Fsite%2FapplicationSquare%2Findex%3Fsid%3D1'
    browser.get(url)

    browser.find_element_by_xpath('//*[@id="app"]/div[2]/div[1]/input').send_keys('your id')
    browser.find_element_by_xpath('//*[@id="app"]/div[2]/div[2]/input').send_keys('your password')
    browser.find_element_by_xpath('//*[@id="app"]/div[3]').click()
    browser.maximize_window()

    action = ActionChains(browser)
    action.move_by_offset(750, 387).click().perform()
    browser.find_element_by_xpath('/html/body/div[1]/div/div/section/div[4]/ul/li[7]/div/input').click()
    browser.find_element_by_xpath('/html/body/div[1]/div/div/section/div[5]/div/a').click()


if __name__ == '__main__':
    chromedriver = 'C:\Program Files (x86)\Google\Chrome\Application\chromedriver'
    browser = webdriver.Chrome(chromedriver)
    login()

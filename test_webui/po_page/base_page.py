# -*- coding: utf-8 -*-
# @Author : lun
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webdriver import WebDriver


class BasePage:
    _base_url = ""
    def __init__(self, driver:WebDriver = None):
        if driver == None:
            option = Options()
            option.debugger_address = "localhost:9222"
            self._driver = webdriver.Chrome(options=option)
            #self._driver = webdriver.Chrome()
        else:
            self._driver = driver

        if self._base_url != "":
            self._driver.get(self._base_url)
        self._driver.implicitly_wait(5)

    def find(self, by, locator):
        return self._driver.find_element(by, locator)

    def quit(self):
        return self._driver.quit()

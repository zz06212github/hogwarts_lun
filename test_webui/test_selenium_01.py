# -*- coding: utf-8 -*-
# @Author : lun
import shelve
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


class TestSelenium:
    def setup(self):
        # option = Options()
        # option.debugger_address = "localhost:9222"
        # self.driver = webdriver.Chrome(options=option)
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def test_cookies(self):
        # cookies = self.driver.get_cookies()
        db = shelve.open("mydb/logincookies")
        # db["cookie"] = cookies
        cookies = db["cookie"]
        db.close()
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        for cookie in cookies:
            self.driver.add_cookie(cookie)
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        self.driver.find_element(By.LINK_TEXT, '导入通讯录').click()
        self.driver.find_element(By.CSS_SELECTOR, '.ww_fileImporter_fileContainer_uploadInputMask').send_keys("D:\python_projects\hogwarts_lun\\test_webui\\test_01.xlsx")
        xlsx_filename = self.driver.find_element(By.CSS_SELECTOR, '.ww_fileImporter_fileContainer_fileNames').text
        assert xlsx_filename == 'test_01.xlsx'
# -*- coding: utf-8 -*-
# @Author : lun
from selenium.webdriver.common.by import By

from test_webui.po_page.base_page import BasePage
from test_webui.po_page.main_page import MainPage
from test_webui.po_page.register_page import RegisterPage


class LoginPage(BasePage):
    _base_url = "https://work.weixin.qq.com/"
    def goto_register_page(self):
        self.find(By.CSS_SELECTOR, ".index_head_info_pCDownloadBtn").click()
        return RegisterPage(self._driver)

    def goto_main_page(self):
        self.find(By.CSS_SELECTOR, ".index_top_operation_loginBtn").click()
        # self.find(By.LINK_TEXT, "企业登录").click()

        return MainPage(self._driver)
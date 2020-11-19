# -*- coding: utf-8 -*-
# @Author : lun
from selenium.webdriver.common.by import By

from test_webui.po_page.base_page import BasePage


class AdddepartmentPage(BasePage):
    def adddepartment(self):
        self.find(By.CSS_SELECTOR, "[name='name']").send_keys("lun_01")
        self.find(By.CSS_SELECTOR, ".js_parent_party_name").click()
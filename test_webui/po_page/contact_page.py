# -*- coding: utf-8 -*-
# @Author : lun
from selenium.webdriver.common.by import By

from test_webui.po_page.adddepartment_page import AdddepartmentPage
from test_webui.po_page.addmember_page import AddmemberPage
from test_webui.po_page.base_page import BasePage
from test_webui.po_page.import_contact_page import ImportContactPage


class ContactPage(BasePage):
    def goto_addmember_page(self):
        return AddmemberPage(self._driver)

    def goto_adddepartment_page(self):
        self.find(By.CSS_SELECTOR, ".member_colLeft_top_addBtn").click()
        self.find(By.CSS_SELECTOR, ".js_create_party").click()
        return AdddepartmentPage(self._driver)

    def goto_importcontact_page(self):
        return ImportContactPage(self._driver)

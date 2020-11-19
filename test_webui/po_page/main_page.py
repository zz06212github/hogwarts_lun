# -*- coding: utf-8 -*-
# @Author : lun
from selenium.webdriver.common.by import By

from test_webui.po_page.addmember_page import AddmemberPage
from test_webui.po_page.base_page import BasePage
from test_webui.po_page.contact_page import ContactPage
from test_webui.po_page.import_contact_page import ImportContactPage


class MainPage(BasePage):

    def goto_contact_page(self):
        self.find(By.CSS_SELECTOR, "#menu_contacts .frame_nav_item_title").click()
        return ContactPage()

    def goto_addmember_page(self):
        return AddmemberPage()

    def goto_importcontact_page(self):
        return ImportContactPage(self._driver)

    def assert_true(self):
        return True

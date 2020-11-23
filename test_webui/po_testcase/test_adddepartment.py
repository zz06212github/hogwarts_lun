# -*- coding: utf-8 -*-
# @Author : lun
from test_webui.po_page.login_page import LoginPage


class TestAdddepartment:
    def setup(self):
        self.login = LoginPage()

    def test_adddepartment(self):
        result = self.login.goto_main_page().goto_contact_page().goto_adddepartment_page().adddepartment("3")
        assert result == "3"
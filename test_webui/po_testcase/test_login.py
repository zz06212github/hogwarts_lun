# -*- coding: utf-8 -*-
# @Author : lun
from test_webui.po_page.login_page import LoginPage


class TestLogin:
    def setup_class(self):
        self.login = LoginPage()

    def teardown_class(self):
        self.login.quit()

    def test_login(self):
        self.login.goto_main_page().assert_true()


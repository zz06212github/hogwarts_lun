# -*- coding: utf-8 -*-
# @Author : lun
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from test_webui.po_page.base_page import BasePage



class AdddepartmentPage(BasePage):
    def adddepartment(self,party_name):
        self.find(By.CSS_SELECTOR, "[name='name']").send_keys(party_name)
        self.find(By.CSS_SELECTOR, ".js_parent_party_name").click()
        self.find(By.CSS_SELECTOR, "[class='qui_dialog_body ww_dialog_body'] [id='1688850088083179_anchor']").click()
        self.find(By.CSS_SELECTOR, "[d_ck='submit']").click()
        self.webdriver_wait(5, expected_conditions.element_to_be_clickable, By.CSS_SELECTOR, "[class='member_colRight_cnt_operation'] [class='qui_btn ww_btn js_add_member']")
        result = self.find(By.CSS_SELECTOR, "#party_name").text
        return result
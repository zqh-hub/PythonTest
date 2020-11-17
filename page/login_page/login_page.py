from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from locator.login_loc.login_page_loc import LoginPageLocator as loc
from common.base_page import BasePage


class LoginPage(BasePage):
    # 正常登录
    def login(self, username, password):
        doc = "登录页面_登录功能"
        self.wait_element_visible(loc.user_txt, doc=doc)
        self.input_text(loc.user_txt, username, doc=doc)
        self.wait_element_visible(loc.pwd_txt, doc=doc)
        self.input_text(loc.pwd_txt, password, doc=doc)
        self.wait_element_visible(loc.login_but, doc=doc)
        self.click_element(loc.login_but, doc=doc)

    # 获取错误的提示信息
    def get_middle_error_info(self):
        doc = "登录页面_获取提示信息"
        self.wait_element_visible(loc.middle_error_info, doc=doc)
        info = self.get_text(loc.middle_error_info, doc=doc)
        print(info)
        return info

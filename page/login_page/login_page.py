from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from locator.login_loc.login_page_loc import LoginPageLocator as loc


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        # self.driver = webdriver.Chrome()

    # 正常登录
    def login(self, username, password):
        WebDriverWait(self.driver, 20).until(ec.visibility_of_element_located(loc.user_txt))
        self.driver.find_element(*loc.user_txt).send_keys(username)
        WebDriverWait(self.driver, 20).until(ec.visibility_of_element_located(loc.pwd_txt))
        self.driver.find_element(*loc.pwd_txt).send_keys(password)
        WebDriverWait(self.driver, 20).until(ec.visibility_of_element_located(loc.login_but))
        self.driver.find_element(*loc.login_but).click()

    # 获取错误的提示信息
    def get_middle_error_info(self):
        WebDriverWait(self.driver, 20).until(ec.visibility_of_element_located(loc.middle_error_info))
        info = self.driver.find_element(*loc.middle_error_info).text
        print(info)
        return info

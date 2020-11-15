from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from locator.login_loc.index_page_loc import IndexPageLocator as loc
from time import sleep


class IndexPage:
    def __init__(self, driver):
        self.driver = driver
        # self.driver = webdriver.Chrome()

    def is_exist_user_login_name(self):
        WebDriverWait(self.driver, 20).until(ec.visibility_of_element_located(loc.user_login_name))
        return self.driver.find_element(*loc.user_login_name)

    # 点击导航栏-前置系统-数据上传
    def click_nav_data_upload(self):
        WebDriverWait(self.driver, 20).until(ec.visibility_of_element_located(loc.nav_font_system))
        self.driver.find_element(*loc.nav_font_system).click()
        WebDriverWait(self.driver, 20).until(ec.visibility_of_element_located(loc.nav_font_system_data_upload))
        self.driver.find_element(*loc.nav_font_system_data_upload).click()

    # 关闭inner_iframe
    def close_inner_iframe_tab(self):
        WebDriverWait(self.driver, 20).until(ec.visibility_of_element_located(loc.close_tab))
        self.driver.find_element(*loc.close_tab).click()
        self.driver.switch_to.alert.accept()
        sleep(6)

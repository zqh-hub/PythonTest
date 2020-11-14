from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class IndexPage:
    def __init__(self, driver):
        self.driver = driver
        # self.driver = webdriver.Chrome()

    def is_exist_user_login_name(self):
        user_login_name = "//span[@id='user_login_name']"
        WebDriverWait(self.driver, 20).until(ec.visibility_of_element_located((By.XPATH, user_login_name)))
        return self.driver.find_element_by_xpath(user_login_name)

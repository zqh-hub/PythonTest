from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        # self.driver = webdriver.Chrome()

    # 正常登录
    def login(self, username, password):
        user_txt = "//input[@id='uname']"
        pwd_txt = "//input[@id='pwd']"
        login_but = "//button[@id='login_button']"
        WebDriverWait(self.driver, 20).until(ec.visibility_of_element_located((By.XPATH, user_txt)))
        self.driver.find_element_by_xpath(user_txt).send_keys(username)
        WebDriverWait(self.driver, 20).until(ec.visibility_of_element_located((By.XPATH, pwd_txt)))
        self.driver.find_element_by_xpath(pwd_txt).send_keys(password)
        WebDriverWait(self.driver, 20).until(ec.visibility_of_element_located((By.XPATH, login_but)))
        self.driver.find_element_by_xpath(login_but).click()

    # 获取错误的提示信息
    def get_middle_error_info(self):
        middle_error_info = "//div[@class='ui-dialog-content']"
        WebDriverWait(self.driver, 20).until(ec.visibility_of_element_located((By.XPATH, middle_error_info)))
        info = self.driver.find_element_by_xpath(middle_error_info).text
        print(info)
        return info

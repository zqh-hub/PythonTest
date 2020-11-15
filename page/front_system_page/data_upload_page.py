from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from locator.front_system_loc.data_upload_loc import DataUploadPageLocator as loc
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class DataUploadPage:
    def __init__(self, driver):
        self.driver = driver
        # self.driver = webdriver.Chrome()

    # 切换iframe
    def switch_iframe(self):
        iframe_ele = self.driver.find_element(*loc.iframe)
        self.driver.switch_to.frame(iframe_ele)

    # 点击 通用信息导入
    def click_general_info_import(self):
        WebDriverWait(self.driver, 20).until(ec.visibility_of_element_located(loc.general_info_import))
        self.driver.find_element(*loc.general_info_import).click()

    # 选择商户
    def choose_merchant(self, merchant):
        WebDriverWait(self.driver, 20).until(ec.visibility_of_element_located(loc.choose_merchant))
        ele = self.driver.find_element(*loc.choose_merchant)
        self.driver.execute_script("arguments[0].readonly=false", ele)
        ele.send_keys(merchant, Keys.ENTER)

    # 批次名称
    def input_batch_name(self, batch_name):
        WebDriverWait(self.driver, 20).until(ec.visibility_of_element_located(loc.batch_name))
        ele = self.driver.find_element(*loc.batch_name)
        ele.clear()
        ele.send_keys(batch_name)

    #
    def input_product_number(self, product_number):
        WebDriverWait(self.driver, 20).until(ec.visibility_of_element_located(loc.product_number))
        self.driver.find_element(*loc.product_number).send_keys(product_number)

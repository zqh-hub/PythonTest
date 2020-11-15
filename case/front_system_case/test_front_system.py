import unittest
from selenium import webdriver
from data import common_data
from page.login_page.login_page import LoginPage
from data.login_data import login_data
from page.login_page.index_page import IndexPage
from page.front_system_page.data_upload_page import DataUploadPage
from data.front_system_data import data_upload_data
from time import sleep


class TestFrontSystem(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(common_data.web_driver_path)
        cls.driver.get(common_data.web_login_url)
        cls.driver.maximize_window()
        cls.index_page = IndexPage(cls.driver)
        cls.login_page = LoginPage(cls.driver)
        cls.data_upload_page = DataUploadPage(cls.driver)
        cls.login_page.login(login_data.success_data["user"], login_data.success_data["password"])

    def test_success_data_upload(self):
        self.index_page.click_nav_data_upload()
        self.index_page.close_inner_iframe_tab()
        self.data_upload_page.switch_iframe()
        print("123")
        self.data_upload_page.click_general_info_import()
        self.data_upload_page.choose_merchant(data_upload_data.merchant)
        self.data_upload_page.input_batch_name(data_upload_data.batch_name)
        self.data_upload_page.input_product_number(data_upload_data.product_number)

    def tearDown(self):
        self.driver.refresh()

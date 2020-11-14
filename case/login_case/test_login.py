import ddt
import unittest

from selenium import webdriver
from Data import common_data
from Data.login_data import login_data
from Page.login_page.index_page import IndexPage
from Page.login_page.login_page import LoginPage


@ddt.ddt
class TestLoginCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(common_data.web_driver_path)
        self.driver.get(common_data.web_login_url)
        self.driver.maximize_window()
        self.login_page = LoginPage(self.driver)
        self.index_page = IndexPage(self.driver)

    def tearDown(self):
        self.driver.quit()

    def test_login_success(self):
        self.login_page.login(login_data.success_data["user"], login_data.success_data["password"])
        self.assertTrue(self.index_page.is_exist_user_login_name())

    @ddt.data(*login_data.error_data)
    def test_error_info_middle(self, data):
        self.login_page.login(data["user"], data["password"])
        middle_error_info = self.login_page.get_middle_error_info()
        self.assertEqual(middle_error_info, data["message"])

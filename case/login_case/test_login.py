import ddt
import unittest
from data import common_data
from selenium import webdriver
from data.login_data import login_data
from page.login_page.index_page import IndexPage
from page.login_page.login_page import LoginPage


@ddt.ddt
class TestLoginCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(common_data.web_driver_path)
        cls.driver.get(common_data.web_login_url)
        cls.driver.maximize_window()
        cls.login_page = LoginPage(cls.driver)
        cls.index_page = IndexPage(cls.driver)

    def test_login_success(self):
        self.login_page.login(login_data.success_data["user"], login_data.success_data["password"])
        self.assertTrue(self.index_page.is_exist_user_login_name())

    @ddt.data(*login_data.error_data)
    def test_error_info_middle(self, data):
        self.login_page.login(data["user"], data["password"])
        middle_error_info = self.login_page.get_middle_error_info()
        self.assertEqual(middle_error_info, data["message"])

    def tearDown(self):
        self.driver.refresh()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

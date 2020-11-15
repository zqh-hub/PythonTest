import logging
import datetime
import time
import os
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        # self.driver = webdriver.Chrome()

    def wait_element_visible(self, locator, wait_time=10, poll_frequency=0.5, doc=""):
        """ 等待元素可见

        :param locator: 定位
        :param wait_time: 等待时间
        :param poll_frequency: 等待刷新频率
        :param doc: 模块名_页面名称_操作名称
        :return:
        """
        logging.info("等待元素{0}可见".format(locator))
        try:
            start = datetime.datetime.now()
            WebDriverWait(self.driver, wait_time, poll_frequency).until(ec.visibility_of_element_located(locator))
            end = datetime.datetime.now()
            logging.info("等待结束，时长：{}".format(end - start))
        except:
            logging.exception("等待元素可见失败")
            # 截图
            self.save_screen(doc)
            raise

    # 等待元素存在
    def wait_element_presence(self):
        pass

    def get_element(self, locator, doc=""):
        """获取元素

        :param locator: 定位
        :param doc: 模块名_页面名称_操作名称
        :return: element
        """
        logging.info("查找元素：{}".format(locator))
        try:
            return self.driver.find_element(*locator)
        except:
            logging.exception("查找元素失败")
            # 截图
            self.save_screen(doc)
            raise

    def click_element(self, locator, doc=""):
        """ 点击元素

        :param locator: 定位
        :param doc: 模块名_页面名称_操作名称
        :return:
        """
        element = self.get_element(locator, doc)
        logging.info("点击元素：{}".format(locator))
        try:
            element.click()
        except:
            logging.exception("元素点击失败")
            self.save_screen(doc)
            raise

    def input_text(self, locator, text, doc=""):
        """ 输入文本

        :param locator: 定位
        :param text: 文本值
        :param doc: 模块名_页面名称_操作名称
        :return:
        """
        element = self.get_element(locator, doc="")
        logging.info("向元素：{}，输入文本".format(locator))
        try:
            element.send_keys(text)
        except:
            logging.exception("输入文本失败")
            self.save_screen(doc)
            raise

    def get_text(self, locator, doc=""):
        """ 获取文本

        :param locator: 定位
        :param doc: 模块名_页面名称_操作名称
        :return: 文本值
        """
        element = self.get_element(locator, doc)
        logging.info("获取{}的文本值".format(locator))
        try:
            return element.text
        except:
            logging.exception("获取文本失败")
            self.save_screen(doc)
            raise

    def get_element_attribute(self, locator, attr, doc):
        """ 获取元素属性

        :param locator: 定位
        :param attr: 属性
        :param doc: 模块名_页面名称_操作名称
        :return: 属性值
        """
        element = self.get_element(locator, doc)
        logging.info("获取{0}的{1}属性值".format(locator, attr))
        try:
            return element.get_attribute(attr)
        except:
            logging.exception("获取属性值失败")
            self.save_screen(doc)
            raise

    # alter处理
    def alert_action(self, action="accept"):
        pass

    # iframe切换
    def switch_iframe(self, iframe_reference):
        pass

    # 截图
    def save_screen(self, name):
        # 图片的名称：模块名_页面名称_操作名称_年-月-日_时分秒.png
        '''
        shot_time = time.strftime("%Y-%m-%d_%H%M%S")
        file_name = "{0}_{1}.png".format(name, shot_time)
        self.driver.save_screenshot(file_name)
        os.path.abspath()
        '''
        pass

from selenium.webdriver.common.by import By


class IndexPageLocator:
    # 用户名
    user_login_name = (By.XPATH, "//span[@id='user_login_name']")
    # 导航栏-前置系统
    nav_font_system = (By.XPATH, "//a[@data-id='MFSH010000']")
    # 导航栏-前置系统-数据上传
    nav_font_system_data_upload = (By.XPATH, "//a[@data-id='MFSP010001']")
    # 获取inner_iframe
    inner_iframe = (By.XPATH, "//iframe[@class='inneriframe']")
    # 关闭前一个tab
    close_tab = (By.XPATH, "//ul[@role='tablist']/li[1]/a[2]")

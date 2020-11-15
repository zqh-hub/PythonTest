from selenium.webdriver.common.by import By


class LoginPageLocator:
    # 用户名输入
    user_txt = (By.XPATH, "//input[@id='uname']")
    # 密码输入
    pwd_txt = (By.XPATH, "//input[@id='pwd']")
    # 登录按钮
    login_but = (By.XPATH, "//button[@id='login_button']")
    # 错误信息提示框
    middle_error_info = (By.XPATH, "//div[@class='ui-dialog-content']")

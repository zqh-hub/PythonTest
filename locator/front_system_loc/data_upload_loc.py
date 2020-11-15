from selenium.webdriver.common.by import By


class DataUploadPageLocator:
    # iframe
    iframe = (By.XPATH, "//iframe[@class='inneriframe']")
    # 通用信息导入
    general_info_import = (By.XPATH, "// span[contains(text(), '通用信息导入')]")
    # 选择商户
    choose_merchant = (
        By.XPATH, "//label[@for='merchantNo']/following-sibling::div[@class='el-form-item__content']//input")
    # 批次名称
    batch_name = (
        By.XPATH, "//label[@for='importBatchNo']/following-sibling::div[@class='el-form-item__content']//input")
    # 产品编号
    product_number = (
        By.XPATH, "//label[@for='productName']/following-sibling::div[@class='el-form-item__content']//input")

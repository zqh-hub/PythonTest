# success 登录
success_data = {"user": "ITADMIN", "password": "000000"}

# 异常用例 -- 无用户名,错误用户名,密码不正确,无密码
error_data = [
    {"user": "", "password": "", "message": "请输入用户名"},  # 无用户名
    {"user": "ITADMI", "password": "000000", "message": "用户不存在"},  # 错误用户名
    {"user": "ITADMIN", "password": "123", "message": "密码输入错误，请重新输入"},  # 密码不正确
    {"user": "ITADMIN", "password": "", "message": "请正确完成此项目"},  # 无密码
]

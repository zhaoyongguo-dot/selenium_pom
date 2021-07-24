# -*- coding:utf-8 -*-
"""
@author: zyg
@file: page_login.py
@time: 2021/7/21 下午 11:44
@desc: 
"""
from selenium import webdriver
from selenium.webdriver.common.by import By

from base.base_page import BasePage

"""
    LoginPage类,用于实现登录页面对象的文件
    主体内容包含:
        1,核心页面元素
            账号,密码,登录按钮
        2,核心业务流
            用户的登录行为  
"""


class LoginPage(BasePage):
    # 核心元素
    url = 'http://47.107.116.139/phpwind/index.php?m=u&c=login/'
    # 参数传入元组是为了人便于管理,元素定位需要两个参数,定位方法和定位对象
    user = (By.NAME, 'username')
    password = (By.NAME, 'password')
    login_button = (By.CLASS_NAME, 'btn.btn_big.btn_submit.mr20')

    # 核心业务流
    def login(self, username, pwd):
        # self.visit(self.url) # url不在这里传,每次都要写,所以直接写死,-----见visit()
        self.visit()
        self.input(self.user, username)  # self指当前类,self.user----user参数,username是txt
        self.input(self.password, pwd)
        self.click(self.login_button)

# if __name__ == '__main__':
#     driver = webdriver.Chrome()
#     username = 'zyg'
#     password = '123456'
#     lp = LoginPage(driver)
#     lp.login(username, password)

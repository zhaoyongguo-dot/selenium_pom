# -*- coding:utf-8 -*-
"""
@author: zyg
@file: base_page.py
@time: 2021/7/21 下午 11:14
@desc: 
"""

"""
    BasePage类是页面中的基类,用于提供常用的函数,为页面对象类提供服务.
"""


class BasePage:
    # driver对象
    # driver = webdriver.Chrome()
    # 使用构造函数传入页面对象driver,来调用以下的方法
    def __init__(self, driver):
        self.driver = driver

    # 访问url
    # 调用此方法的页面类每次都要写,所以直接写死
    # def visit(self, url):
    #     self.driver.get(url)
    def visit(self):
        self.driver.get(self.url)  # 这个self指调用它的类,而不是当前类对象

    # 定位元素
    def locator(self, loc):
        return self.driver.find_element(*loc)

    # 输入
    def input(self, loc, txt):
        self.locator(loc).send_keys(txt)

    # 点击
    def click(self, loc):
        self.locator(loc).click()

    # 放大浏览器
    def max_page(self):
        self.driver.maximize_window()

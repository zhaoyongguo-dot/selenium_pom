# -*- coding:utf-8 -*-
"""
@author: zyg
@file: case_unittest.py
@time: 2021/7/22 上午 12:50
@desc: tab / shift+tab  选中点击引号就会自动加引号
"""
import unittest
from time import sleep

from ddt import ddt, file_data, data
from selenium import webdriver

from page_object.page_index import IndexPage
from page_object.page_login import LoginPage

"""
    登录+搜索,分别执行用例,有时候搜索需要登陆怎么办呐,只用一个浏览器对象去调用即可
"""


@ddt
class TestCase(unittest.TestCase):

    # class 之前要做的事
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome()
        cls.lp = LoginPage(cls.driver)
        cls.ip = IndexPage(cls.driver)

    # class 之后要做的事
    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()

    # ddt + file_data 读取yaml文件
    @file_data('../data/user.yaml')
    def test_1_login(self, username, password):
        self.lp.login(username, password)
        assert 1 == 1, '登录成功'
        sleep(2)

    # data 简单数据驱动
    @data('车金丽')
    def test_2_search(self, txt):
        self.ip.search(txt)
        assert 1 == 1, '搜索成功'
        sleep(2)


if __name__ == '__main__':
    unittest.main('-vs')

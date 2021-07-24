# -*- coding:utf-8 -*-
"""
@author: zyg
@file: test_pytest.py
@time: 2021/7/23 上午 8:05
@desc: 
"""
import pytest
from selenium import webdriver

from page_object.page_index import IndexPage
from page_object.page_login import LoginPage
from util.yaml_tool import read_yaml

"""
    测试类
"""


class TestCase(object):

    @classmethod
    def setup_class(cls) -> None:
        cls.driver = webdriver.Chrome()
        cls.lp = LoginPage(cls.driver)
        cls.ip = IndexPage(cls.driver)

    @classmethod
    def teardown_class(cls) -> None:
        cls.driver.quit()

    # 登陆测试
    # 这里的路径为啥是./ 而不是../
    @pytest.mark.smoke
    @pytest.mark.parametrize('data', read_yaml('./data/user.yaml'))
    def test_1_login(self, data):
        username = data['username']
        password = data['password']
        self.lp.login(username, password)
        assert username == 'zyg', '登陆成功'

    # 搜索测试
    @pytest.mark.smoke
    @pytest.mark.parametrize('data', read_yaml('./data/search.yaml'))
    def test_2_index(self, data):
        txt = data['txt']
        self.ip.search(txt)
        assert txt == '手机', '搜索成功'

    @pytest.mark.smoke
    def test_3_(self):
        print('用例3执行成功')
        assert 1==1, '1==1'

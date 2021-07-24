# -*- coding:utf-8 -*-
"""
@author: zyg
@file: page_index.py
@time: 2021/7/22 上午 1:02
@desc: 
"""
from selenium.webdriver.common.by import By

from base.base_page import BasePage

"""
    IndexPage类,用于实现首页页面对象的文件
    主体内容包含:
        1,核心页面元素
            搜索框,搜索按钮
        2,核心业务流
            用户的搜索行为  
"""


class IndexPage(BasePage):
    # 核心元素
    url = 'http://47.107.116.139/phpwind/'
    search_input = (By.ID, 's')
    search_button = (By.XPATH, '//*[@id="J_header"]/div[2]/form/button')

    def search(self, search_txt):
        self.visit()
        self.input(self.search_input, search_txt)
        self.click(self.search_button)


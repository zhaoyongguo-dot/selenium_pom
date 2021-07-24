# -*- coding:utf-8 -*-
"""
@author: zyg
@file: yaml_tool.py
@time: 2021/7/23 上午 8:07
@desc: 
"""
import yaml


# 读yaml文件
def read_yaml(file):
    with open(file, mode='r', encoding='utf-8', closefd=True) as f:
        data = yaml.load(f, Loader=yaml.FullLoader)
        return data


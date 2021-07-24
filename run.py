# -*- coding:utf-8 -*-
"""
@author: zyg
@file: run.py
@time: 2021/7/23 上午 8:04
@desc: 
"""
import datetime
import os
from time import sleep

import pytest


"""
    run.py: error: unrecognized arguments: --alluredir=./report/allure_raw
    settings---python interpreter---不要使用虚拟环境,使用系统环境运行
"""

if __name__ == '__main__':
    now = datetime.datetime.now()
    t =now.strftime('%Y%m%d%H%M%S')
    pytest.main()
    sleep(3)
    os.system(f'allure generate ./report/allure_row -o ./report/report_{t} --clean')
    os.system('allure serve ./report/allure_row')  # 打开测试报告

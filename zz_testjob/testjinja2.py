# -*- coding: UTF-8 -*-
# !/usr/bin/python3
# @version: V
# @author: 飞翔的卡夫卡
# @contact: 592901924@qq.com
# @site: 
# @software: PyCharm
# @file: testjinja2.py
# @time: 2018/5/25 10:46
# @python：python3.6

import os
from jinja2 import Environment, PackageLoader

MONDAY_PATH = os.getenv("MONDAY_PATH")
summ_info = ['sum_h1','123','456','789','0123']
os.chdir(os.path.join(MONDAY_PATH,'html'))
env = Environment(loader=PackageLoader('html', 'templates')) # html 为包名 templates为包中读取report.html的路径名
template = env.get_template('report.html')
html_content = template.render(summary = summ_info)
print(html_content)

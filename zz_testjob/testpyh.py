# -*- coding: UTF-8 -*-
# !/usr/bin/python3
# @version: V
# @author: 飞翔的卡夫卡
# @contact: 592901924@qq.com
# @site: 
# @software: PyCharm
# @file: testpyh.py
# @time: 2018/5/17 12:36
# @python：python3.6

from pyh import *
######################################
# 放弃这个
page = PyH('My wonderful PyH page')
page << h2('Most compact way to build a 4 by 4 table')
page << table() << tr(td('1') + td('2')) + tr(td('3') + td('4'))
page << h2('Another way to build a 4 by 4 table')
mytab = page << table()
tr1 = mytab << tr()
tr1 << td('1') + td('2')
tr2 = mytab << tr()
tr2 << td('3') + td('4')
page.printOut()
print('voer~')
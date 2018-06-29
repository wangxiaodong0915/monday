# -*- coding: UTF-8 -*-
# !/usr/bin/python3
# @version: V
# @author: 飞翔的卡夫卡
# @contact: 592901924@qq.com
# @site: 
# @software: PyCharm
# @file: init_oracle_monday.py
# @time: 2018/6/29 17:11
# @python：python3.6

import os

import cx_Oracle

conn = cx_Oracle.connect('monday/monday@localhost/monday')
cur = conn.cursor()
# MONDAY_HOME = os.getenv("MONDAY_HOME")
# os.chdir(MONDAY_HOME)



cur.close()
conn.close()
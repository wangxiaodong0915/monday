# -*- coding: UTF-8 -*-
# !/usr/bin/python3
# @version: V
# @author: 飞翔的卡夫卡
# @contact: 592901924@qq.com
# @site: 
# @software: PyCharm
# @file: helpcode.py
# @time: 2018/5/17 11:03
# @python：python3.6

import sys
import os

#get global variables from __main__ module
if hasattr(sys.modules['__main__'], '__file__'):
    FILE_NAME = os.path.basename(sys.modules['__main__'].__file__).split('.')[0]
else:
    FILE_NAME = 'terminal'
#else:
    #print("Error:please run the script as file.")
    #exit(1)
if hasattr(sys.modules['__main__'], 'APP_NAME'):
    APP_NAME = sys.modules['__main__'].APP_NAME
else:
    APP_NAME = 'other'
if hasattr(sys.modules['__main__'], 'WORK_DATE'):
    WORK_DATE = sys.modules['__main__'].WORK_DATE
else:
    if APP_NAME in ('admin', 'gen', 'meta', 'daemon', 'other'):
        WORK_DATE = ''
    else:
        print("Error:you must define a WORK_DATE before import rds module")
        exit(1)

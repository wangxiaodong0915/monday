#!/usr/bin/python3

__author__ = 'wangxiaodong'
__filename__ = 'helloword'

# project name:monday
#   file name:helloword
#   auther:wangxiaodong
#   create date:2018/5/22 0:10
#   change auther:
#   change date:
#   version:
#   using enviroment:Django 1.13.0
#   python version:python 3.5.2
#   usage:

print("hello world!!!")

import config
print(config.config["log"]["level"])

print("123456789")
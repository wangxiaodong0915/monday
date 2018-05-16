# -*- coding: UTF-8 -*-
# !/usr/bin/python3
# @version: V
# @author: 飞翔的卡夫卡
# @contact: 592901924@qq.com
# @site: 
# @software: PyCharm
# @file: logtest.py
# @time: 2018/5/16 16:27
# @python：python3.6

#导入封装的日志记录模块
from mondayLog import MondayLogger
log = MondayLogger()

# from mondayLog import log
#输出日志
log.info("日志模块消息!");
log.debug("日志模块调试消息!");
log.error("日志模块错误消息!");

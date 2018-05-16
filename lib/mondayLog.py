# -*- coding: UTF-8 -*-
# !/usr/bin/python3
# @version: V1.0
# @author: 飞翔的卡夫卡
# @contact: 592901924@qq.com
# @site: 
# @software: PyCharm
# @file: mondayLog.py
# @time: 2018/5/16 16:16
# @python：python3.6

import os
import sys

import config
from datetime import date

MONDAY_LOG = config.config['log']['path']
LOG_LEVEL = config.config['log']['level']
################################## get from CSDN @风中斗士 #####################################################
import logging.handlers

class MondayLogger(logging.Logger):
    def __init__(self, filename=None):
        super(MondayLogger, self).__init__(self)
        # 日志文件名
        if filename is None:
            filename = 'pt_%s.log' % str(date.today())
        self.filename = os.path.join(MONDAY_LOG,filename)

        # 创建一个handler，用于写入日志文件 (每天生成1个，保留30天的日志)
        fh = logging.handlers.TimedRotatingFileHandler(self.filename, 'D', 1, 30)
        fh.suffix = "%Y%m%d-%H%M.log"
        fh.setLevel(LOG_LEVEL) # 可以从config中设置

        # 再创建一个handler，用于输出到控制台
        ch = logging.StreamHandler()
        ch.setLevel(LOG_LEVEL) # 可以从config中设置

        # 定义handler的输出格式
        formatter = logging.Formatter('[%(asctime)s] - %(filename)s [Line:%(lineno)d] - [%(levelname)s]-[thread:%(thread)s]-[process:%(process)s] - %(message)s')
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)

        # 给logger添加handler
        self.addHandler(ch)
        self.addHandler(fh)
################################## get from CSDN @风中斗士 #####################################################


# # ,把log能够读取到主程序名，加上YYYYMMDD的日期进行写日志处理
# if __name__!="main":
#     jobname = __name__ #如何获取名称
#     filename = jobname + "%s.log" % str(date.today())
#     log = MondayLogger(filename);



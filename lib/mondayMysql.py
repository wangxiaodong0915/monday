# -*- coding: UTF-8 -*-
# !/usr/bin/python3
# @version: V1.0
# @author: 飞翔的卡夫卡
# @contact: 592901924@qq.com
# @site: 
# @software: PyCharm
# @file: mondayMysql.py
# @time: 2018/5/16 17:41
# @python：python3.6

#导入封装的日志记录模块
from mondayLog import MondayLogger
log = MondayLogger('mondayMysql')

import pymysql

import config
from mondayTimer import func_timer

class mondayMysql():

    def __init__(self, host, user, password, database, db=None, charset='utf8'):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        if db is None:
            self.db = 'scrapy' # 确认None是否可行
        else:
            self.db = db
        self.charset = charset

    def connect(self):
        try:
            log.info("Mysql connect ……")
            self.db = pymysql.connect(self.host, self.user, self.password, self.database, charset='utf8')  # charset='utf-8' 不然python3输出的是乱码
            self.cursor = self.db.cursor()
            log.info("Mysql connect to %s:%s by %s" % (self.host, self.database ,self.user))
        except Exception as e:
            log.error(e)

    def execute(self,sql):
        self.results = self.execute_silent(sql)
        return self.results
    @func_timer
    def execute_silent(self, sql):
        try:
            # 执行SQL语句
            log.info("sql will be execute: %s" % sql)
            self.cursor.execute(sql)
            # 获取所有记录列表
            self.results = self.cursor.fetchall()
        except Exception as e:
            log.error(e)
        return self.results

    @func_timer
    def delete(self):
        pass

    @func_timer
    def create_table(self):
        pass

    @func_timer
    def drop_table(self):
        pass

    def useDatabase(self):
        pass

    def __exit__(self):
        self.cursor.close()
        self.db.close()
        log.info('Mysql connect closed!')

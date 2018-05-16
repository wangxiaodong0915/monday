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
            db = pymysql.connect(self.host, self.user, self.password, self.database, charset='utf8')  # charset='utf-8' 不然python3输出的是乱码

    @func_timer
    def execute(self):
        pass

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

#################################################################################
log.info('search JOB msg from mysql ---- START ----')
# 读取爬虫爬到的数据
# 获取mysql信息
# host = config.mysql['mysql_scrapy']['host']
# user = config.mysql['mysql_scrapy']['user']
# password = config.mysql['mysql_scrapy']['password']
# database = config.mysql['mysql_scrapy']['database']
# # 打开数据库连接
# db = pymysql.connect(host, user,password, database, charset='utf8') # charset='utf-8' 不然python3输出的是乱码
#
# # 使用 cursor() 方法创建一个游标对象 cursor
# cursor = db.cursor()
#
# # 获取数据的查询语句
# sql = """select
#  Positionname,
#  Companyname,
#  Workplace,
#  Salary,
#  Posttime,
#  Experience
#  from scrapy.qcwy"""
#
# try:
#     # 执行SQL语句
#     cursor.execute(sql)
#     # 获取所有记录列表
#     results = cursor.fetchall()
#     log.info('search JOB msg from mysql ---- END ----')
# except Exception as e:
#     log.error("unable to fetch data")
#     log.error(e)
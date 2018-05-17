# -*- coding: UTF-8 -*-
# !/usr/bin/python3
# @version: V
# @author: 飞翔的卡夫卡
# @contact: 592901924@qq.com
# @site: 
# @software: PyCharm
# @file: initMysql.py
# @time: 2018/5/17 15:40
# @python：python3.6

import config
import mondayMysql
#导入封装的日志记录模块
from mondayLog import MondayLogger
log = MondayLogger('mysqltest')

# 接受ddl文件清单，已逗号分隔
ddl_list = input("输入要初始化的ddl文件，如果多个文件以','分隔").split(',')

# Mysql login infomation
host = config.mysql['mysql_scrapy']['host']
user = config.mysql['mysql_scrapy']['user']
password = config.mysql['mysql_scrapy']['password']
database = config.mysql['mysql_scrapy']['database']
log.info("Mysql connect to %s:%s by %s" % (host, database, user) )

# Mysql connect and execute  a query sql
conn = mondayMysql.mondayMysql(host, user, password, database)
conn.connect()
log.info('login successful!')

#execute sql
for ddlfile in ddl_list:
    log.info('execute file %s' % ddlfile)
    conn.execute_ddlfile(ddlfile)



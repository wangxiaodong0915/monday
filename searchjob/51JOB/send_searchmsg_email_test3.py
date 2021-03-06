# -*- coding: UTF-8 -*-
# !/usr/bin/python3
# @version: V
# @author: 飞翔的卡夫卡
# @contact: 592901924@qq.com
# @site: 
# @software: PyCharm
# @file: send_searchmsg_email_test2.py
# @time: 2018/5/16 17:18
# @python：python3.6

#导入封装的日志记录模块
from mondayLog import MondayLogger
log = MondayLogger('send_searchmsg_email_test3')

import mondayMysql
import config

# 获取mysql信息
host = config.mysql['mysql_scrapy']['host']
user = config.mysql['mysql_scrapy']['user']
password = config.mysql['mysql_scrapy']['password']
database = config.mysql['mysql_scrapy']['database']
conn = mondayMysql.mondayMysql(host, user, password, database)
conn.connect()
log.info('login successful!')

# 获取数据的查询语句
sql = """select 
 Positionname,
 Companyname,
 Workplace,
 Salary,
 Posttime,
 Experience
 from scrapy.qcwy"""

# 执行SQL语句并获取结果
results = conn.execute(sql)
log.info('search JOB msg from mysql ---- END ----')


import sendemail

#拼装msg_str
log.info('Assembling msg_str ---- START ----')
msg_str = """"""
msg_str += """***Positionname***\t***Companyname***\t***Workplace***\t***Salary***\t***Posttime***\t***Experience***\n"""
count = 0
for row in results:
    msg_str += """%20s\t%20s\t%10s\t%20s\t%10s\t%10s\n""" % (row[0], row[1], row[2], row[3], row[4], row[5]) # (Positionname, Companyname, Workplace, Salary, Posttime, Experience)
    count += 1
msg_conut = """总计岗位：%d\n""" % count
log.info('Assembling msg_str ---- SUCCESS ----')
# 创建sendEmail类
se = sendemail.sendEmail(
    msg_conut + msg_str,
    config.mail['qq_email_wxd']['email'],
    config.mail['qq_email_wxd']['password'],
    config.sendlist['51job_list']['userlist'].split(','))
# 格式化发送的表头
se.set_msg("王晓东", "[sendEmail]sendEmail V1.0 Test 1st")
# 进行发送
# se.login()
se.send()
# 发送完成退出
se.close()

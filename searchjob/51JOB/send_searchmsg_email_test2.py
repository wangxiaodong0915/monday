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
log = MondayLogger('send_searchmsg_email_test2')

import pymysql
import config
#################################################################################
log.info('search JOB msg from mysql ---- START ----')
# 读取爬虫爬到的数据
# 获取mysql信息
host = config.mysql['mysql_scrapy']['host']
user = config.mysql['mysql_scrapy']['user']
password = config.mysql['mysql_scrapy']['password']
database = config.mysql['mysql_scrapy']['database']
# 打开数据库连接
db = pymysql.connect(host, user,password, database, charset='utf8') # charset='utf-8' 不然python3输出的是乱码

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

# 获取数据的查询语句
sql = """select 
 Positionname,
 Companyname,
 Workplace,
 Salary,
 Posttime,
 Experience
 from scrapy.qcwy"""

try:
    # 执行SQL语句
    cursor.execute(sql)
    # 获取所有记录列表
    results = cursor.fetchall()
    log.info('search JOB msg from mysql ---- END ----')
except Exception as e:
    log.error("unable to fetch data")
    log.error(e)

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
se.send()
# 发送完成退出
se.close()

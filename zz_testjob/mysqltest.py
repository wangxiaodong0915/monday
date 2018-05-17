# -*- coding: UTF-8 -*-
# !/usr/bin/python3
# @version: V
# @author: 飞翔的卡夫卡
# @contact: 592901924@qq.com
# @site: 
# @software: PyCharm
# @file: mysqltest.py
# @time: 2018/5/17 9:56
# @python：python3.6

import config
import mondayMysql
#导入封装的日志记录模块
from mondayLog import MondayLogger
log = MondayLogger('mysqltest')

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

#select sql
sql = """
SELECT 
positionname
FROM scrapy.qcwy
"""

#execute sql
results  = conn.execute(sql)

# print(results)
for row in results:
    print(row[0])


class Date():
    """Date transform functions"""

    def __init__(self):
        self.log = logging.getLogger('rds.Date')

    def set_log_level(self, level):
        self.log.setLevel(level)

    def is_valid(self, date_str):
        '''Is the YYYYMMDD string a valid date'''
        try:
            datetime.strptime(date_str, '%Y%m%d')
            return True
        except:
            self.log.error('%s is not a valid date' % date_str)
            return False

    def check_date(self, date_str):
        if not self.is_valid(date_str):
            raise ValueError("%s is not a vilid date string" % date_str)

    def db_date(self, date_str):
        self.check_date(date_str)
        db_date_str = "TO_DATE('%s','YYYYMMDD')" % date_str
        return db_date_str

    def weekday(self, date_str):
        '''返回星期几 MON-SUN is 1-7'''
        if self.is_valid(date_str):
            dt = datetime.strptime(date_str, '%Y%m%d').date()
            return dt.isoweekday()

    def to_date(self, date_str):
        '''convert YYYYMMDD to date type'''
        return datetime.strptime(date_str, '%Y%m%d').date()

    def to_str(self, pydate):
        '''convert date type to YYYYMMDD'''
        return pydate.strftime('%Y%m%d')

    def day_add(self, date_str, days):
        '''add days to a date string'''
        return self.to_str(self.to_date(date_str) + relativedelta(days=days))

    def tomorrow(self, date_str):
        '''tomorrow date string'''
        return self.day_add(date_str, 1)

    def month_add(self, date_str, months):
        '''输入：日期 ，月数（可为正、负）
        eg:
            month_add('20130212', -2)'''
        return self.to_str(self.to_date(date_str) + relativedelta(months=months))

    def month_begin(self, date_str):
        '''返回日期字符串，格式'YYYYMMDD'的月初'''
        if self.is_valid(date_str):
            datetime_str = datetime.strptime(date_str, '%Y%m%d').date()
            month_first = date(datetime_str.year, datetime_str.month, 1)
            return month_first.strftime('%Y%m%d')

    def month_end(self, date_str):
        '''返回日期字符串，格式'YYYYMMDD'的月末'''
        if self.is_valid(date_str):
            datetime_str = datetime.strptime(date_str, '%Y%m%d').date()
            month_end_day = calendar.monthrange(datetime_str.year, datetime_str.month)[1]
            month_end = date(datetime_str.year, datetime_str.month, month_end_day)
            return month_end.strftime('%Y%m%d')

    def last_month(self, date_str):
        '''返回日期字符串，格式'YYYYMMDD'的上月'''
        if self.is_valid(date_str):
            return self.month_add(date_str, -1)

    def last_month_end(self, date_str):
        '''返回日期字符串，格式'YYYYMMDD'的上一月末'''
        if self.is_valid(date_str):
            return self.month_end(self.last_month(date_str))

    def three_month_ago(self, date_str):
        '''返回日期字符串，格式'YYYYMMDD'的三月前'''
        if self.is_valid(date_str):
            return self.month_add(date_str, -3)

    def six_month_ago(self, date_str):
        '''返回日期字符串，格式'YYYYMMDD'的六月前'''
        if self.is_valid(date_str):
            return self.month_add(date_str, -6)

    def last_year(self, date_str):
        '''返回日期字符串，格式'YYYYMMDD'的上一年'''
        if self.is_valid(date_str):
            return self.month_add(date_str, -12)

    def two_year_ago(self, date_str):
        '''返回日期字符串，格式'YYYYMMDD'的两年前'''
        if self.is_valid(date_str):
            return self.month_add(date_str, -24)
# -*- coding: UTF-8 -*-
# !/usr/bin/python3
# @version: V
# @author: 飞翔的卡夫卡
# @contact: 592901924@qq.com
# @site: 
# @software: PyCharm
# @file: mondayDate.py
# @time: 2018/5/24 14:29
# @python：python3.6

import time
from datetime import datetime,date

class datetime():

    def __init__(self):
        pass

    def isVaildDate(self, datestr):
        """date format:%Y-%m-%d / %Y-%m-%d %H:%M:%S"""
        try:
            if ":" in datestr:
                time.strptime(datestr, "%Y-%m-%d %H:%M:%S")
            else:
                time.strptime(datestr, "%Y-%m-%d")
            return True
        except:
            return False

    def toDate(self, datestr):
        """date format:%Y-%m-%d / %Y-%m-%d %H:%M:%S return datetime.date(yyyy,mm,dd) """
        if self.isVaildDate(datestr):
            try:
                year, month, day = datestr.split('-')
                date_date = date(int(year), int(month), int(day) )
                return date_date
            except Exception as e:
                return False
        else:
            return False

    def ismonday(self, datestr):
        """判断是否为星期一"""
        if date.weekday(self.toDate(datestr)) == 0:
            return True
        else:
            return False

    def istuesday(self, datestr):
        """判断是否为星期2"""
        if date.weekday(self.toDate(datestr)) == 1:
            return True
        else:
            return False

    def iswednesday(self, datestr):
        """判断是否为星期3"""
        if date.weekday(self.toDate(datestr)) == 2:
            return True
        else:
            return False

    def isthursday(self, datestr):
        """判断是否为星期4"""
        if date.weekday(self.toDate(datestr)) == 3:
            return True
        else:
            return False

    def isfriday(self, datestr):
        """判断是否为星期5"""
        if date.weekday(self.toDate(datestr)) == 4:
            return True
        else:
            return False

    def issaturday(self, datestr):
        """判断是否为星期6"""
        if date.weekday(self.toDate(datestr)) == 5:
            return True
        else:
            return False

    def issunday(self, datestr):
        """判断是否为星期7"""
        if date.weekday(self.toDate(datestr)) == 6:
            return True
        else:
            return False

    def isworkday(self, datestr):
        """判断是否为工作日"""
        if date.weekday(self.toDate(datestr)) in (0,1,2,3,4):
            return True
        else:
            return False

    def isweekend(self, datestr):
        """判断是否为周末"""
        if date.weekday(self.toDate(datestr)) in (5,6):
            return True
        else:
            return False
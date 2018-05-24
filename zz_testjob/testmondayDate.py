# -*- coding: UTF-8 -*-
# !/usr/bin/python3
# @version: V
# @author: 飞翔的卡夫卡
# @contact: 592901924@qq.com
# @site: 
# @software: PyCharm
# @file: testmondayDate.py
# @time: 2018/5/24 15:31
# @python：python3.6

import mondayDate as md
import datetime

import unittest


class mytest(unittest.TestCase):
    ##初始化工作
    def setUp(self):
        self.tclass = md.datetime()  ##实例化了被测试模块中的类

    # 退出清理工作
    def tearDown(self):
        pass

        # 具体的测试用例，一定要以test开头

    def testisValid(self):
        self.assertEqual(self.tclass.isVaildDate('2018-1-12'), True)
        self.assertEqual(self.tclass.isVaildDate('2018-1-25'), True)
        self.assertEqual(self.tclass.isVaildDate('2018-1-32'), False)
        self.assertEqual(self.tclass.isVaildDate('2018-02-12'), True)
        self.assertEqual(self.tclass.isVaildDate('2018-02-29'), False)

    def testtoDate(self):
        self.assertEqual(self.tclass.toDate('2018-1-12'), datetime.date(2018,1,12))
        self.assertEqual(self.tclass.toDate('2018-01-12'), datetime.date(2018, 1, 12))
        self.assertEqual(self.tclass.toDate('2018-2-29'), False)

    def testismonday(self):
        self.assertEqual(self.tclass.ismonday('2018-05-21'), True)
        self.assertEqual(self.tclass.ismonday('2018-05-22'), False)
        self.assertEqual(self.tclass.ismonday('2018-05-23'), False)
        self.assertEqual(self.tclass.ismonday('2018-05-24'), False)
        self.assertEqual(self.tclass.ismonday('2018-05-25'), False)
        self.assertEqual(self.tclass.ismonday('2018-05-26'), False)
        self.assertEqual(self.tclass.ismonday('2018-05-27'), False)
        self.assertEqual(self.tclass.ismonday('2018-05-28'), True)
    def testistuesday(self):
        self.assertEqual(self.tclass.istuesday('2018-05-21'), False)
        self.assertEqual(self.tclass.istuesday('2018-05-22'), True)
        self.assertEqual(self.tclass.istuesday('2018-05-23'), False)
        self.assertEqual(self.tclass.istuesday('2018-05-24'), False)
        self.assertEqual(self.tclass.istuesday('2018-05-25'), False)
        self.assertEqual(self.tclass.istuesday('2018-05-26'), False)
        self.assertEqual(self.tclass.istuesday('2018-05-27'), False)
        self.assertEqual(self.tclass.istuesday('2018-05-28'), False)
    #iswednesday
    def testiswednesday(self):
        self.assertEqual(self.tclass.iswednesday('2018-05-21'), False)
        self.assertEqual(self.tclass.iswednesday('2018-05-22'), False)
        self.assertEqual(self.tclass.iswednesday('2018-05-23'), True)
        self.assertEqual(self.tclass.iswednesday('2018-05-24'), False)
        self.assertEqual(self.tclass.iswednesday('2018-05-25'), False)
        self.assertEqual(self.tclass.iswednesday('2018-05-26'), False)
        self.assertEqual(self.tclass.iswednesday('2018-05-27'), False)
        self.assertEqual(self.tclass.iswednesday('2018-05-28'), False)
    #isthursday
    def testisthursday(self):
        self.assertEqual(self.tclass.isthursday('2018-05-21'), False)
        self.assertEqual(self.tclass.isthursday('2018-05-22'), False)
        self.assertEqual(self.tclass.isthursday('2018-05-23'), False)
        self.assertEqual(self.tclass.isthursday('2018-05-24'), True)
        self.assertEqual(self.tclass.isthursday('2018-05-25'), False)
        self.assertEqual(self.tclass.isthursday('2018-05-26'), False)
        self.assertEqual(self.tclass.isthursday('2018-05-27'), False)
        self.assertEqual(self.tclass.isthursday('2018-05-28'), False)
    #isfriday
    def testisfriday(self):
        self.assertEqual(self.tclass.isfriday('2018-05-21'), False)
        self.assertEqual(self.tclass.isfriday('2018-05-22'), False)
        self.assertEqual(self.tclass.isfriday('2018-05-23'), False)
        self.assertEqual(self.tclass.isfriday('2018-05-24'), False)
        self.assertEqual(self.tclass.isfriday('2018-05-25'), True)
        self.assertEqual(self.tclass.isfriday('2018-05-26'), False)
        self.assertEqual(self.tclass.isfriday('2018-05-27'), False)
        self.assertEqual(self.tclass.isfriday('2018-05-28'), False)
    #issaturday
    def testissaturday(self):
        self.assertEqual(self.tclass.issaturday('2018-05-21'), False)
        self.assertEqual(self.tclass.issaturday('2018-05-22'), False)
        self.assertEqual(self.tclass.issaturday('2018-05-23'), False)
        self.assertEqual(self.tclass.issaturday('2018-05-24'), False)
        self.assertEqual(self.tclass.issaturday('2018-05-25'), False)
        self.assertEqual(self.tclass.issaturday('2018-05-26'), True)
        self.assertEqual(self.tclass.issaturday('2018-05-27'), False)
        self.assertEqual(self.tclass.issaturday('2018-05-28'), False)
    #issunday
    def testissunday(self):
        self.assertEqual(self.tclass.issunday('2018-05-21'), False)
        self.assertEqual(self.tclass.issunday('2018-05-22'), False)
        self.assertEqual(self.tclass.issunday('2018-05-23'), False)
        self.assertEqual(self.tclass.issunday('2018-05-24'), False)
        self.assertEqual(self.tclass.issunday('2018-05-25'), False)
        self.assertEqual(self.tclass.issunday('2018-05-26'), False)
        self.assertEqual(self.tclass.issunday('2018-05-27'), True)
        self.assertEqual(self.tclass.issunday('2018-05-28'), False)
    #isworkday
    def testisworkday(self):
        self.assertEqual(self.tclass.isworkday('2018-05-21'), True)
        self.assertEqual(self.tclass.isworkday('2018-05-22'), True)
        self.assertEqual(self.tclass.isworkday('2018-05-23'), True)
        self.assertEqual(self.tclass.isworkday('2018-05-24'), True)
        self.assertEqual(self.tclass.isworkday('2018-05-25'), True)
        self.assertEqual(self.tclass.isworkday('2018-05-26'), False)
        self.assertEqual(self.tclass.isworkday('2018-05-27'), False)
        self.assertEqual(self.tclass.isworkday('2018-05-28'), True)
    #isweekend
    def testisweekend(self):
        self.assertEqual(self.tclass.isweekend('2018-05-21'), False)
        self.assertEqual(self.tclass.isweekend('2018-05-22'), False)
        self.assertEqual(self.tclass.isweekend('2018-05-23'), False)
        self.assertEqual(self.tclass.isweekend('2018-05-24'), False)
        self.assertEqual(self.tclass.isweekend('2018-05-25'), False)
        self.assertEqual(self.tclass.isweekend('2018-05-26'), True)
        self.assertEqual(self.tclass.isweekend('2018-05-27'), True)
        self.assertEqual(self.tclass.isweekend('2018-05-28'), False)

if __name__ == '__main__':
    unittest.main()
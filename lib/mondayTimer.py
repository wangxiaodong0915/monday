# -*- coding: UTF-8 -*-
# !/usr/bin/python3
# @version: V
# @author: 飞翔的卡夫卡
# @contact: 592901924@qq.com
# @site: 
# @software: PyCharm
# @file: mondayTimer.py
# @time: 2018/5/16 17:57
# @python：python3.6

#导入封装的日志记录模块
from mondayLog import MondayLogger
log = MondayLogger('mondayTimer')

from functools import wraps
import time

########################################## 借用 AzureSky 的 $如何用Python装饰器实现一个代码计时器？###################################################
# https://www.cnblogs.com/jiayongji/p/7588133.html
def func_timer(function):
    '''
    用装饰器实现函数计时
    :param function: 需要计时的函数
    :return: None
    '''
    @wraps(function)
    def function_timer(*args, **kwargs):
        log.info('[Function: {name} start...]'.format(name = function.__name__))
        t0 = time.time()
        result = function(*args, **kwargs)
        t1 = time.time()
        log.info('[Function: {name} finished, spent time: {time:.2f}s]'.format(name = function.__name__,time = t1 - t0))
        return result
    return function_timer

########################################## 借用 AzureSky 的 $如何用Python装饰器实现一个代码计时器？###################################################
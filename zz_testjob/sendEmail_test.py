# -*- coding: UTF-8 -*-
# !/usr/bin/python3
# @version: V
# @author: 飞翔的卡夫卡
# @contact: 592901924@qq.com
# @site: 
# @software: PyCharm
# @file: sendEmail_test.py
# @time: 2018/5/16 15:59
# @python：python3.6

import sendemail

# 创建sendEmail类
se = sendemail.sendEmail(
    'hello World!',
    '592901924@qq.com'
)
# 格式化发送的表头
se.set_msg("见你就上", "[sendEmail]sendEmail V1.0 Test 1st")
se.send()
# 发送完成退出
se.close()

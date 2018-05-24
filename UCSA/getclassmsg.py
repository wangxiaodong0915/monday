# -*- coding: UTF-8 -*-
# !/usr/bin/python3
# @version: V
# @author: 飞翔的卡夫卡
# @contact: 592901924@qq.com
# @site: 
# @software: PyCharm
# @file: getclassmsg.py
# @time: 2018/5/24 11:54
# @python：python3.6

import re
import urllib.request

#导入封装的日志记录模块
from mondayLog import MondayLogger
log = MondayLogger('getclassmsg')

import sendemail
def getclassmsg():
    try:
        html1 = urllib.request.urlopen("http://aipt.ucas.ac.cn/index.php/zh-cn/jxgg/5933-3-3-4").read()
        html1 = html1.decode('utf-8')
        part_title = r"<title>(.+?)</title>"
        title = re.compile(part_title).findall(html1)
        # print(title)
        part_table = r"""<table style="width: 707px; height: 302px;">((.|\r\n)+)</table> """
        table = re.compile(part_table).findall(html1)
        html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>%s</title>
    <p><h2>%s</h2></p>
    <table>
""" % (title[0], title[0])
        for x in table:
            for i in x:
                html += i
        html += """
</table>

</body>
</html>
"""
        # 创建sendEmail类
        se = sendemail.sendEmail(
            html,
            "592901924@qq.com",
            "html"
        )
        # 格式化发送的表头
        se.set_msg("王晓东", "[%s]sendEmail about UCAS class" % title[0])
        # 进行发送
        se.send()
        # 发送完成退出
        se.close()
        return True
    except Exception as e:
        log.error(e)
        return False

from datetime import date,datetime
import time

if __name__ == "__main__":
    while 1:
        if date.weekday(date.today()) == 3:
            if datetime.now().hour == 14:
                result = getclassmsg()
                if result is True:
                    log.info("sleep 86400")
                    time.sleep(86400)
                else:
                    continue
            else:
                log.info("sleep 3600")
                time.sleep(3600)
        else:
            log.info("sleep 86400")
            time.sleep(86400)

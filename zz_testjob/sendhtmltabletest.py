# -*- coding: UTF-8 -*-
# !/usr/bin/python3
# @version: V
# @author: 飞翔的卡夫卡
# @contact: 592901924@qq.com
# @site: 
# @software: PyCharm
# @file: sendhtmltabletest.py
# @time: 2018/5/17 13:48
# @python：python3.6

import sendemail

# 创建html table
html = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>table test</title>
</head>
<body>
    <div>
<table border="1">
<tr>
    <td><a href="http://www.w3school.com.cn">This is a link</a></td>
<tr>
<td>row 1, cell 1</td>
<td>row 1, cell 2</td>
</tr>
<tr>
<td>row 2, cell 1</td>
<td>row 2, cell 2</td>
</tr>
</table>
    </div>
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
se.set_msg("王晓东", "[sendEmail]sendEmail about html table V1.1 Test 2nd")
# 进行发送
se.send()
# 发送完成退出
se.close()

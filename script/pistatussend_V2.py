#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# @version: V
# @author: 飞翔的卡夫卡
# @contact: 592901924@qq.com
# @site: 
# @software: PyCharm
# @file: pistatussend.py
# @time: 2018/5/21 10:03
# @python：python3.6

from datetime import date

from psutil import *
from mondayLog import MondayLogger
log = MondayLogger('pistatussend')


log.info("*******Start to GET Usage*******")
# print(virtual_memory()) # 单位是MB(兆B）
mem_total = virtual_memory().total/1024/1024
mem_use = virtual_memory().used/1024/1024
mem_percent = virtual_memory().percent # 百分比值 超过80% 需要报异常
mem_free = virtual_memory().free/1024/1024
log.info('Get virtual memory usage,successful!')


# print(swap_memory()) # 单位是Mb(兆b）
swap_total = swap_memory().total/1024/1024
swap_used = swap_memory().used/1024/1024
swap_percent = swap_memory().percent # 百分比值 超过80% 需要报异常
log.info('Get swap memory usage,successful!')

# print(disk_partitions())
# print(disk_partitions()[0].device) 获取磁盘清单，包括逻辑盘和物理盘
device_list = []
for index in range(0,len(disk_partitions(all=False))):
    # device_list.append(disk_partitions(all=False)[index].device) # win10 使用
    device_list.append(disk_partitions(all=False)[index].mountpoint) # PI UNIX 使用
log.info('Get disk list msg,successful!')

# print(disk_usage(disk_partitions()[0].device).total) # 获取每个磁盘路径或者逻辑盘的总空间、使用情况、使用比例
device_used = {}
disk_status = ""
disk_status_path = ""
for device in device_list:
    disk_part = disk_usage(device)
    status = ""
    if float(disk_part.percent) > 85:
        status = "red"
    elif float(disk_part.percent) > 50 and float(disk_part.percent) <= 85:
        status = "yellow"
    else:
        status = "green"
    if status == "red":
        disk_status = "red"
        disk_status_path = device + " percent:" + str(disk_part.percent) + "%"
    elif disk_status != "red" and status == "yellow":
        disk_status = "yellow"
        disk_status_path = device + " percent:" + str(disk_part.percent) + "%"
    elif disk_status == "":
        disk_status = "green"
        disk_status_path = "Normal"
    device_used[device] = [round(disk_part.total/1024/1024), round(disk_part.used/1024/1024), disk_part.percent, status]
log.info('Get dict of disk usage,successful!')
log.info("*******End to GET Usage*******")
log.info("******* Start to decide server status *******")
# memory percent >= 80%  红级别；80% >= memory percent > 60%  黄级别；else 绿级别
memory_status = ""
if float(mem_percent) >= 80:
    memory_status = "red"
elif float(mem_percent) < 80 and float(mem_percent) >= 60:
    memory_status = "yellow"
else:
    memory_status = "green"
log.info("momory status is %s" % memory_status)

swap_status = ""
if float(swap_percent) >= 80:
    swap_status = "red"
elif float(swap_percent) < 80 and float(swap_percent) >= 60:
    swap_status = "yellow"
else:
    swap_status = "green"
log.info("******* END to decide server status *******")

log.info('******* Start to assembly HTML *******')
# msg_str = """
# <!DOCTYPE html>
# <html lang="en">
# <head>
#     <meta charset="UTF-8">
#     <title>PI server usage today!</title>
# </head>
# <body>
#     <div>
# """
# log.info('拼装html，写入树莓派总体运行状况')
# msg_str += """
#         <table border="1" bgcolor="#66CCCC">
#             <tr>
#                 <th>树莓派使用情况</th>
#             </tr>
#             <tr bgcolor="#33CCFF">
#                 <td><h3>Memory status</h3></td>
#                 <td><h3>Swap status</h3></td>
#                 <td><h3>Disk status</h3></td>
#             </tr>
#             <tr>
#                 <td bgcolor="%s">%s</td>
#                 <td bgcolor="%s">%s</td>
#                 <td bgcolor="%s">%s</td>
#             </tr>
#         </table>
# """ % (memory_status, str(mem_percent) + "%", swap_status, str(swap_percent) + "%", disk_status, disk_status_path)
# log.info("拼装html，写入内存详情")
# msg_str += """
# <table border="1" bgcolor="#66CCCC">
#             <tr bgcolor="#33CCFF">
#                 <th>内存使用情况说明</th>
#             </tr>
#             <tr bgcolor="#33CCFF">
#                 <td><h3>总量</h3></td>
#                 <td><h3>已用量</h3></td>
#                 <td><h3>使用百分比</h3></td>
#             </tr>
#             <tr>
#                 <td>%s MB</td>
#                 <td>%s MB</td>
#                 <td bgcolor="%s">%s</td>
#             </tr>
#         </table>
# """ % (round(mem_total), round(mem_use), memory_status, str(mem_percent) + "%")
# log.info("拼装html，写入swap详情")
# msg_str += """
#         <table border="1" bgcolor="#66CCCC">
#             <tr bgcolor="#33CCFF">
#                 <th>SWAP使用情况说明</th>
#             </tr>
#             <tr bgcolor="#33CCFF">
#                 <td><h3>总量</h3></td>
#                 <td><h3>已用量</h3></td>
#                 <td><h3>使用百分比</h3></td>
#             </tr>
#             <tr>
#                 <td>%s MB</td>
#                 <td>%s MB</td>
#                 <td bgcolor="%s">%s</td>
#             </tr>
#         </table>
# """ % (round(swap_total), round(swap_used), swap_status, str(swap_percent) + "%")
# log.info("拼装html，写入磁盘使用情况详情")
# msg_str += """
#         <table border="1" bgcolor="#66CCCC">
#             <tr bgcolor="#33CCFF">
#                 <th>磁盘使用情况说明</th>
#             </tr>
#             <tr bgcolor="#33CCFF">
#                 <td><h3>磁盘路径</h3></td>
#                 <td><h3>总量</h3></td>
#                 <td><h3>已用量</h3></td>
#                 <td><h3>使用百分比</h3></td>
#             </tr>
# """
# for device in device_used:
#     msg_str += """
#             <tr>
#                 <td>%s</td>
#                 <td>%s MB</td>
#                 <td>%s MB</td>
#                 <td bgcolor="%s">%s</td>
#             </tr>
#     """  % (device, round(device_used[device][0]), round(device_used[device][1]), device_used[device][3], str(device_used[device][2]) + "%")
# msg_str += """
#         </table>
#     </div>
# </body>
# </html>
# """

# use jinja2 make html
import os
from jinja2 import Environment, PackageLoader

env = Environment(loader=PackageLoader('html', 'templates')) # html 为包名 templates为包中读取report.html的路径名
template = env.get_template('serverusage.html')
html_content = template.render(
    memory_status = memory_status,
    mem_percent = str(mem_percent),
    swap_status = swap_status,
    swap_percent = str(swap_percent),
    disk_status = disk_status,
    disk_status_path = disk_status_path,
    mem_total = round(mem_total),
    mem_use = round(mem_use),
    swap_total = round(swap_total),
    swap_used = round(swap_used),
    device_used = device_used
)

import sendemail
# 创建sendEmail类
se = sendemail.sendEmail(
    html_content,
    "592901924@qq.com",
    "html"
)
# 格式化发送的表头
label = ""
if memory_status == "red" or disk_status == "red" or swap_status == "red": # 包含19种情况
    label = "Red"
elif (memory_status != "red" and disk_status != "red" and swap_status != "red") and (memory_status == "yellow" or disk_status == "yellow" or swap_status == "yellow"): #
    label = "Yellow"
elif memory_status == "green" and disk_status == "green" and swap_status == "green":
    label = "Green"
se.set_msg("东助", "[%s-%s]PI server status is %s !" % (label, str(date.today()), label.upper()))
# 登录邮件
se.login()
# 进行发送
se.send()
# 发送完成退出
se.close()

log.info('PI server status successful!!!')
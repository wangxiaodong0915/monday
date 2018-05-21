# -*- coding: UTF-8 -*-
# !/usr/bin/python3
# @version: V
# @author: 飞翔的卡夫卡
# @contact: 592901924@qq.com
# @site: 
# @software: PyCharm
# @file: pistatussend.py
# @time: 2018/5/21 10:03
# @python：python3.6

# import psutil
# import datetime

'''  
#查看cpu的信息  
print u"CPU 个数 %s"%psutil.cpu_count()  
print u"物理CPU个数 %s"%psutil.cpu_count(logical=False)  
print u"CPU uptimes"  
print psutil.cpu_times()  
print ""  

#查看内存信息  
# print u"系统总内存 %s M"%(psutil.TOTAL_PHYMEM/1024/1024)  
# print u"系统可用内存 %s M"%(psutil.avail_phymem()/1024/1024)  
# mem_rate = int(psutil.avail_phymem())/float(psutil.TOTAL_PHYMEM)  
# print u"系统内存使用率 %s %%"%int(mem_rate*100)  

#系统启动时间  
print u"系统启动时间 %s"%datetime.datetime.fromtimestamp(psutil.boot_time()).strftime("%Y-%m-%d %H:%M:%S")  

#系统用户  
users_count = len(psutil.users())  
users_list = ",".join([ u.name for u in psutil.users()])  
print u"当前有%s个用户，分别是%s"%(users_count, users_list)  

#网卡，可以得到网卡属性，连接数，当前流量等信息  
net = psutil.net_io_counters()  
bytes_sent = '{0:.2f} kb'.format(net.bytes_recv / 1024)  
bytes_rcvd = '{0:.2f} kb'.format(net.bytes_sent / 1024)  
print u"网卡接收流量 %s 网卡发送流量 %s"%(bytes_rcvd, bytes_sent)  
'''

#进程  进程的各种详细参数
# # 查看系统全部进程
# print(u"系统全部进程 %s"%psutil.pids())
# for pnum in psutil.pids():
#     p = psutil.Process(pnum)
#     print(u"进程名 %-20s  内存利用率 %-18s 进程状态 %-10s 创建时间 %-10s "%(p.name(),p.memory_percent(),p.status(),p.create_time()))
#     # print p.io_counters()    #进程读写信息
# p.cwd()    #进程的工作目录绝对路径
# p.status()   #进程状态
# p.create_time()  #进程创建时间
# p.uids()    #进程uid信息

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
    device_used[device] = [disk_part.total/1024/1024, disk_part.used/1024/1024, disk_part.percent, status]
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
msg_str = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>PI server usage today!</title>
</head>
<body>
    <div>
"""
log.info('拼装html，写入树莓派总体运行状况')
msg_str += """
        <table border="1" bgcolor="#66CCCC">
            <tr>
                <th>树莓派使用情况</th>
            </tr>
            <tr bgcolor="#33CCFF">
                <td><h3>Memory status</h3></td>
                <td><h3>Swap status</h3></td>
                <td><h3>Disk status</h3></td>
            </tr>
            <tr>
                <td bgcolor="%s">%s</td>
                <td bgcolor="%s">%s</td>
                <td bgcolor="%s">%s</td>
            </tr>
        </table>
""" % (memory_status, str(mem_percent) + "%", swap_status, str(swap_percent) + "%", disk_status, disk_status_path)
log.info("拼装html，写入内存详情")
msg_str += """
<table border="1" bgcolor="#66CCCC">
            <tr bgcolor="#33CCFF">
                <th>内存使用情况说明</th>
            </tr>
            <tr bgcolor="#33CCFF">
                <td><h3>总量</h3></td>
                <td><h3>已用量</h3></td>
                <td><h3>使用百分比</h3></td>
            </tr>
            <tr>
                <td>%s MB</td>
                <td>%s MB</td>
                <td bgcolor="%s">%s</td>
            </tr>
        </table>
""" % (round(mem_total), round(mem_use), memory_status, str(mem_percent) + "%")
log.info("拼装html，写入swap详情")
msg_str += """
        <table border="1" bgcolor="#66CCCC">
            <tr bgcolor="#33CCFF">
                <th>SWAP使用情况说明</th>
            </tr>
            <tr bgcolor="#33CCFF">
                <td><h3>总量</h3></td>
                <td><h3>已用量</h3></td>
                <td><h3>使用百分比</h3></td>
            </tr>
            <tr>
                <td>%s MB</td>
                <td>%s MB</td>
                <td bgcolor="%s">%s</td>
            </tr>
        </table>
""" % (round(swap_total), round(swap_used), swap_status, str(swap_percent) + "%")
log.info("拼装html，写入磁盘使用情况详情")
msg_str += """
        <table border="1" bgcolor="#66CCCC">
            <tr bgcolor="#33CCFF">
                <th>磁盘使用情况说明</th>
            </tr>
            <tr bgcolor="#33CCFF">
                <td><h3>磁盘路径</h3></td>
                <td><h3>总量</h3></td>
                <td><h3>已用量</h3></td>
                <td><h3>使用百分比</h3></td>
            </tr>
"""
for device in device_used:
    msg_str += """
            <tr>
                <td>%s</td>
                <td>%s MB</td>
                <td>%s MB</td>
                <td bgcolor="%s">%s</td>
            </tr>
    """  % (device, round(device_used[device][0]), round(device_used[device][1]), device_used[device][3], str(device_used[device][2]) + "%")
msg_str += """
        </table>
    </div>
</body>
</html>
"""

import sendemail
# 创建sendEmail类
se = sendemail.sendEmail(
    msg_str,
    "592901924@qq.com",
    "html"
)
# 格式化发送的表头
label = ""
print(str(memory_status), str(disk_status), str(swap_status))
if memory_status == "red" or disk_status == "red" or swap_status == "red": # 包含19种情况
    label = "Red"
elif (memory_status != "red" and disk_status != "red" and swap_status != "red") and (memory_status == "yellow" or disk_status == "yellow" or swap_status == "yellow"): #
    label = "Yellow"
elif memory_status == "green" and disk_status == "green" and swap_status == "green":
    lable = "Green"
print(label)
se.set_msg("王晓东", "[%s-%s]PI server status is %s !" % (label, str(date.today()), label.upper()))
# 登录邮件
se.login()
# 进行发送
se.send()
# 发送完成退出
se.close()

log.info('PI server status successful!!!')
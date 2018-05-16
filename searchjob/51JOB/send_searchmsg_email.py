# -*- coding: UTF-8 -*-

# !/usr/bin/python3

import pymysql
import config
#################################################################################
# 读取爬虫爬到的数据

# 打开数据库连接
db = pymysql.connect("localhost", "root", "123456", "scrapy", charset='utf8') # charset='utf-8' 不然python3输出的是乱码

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

# 使用 execute()  方法执行 SQL 查询
# cursor.execute("select * from screpy")

# 使用 fetchone() 方法获取单条数据.
# data = cursor.fetchone()

# 获取数据的查询语句
sql = """select 
 Positionname,
 Companyname,
 Workplace,
 Salary,
 Posttime,
 Experience
 from qcwy"""

try:
    # 执行SQL语句
    cursor.execute(sql)
    # 获取所有记录列表
    results = cursor.fetchall()
    # for row in results:
    #     Positionname = row[0]
    #     Companyname = row[1]
    #     Workplace = row[2]
    #     Salary = row[3]
    #     Posttime = row[4]
    #     Experience = row[5]
    #     # 打印结果
    #     print("Positionname=%s\tCompanyname=%s\tWorkplace=%s\tSalary=%s\tPosttime=%s\tExperience=%s" % \
    #           (Positionname, Companyname, Workplace, Salary, Posttime, Experience))
except Exception as e:
    raise e
    print("Error: unable to fetch data")

# ###########################################################
# 发送普通html邮件，不带附件不带其他信息，不带签名。
from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr

import smtplib

def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))

# 输入Email地址和口令:
from_addr = config.mail['qq_email_wxd']['email']
password = config.mail['qq_email_wxd']['password']
# 输入收件人地址:
to_addr = '592901924@qq.com'
# 输入SMTP服务器地址:
smtp_server = config.mail['qq_email_wxd']['smtp']
smtp_port = config.mail['qq_email_wxd']['smtp_port']

#构造msg_str
msg_type = 'plain' # plain:文本 html：网页

msg_str = """"""
msg_str += """***Positionname***\t***Companyname***\t***Workplace***\t***Salary***\t***Posttime***\t***Experience***\n"""
count = 0
for row in results:
    msg_str += """%s\t%s\t%s\t%s\t%s\t%s\n""" % (row[0], row[1], row[2], row[3], row[4], row[5]) # (Positionname, Companyname, Workplace, Salary, Posttime, Experience)
    count += 1
msg_conut = """总计岗位：%d\n""" % count
msg = MIMEText( msg_conut + msg_str, msg_type, 'utf-8')
msg['From'] = _format_addr('王晓东 <%s>' % from_addr)
msg['To'] = _format_addr('王晓东 <%s>' % to_addr)
msg['Subject'] = Header('[from东助]51JOB 自动采集结果推送', 'utf-8').encode()

server = smtplib.SMTP_SSL(smtp_server, 465)
server.set_debuglevel(1)
print(from_addr)
server.login(from_addr, password)
print(from_addr)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()
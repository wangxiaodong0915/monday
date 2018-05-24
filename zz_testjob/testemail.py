# -*- coding: UTF-8 -*-
# !/usr/bin/python3
# @version: V
# @author: 飞翔的卡夫卡
# @contact: 592901924@qq.com
# @site: 
# @software: PyCharm
# @file: testemail.py
# @time: 2018/5/24 18:14
# @python：python3.6
import smtplib

import config
# ###########################################################
# 发送普通html邮件，不带附件不带其他信息，不带签名。
from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr

def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))
from_addr = "1355449754@qq.com"
password = "milxihzmqxtohbfh"
# 输入收件人地址:
to_addr = config.sendlist['51job_list']['userlist'].split(',')
# 输入SMTP服务器地址:
smtp_server = config.mail['qq_email_monday']['smtp']
smtp_port = config.mail['qq_email_monday']['smtp_port']

#构造msg_str
msg_type = 'plain' # plain:文本 html：网页

msg_str = """"""
msg_str += """***Positionname***\t***Companyname***\t***Workplace***\t***Salary***\t***Posttime***\t***Experience***\n"""

msg = MIMEText( msg_str, msg_type, 'utf-8')
msg['From'] = _format_addr('王晓东 <%s>' % from_addr)
msg['To'] = _format_addr('王晓东 <%s>' % to_addr)
msg['Subject'] = Header('[from东助]51JOB 自动采集结果推送', 'utf-8').encode()

server = smtplib.SMTP_SSL(smtp_server, 465)
server.set_debuglevel(1)
print(from_addr)
server.login(from_addr, password)
print(from_addr)
server.sendmail(from_addr, to_addr, msg.as_string())
server.quit()
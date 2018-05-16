# -*- coding: UTF-8 -*-
# !/usr/bin/python3
# @version: V1.0
# @author: 飞翔的卡夫卡
# @contact: 592901924@qq.com
# @site: 
# @software: PyCharm
# @file: sendemail.py.py
# @time: 2018/5/16 15:32
# @python：python3.6

from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
import smtplib

from mondayLog import MondayLogger
log = MondayLogger('sendemail')

class sendEmail():
    __doc__="""
待补充！！！ 20180516

eg:
import sendemail
# 创建sendEmail类
se = sendemail.sendEmail(
    'hello World!',
    'xxxxxxxx@qq.com',
    'password',
    ['xxxxxxxx@qq.com'])
# format Header
se.set_msg("wxd", "[sendEmail]sendEmail V1.0 Test 1st")
# send email
se.send()
# close email server process
se.close()
    """

    def __init__(self, msg_str, from_addr, password, to_addrs, smtp_server='smtp.qq.com', smtp_port=465, msg_type='plain'):
        self.msg_str = msg_str
        self.from_addr = from_addr
        self.password = password
        self.to_addrs = to_addrs
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.msg_type = msg_type  # plain:文本 html：网页
        
    def _format_addr(self, s):
        self.name, self.addr = parseaddr(s)
        return formataddr((Header(self.name, 'utf-8').encode(), self.addr))

    def login(self):
        try:
            log.info('connect email with smtp, from address: %s' % self.from_addr)
            server = smtplib.SMTP_SSL(self.smtp_server, 465)
            server.set_debuglevel(1)
            server.login(self.from_addr, self.password)
            log.info('%s login success!' % self.from_addr)
        except Exception as e:
            log.error(e)
        return server

    def send(self):
        self.server  = self.login()
        self.server.sendmail(self.from_addr, self.to_addrs, self.msg.as_string())
        log.info('send email from address %s to address %s …' % (self.from_addr, self.to_addrs[0]))
        return True

    def set_msg(self, from_name, subject, ):
        self.msg = MIMEText(self.msg_str, self.msg_type, 'utf-8')
        self.msg['From'] = self._format_addr('%s <%s>' % (from_name, self.from_addr))
        # self.msg['To'] = self._format_addr('王晓东 <%s>' % self.to_addrs)
        self.msg['Subject'] = Header(subject, 'utf-8').encode()

    def close(self):
        self.server.quit()
        log.info('email:%s quit successful!' % self.from_addr)

    def __exit__(self):
        self.close()

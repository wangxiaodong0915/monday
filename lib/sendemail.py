# -*- coding: UTF-8 -*-
# !/usr/bin/python3
# @version: V1.2
# @author: 飞翔的卡夫卡
# @contact: 592901924@qq.com
# @site: 
# @software: PyCharm
# @file: sendemail.py.py
# @time: 2018/5/16 15:32
# @python：python3.6

# V1.0 定义sendemail.py  为发送邮件的公用类
# V1.1 修改了登录机制,把server 修改为 self.server 内部对象
# V1.2 self.send() 中先执行self.login()，减少调用的麻烦。

from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
import smtplib
import config

from mondayLog import MondayLogger
log = MondayLogger('sendemail')

FROM_ADDR = config.mail['qq_email_monday']['email']
PASSWORD = config.mail['qq_email_monday']['password']
SMTP = config.mail['qq_email_monday']['smtp']
STMP_PORT = config.mail['qq_email_monday']['smtp_port']
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

    def __init__(self, msg_str, to_addrs, msg_type='plain',from_addr=FROM_ADDR, password=PASSWORD, smtp_server=SMTP, smtp_port=STMP_PORT):
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
            self.server = smtplib.SMTP_SSL(self.smtp_server, 465)
            self.server.set_debuglevel(1)
            self.server.login(self.from_addr, self.password)
            log.info('%s login success!' % self.from_addr)
        except Exception as e:
            log.error(e)

    def send(self):
        self.login()
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

#!/usr/bin/python env
from time import sleep

__author__ = 'wangxiaodong'
__filename__ = 'runscript'

# project name:monday
#   file name:runscript
#   auther:wangxiaodong
#   create date:2018/5/23 21:03
#   change auther:
#   change date:
#   version:
#   using enviroment:Django 1.13.0
#   python version:python 3.5.2
#   usage:

import os

from mondayLog import MondayLogger
log = MondayLogger('runscript')

MONDAY_PATH = os.getenv('MONDAY_PATH')
os.chdir(os.path.join(MONDAY_PATH,'script'))
while 1:
    log.info("python3 pistatussend_V2.py")
    os.system('python3 pistatussend_V2.py')
    log.info('sleep 12 hours.')
    sleep(12 * 3600)
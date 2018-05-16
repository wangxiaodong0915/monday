
import os
import os.path
import configparser
import logging

MONDAY_PATH = os.getenv('MONDAY_PATH')
# print(MONDAY_PATH)
# MONDAY_PATH/conf/config.ini
config_file = (os.path.join(MONDAY_PATH,'conf','config.ini'),
                os.path.join(MONDAY_PATH,'conf','config.custom.ini') )
config = configparser.ConfigParser()
config.read(config_file)

# MODAY_PATH/conf/mail.ini
mail_file = (os.path.join(MONDAY_PATH,'conf','mail.ini'),
                os.path.join(MONDAY_PATH,'conf','mail.custom.ini') )
mail = configparser.ConfigParser()
mail.read(mail_file)

# MONDAY_PATH/conf/mysql.ini
mysql_file = (os.path.join(MONDAY_PATH,'conf','mysql.ini'),
                os.path.join(MONDAY_PATH,'conf','mysql.custom.ini') )
mysql = configparser.ConfigParser()
mysql.read(mysql_file)

# MONDAY_PATH/conf/sendlist.ini
sendlist_file = (os.path.join(MONDAY_PATH,'conf','send_list.ini'),
                os.path.join(MONDAY_PATH,'conf','send_list.custom.ini') )
sendlist = configparser.ConfigParser()
sendlist.read(sendlist_file)
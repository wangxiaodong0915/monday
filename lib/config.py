import os
import os.path
import configparser
import logging

MONDAY_PATH = os.getenv('MONDAY_PATH')

config_file = (os.path.join(MONDAY_PATH,'conf','config.ini'),
                os.path.join(MONDAY_PATH,'conf','config.custom.ini') )
config = configparser.ConfigParser()
config.read(config_file)

mail_file = (os.path.join(MONDAY_PATH,'conf','mail.ini'),
                os.path.join(MONDAY_PATH,'conf','mail.custom.ini') )
mail = configparser.ConfigParser()
mail.read(mail_file)



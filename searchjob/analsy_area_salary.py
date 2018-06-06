# -*- coding: UTF-8 -*-
# !/usr/bin/python3
# @version: V
# @author: 飞翔的卡夫卡
# @contact: 592901924@qq.com
# @site: 
# @software: PyCharm
# @file: analsy_area_salary.py
# @time: 2018/6/4 11:51
# @python：python3.6

import jieba
import jieba.posseg as pseg
import jieba.analyse

import config
import mondayMysql

UNIT_CONVERSION = {"千":1000
                   ,"万":10000
                   ,"百":100
                   ,"十":10
                   ,"一":1
                   ,"两":2}

#把中文内容转换成数字信息
def transformToNumber(salary):
    """
    :param salary:一个中文描述的字段，包含最低薪资，最高薪资
    :return: 返回最低薪资和最高薪资的数字，单位：元
    """
    # salary_list = list(jieba.cut(row[0], cut_all=False))
    # ['0.8', '-', '1.6', '万', '/', '月']
    # ['2', '万', '以下', '/', '年']
    if "/月" in salary:
        salary_list = list(jieba.cut(salary, cut_all=False))
        if "以下" in salary:
            salary_min = 0.0
            salary_max = round(float(salary_list[0]) * UNIT_CONVERSION[salary_list[1]] , 2)
        elif "以上" in salary:
            salary_min = round(float(salary_list[0]) * UNIT_CONVERSION[salary_list[1]] , 2)
            salary_max = float("inf")
        else:
            salary_min = round(float(salary_list[0]) * UNIT_CONVERSION[salary_list[3]] , 2)
            salary_max = round(float(salary_list[2]) * UNIT_CONVERSION[salary_list[3]] , 2)
        return salary_min, salary_max
    elif "/年" in salary:
        salary_list = list(jieba.cut(salary, cut_all=False))
        if "以下" in salary:
            salary_min = 0.0
            salary_max = round(float(salary_list[0]) * UNIT_CONVERSION[salary_list[1]] / 12 , 2)
        elif "以上" in salary:
            salary_min = round(float(salary_list[0]) * UNIT_CONVERSION[salary_list[1]] / 12 , 2)
            salary_max = float("inf")
        else:
            # print(salary_list)
            salary_min = round(float(salary_list[0]) * UNIT_CONVERSION[salary_list[3]] / 12 , 2)
            salary_max = round(float(salary_list[2]) * UNIT_CONVERSION[salary_list[3]] / 12 , 2)
        return salary_min, salary_max
    else:
        return 0, 0

def workExperience(experience):
    """
    把爬到的汉字转换成数字
    :param experience: 工作经验描述
    :return:
    """
    if "无工作经验" in experience:
        return 0 , 0
    elif "-" in experience:
        exper_list = list(jieba.cut(experience, cut_all=False))
        exper_min = int(exper_list[0])
        exper_max = int(exper_list[2])
        return exper_min , exper_max
    elif "年经验" in experience:
        exper_list = list(jieba.cut(experience, cut_all=False))
        exper_min = 0
        exper_max = int(exper_list[0])
        return exper_min , exper_max
    else:
        return 0 , 0


# 获取mysql信息
host = config.mysql['mysql_scrapy']['host']
user = config.mysql['mysql_scrapy']['user']
password = config.mysql['mysql_scrapy']['password']
database = config.mysql['mysql_scrapy']['database']
conn = mondayMysql.mondayMysql(host, user, password, database)
conn.connect()

# 转换salary
# sql = """
# select salary from qcwy;
# """
# result = conn.execute(sql)
# # for row in result:
# #     print(row[0],'\n')
# #     print(transformToNumber(row[0]))

# # 转换工作经验
# sql = """
# select experience from qcwy;
# """
# result = conn.execute(sql)
# for row in result:
#     print(row[0],'\n')
#     print(workExperience(row[0]))

# # 截取workplace
# sql = """
# select workplace from qcwy;
# """
# result = conn.execute(sql)
# for row in result:
#     print(row[0],'\n')
#     print(list(jieba.cut(row[0],cut_all=False)))

# # 截取positionname
# sql = """
# select positionname from qcwy;
# """
# result = conn.execute(sql)
# for row in result:
#     print(row[0],'\n')
#     print(list(jieba.cut(row[0],cut_all=False)))

def avg(salary_min, salary_max):
    pass

# # 截取positionname
sql = """
select salary,experience,Positionname from qcwy;
"""
results = conn.execute(sql)

T_list = []
for row in results:
    salary_min , salary_max = transformToNumber(row[0])
    workExper_min , workExper_max = workExperience(row[1])
    positionname = row[2]
    T_list.append([salary_min, salary_max, workExper_min, workExper_max, positionname])

# 把转换的数据写入DataFrom中
from pandas.core.frame import DataFrame

# 取交集

df = DataFrame(T_list)
print(df[(df[4] == "项目经理") & (df[0] < 100000)].reset_index(drop=True).describe())

# df_pm = df[df[4] == "项目经理"]
# import matplotlib.pyplot as plt
# plt.style.use("ggplot")
# import numpy as np
# fig , ax = plt.subplots(sharex=True, figsize = (9,6))
# ax.scatter(df_pm[df_pm[0] < 100000][3], df_pm[df_pm[0] < 100000][0],color="green")
# ax.set_ylabel("Salary < 100000", fontsize = 10)
# ax.set_xlabel("Experience = Project Manager", fontsize = 12)
# plt.title("Salary VS Experience", fontsize = 14, y=1.01)
# plt.show()

# df_db = df[df[4]=="数据分析师"]
# import matplotlib.pyplot as plt
# plt.style.use("ggplot")
# import numpy as np
# fig , ax = plt.subplots(sharex=True, figsize = (9,6))
# ax.scatter(df_db[df_db[0] < 100000][3], df_db[df_db[0] < 100000][0],color="blue")
# ax.set_ylabel("Salary < 100000", fontsize = 10)
# ax.set_xlabel("Experience = Data Analyst", fontsize = 12)
# plt.title("Salary VS Experience", fontsize = 14, y=1.01)
# plt.show()

df_ProM = df[df[4] == "产品经理"]
import matplotlib.pyplot as plt
plt.style.use("ggplot")
import numpy as np
fig , ax = plt.subplots(sharex=True, figsize = (9,6))
ax.scatter(df_ProM[df_ProM[0] < 60000][3], df_ProM[df_ProM[0] < 60000][0],color="blue")
ax.set_ylabel("Salary < 100000", fontsize = 10)
ax.set_xlabel("Experience = Product Manager", fontsize = 12)
plt.title("Salary VS Experience", fontsize = 14, y=1.01)
plt.show()
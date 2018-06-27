# -*- coding: UTF-8 -*-
# !/usr/bin/python3
# @version: V1.0
# @author: 飞翔的卡夫卡
# @contact: 592901924@qq.com
# @site: 
# @software: PyCharm
# @file: caixin_company.py
# @time: 2018/6/27 11:25
# @python：python3.6

#读入csv数据
import jieba
import pandas as pd
import os
import jieba.posseg as pseg

# 读取数据文件到pandas中
file_path = "D:/event/httpcompanies.caixin.com"
datafile="20180627日采集财新数据.csv"
df = pd.read_csv(os.path.join(file_path,datafile),encoding='utf-8',engine='python',names=['datetime', 'content'])
# print(df)

# **********************************************************
# 解析数据
# 目的：获取到新闻报道的实体和事情及发生的时间
# 步骤：
#     1.分词
#     2.提取词性
#     3.选择nr和 ns、t 保留
#     4.保留n & vn
#     5.判断主题和事件发生的概率
# ***********************************************************

def jiebacut(stat, module="default"):
    seg_list = jieba.cut(stat, cut_all=False, HMM=True)
    return "默认模式：" + "/".join(seg_list)

# print(df['content'])
#
# 遍历df["content]
# for x in df['content']:
#     print(type(x))
#     print(x)
os.chdir('d:/pycharmworkspace/monday/event/data/jieba_out')
for x in df['content']:
    if x is not None:
        str1 = jiebacut(x)
        with open('result.txt', encoding='utf-8', mode='a') as file:
            file.writelines(str1)
        words = pseg.cut(x, HMM=False)
        for w in words:
            str2 = "%s %s \n" % (w.word, w.flag)
            with open('result.txt', encoding='utf-8', mode='a') as file:
                file.writelines(str2)
    else:
        print("None is pass")


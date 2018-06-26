# -*- coding: UTF-8 -*-
# !/usr/bin/python3
# @version: V
# @author: 飞翔的卡夫卡
# @contact: 592901924@qq.com
# @site: 
# @software: PyCharm
# @file: jieba_test.py
# @time: 2018/6/26 14:37
# @python：python3.6

import jieba

stat = "王晓东使用jieba进行分词，并对词性进行标注。"

# seg_list = jieba.cut("我来到北京清华大学", cut_all=True, HMM=False)
# print("Full Mode: " + "/ ".join(seg_list))  # 全模式
#
# seg_list = jieba.cut("我来到北京清华大学", cut_all=False, HMM=True)
# print("Default Mode: " + "/ ".join(seg_list))  # 默认模式
#
# seg_list = jieba.cut("他来到了网易杭研大厦", HMM=False)
# print(", ".join(seg_list))
#
# seg_list = jieba.cut_for_search("小明硕士毕业于中国科学院计算所，后在日本京都大学深造", HMM=False)  # 搜索引擎模式
# print(", ".join(seg_list))

seg_list = jieba.cut(stat, cut_all=True, HMM=False)
print("全模式：" + "/".join(seg_list))

seg_list = jieba.cut(stat, cut_all=False, HMM=True)
print("默认模式：" + "/".join(seg_list))
#
# seg_list = jieba.cut(stat, cut_all=True, HMM=True)
# print("模式：" + "/".join(seg_list))

seg_list = jieba.cut_for_search(stat, HMM=False)
print("搜索引擎模式：" + "/".join(seg_list))

import jieba.posseg as pseg
# 使用posseg进行分词并显示词性

words = pseg.cut(stat, HMM=False)
for w in words:
    print("%s %s" %(w.word, w.flag))



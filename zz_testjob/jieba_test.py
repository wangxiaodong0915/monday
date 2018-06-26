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

print('*' * 60)
stat = "近期，一些第三方平台打着“创业”“创新”的旗号，以“购物返本”“消费等于赚钱”“你消费我还钱”为噱头，承诺高额甚至全额返还消费款、加盟费等，以此吸引消费者、商家投入资金。此类“消费返利”不同于正常商家返利促销活动，存在较大风险隐患"
print('stat = %s' % stat)
print('*' * 60)

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
# jieba.load_userdict('dict.txt')

print('*' * 60)
seg_list = jieba.cut(stat, cut_all=True, HMM=False)
print("全模式：" + "/".join(seg_list))
print('*' * 60)
seg_list = jieba.cut(stat, cut_all=False, HMM=True)
print("默认模式：" + "/".join(seg_list))
print('*' * 60)
# seg_list = jieba.cut(stat, cut_all=True, HMM=True)
# print("模式：" + "/".join(seg_list))
print('*' * 60)
seg_list = jieba.cut_for_search(stat, HMM=False)
print("搜索引擎模式：" + "/".join(seg_list))
print('*' * 60)
print('import jieba.posseg as pseg')
import jieba.posseg as pseg

# 使用posseg进行分词并显示词性
words = pseg.cut(stat, HMM=False)
for w in words:
    print("%s %s" % (w.word, w.flag))

print('*' * 60)

# 关键词提取
print('关键词提取')
import jieba.analyse  as ana

words = ana.extract_tags(stat, topK=5, withWeight=False, allowPOS=('x', 'n'))
print(type(words))
print('/'.join(words))

# 基于TextRank的关键词提取
print('*' * 60)
print('关键词提取-TextRank')
for x, w in ana.textrank(stat, withWeight=True):
    print('%s %s' % (x, w))

print('*' * 60)

# result = jieba.tokenize(stat.encode('utf-8').decode('utf-8'))
result = jieba.tokenize(stat)
for tk in result:
    print("word %s \t\t start: %d \t\t end: %d" % (tk[0], tk[1], tk[2]))
print('*' * 60)

from jieba.analyse import ChineseAnalyzer


analyzer = ChineseAnalyzer()

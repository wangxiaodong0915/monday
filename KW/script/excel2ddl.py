# -*- coding: UTF-8 -*-
# !/usr/bin/python3
# @version: V
# @author: 飞翔的卡夫卡
# @contact: 592901924@qq.com
# @site: 
# @software: PyCharm
# @file: excel2ddl.py
# @time: 2018/6/29 15:51
# @python：python3.6



import xlrd
import cx_Oracle
from jinja2 import Environment, PackageLoader

# 全局DDL语句
def read_excel(file):
    # open file
    workbook = xlrd.open_workbook(file)
    print("read excel: %s" % file)
    # 获取所有sheet页名称
    return workbook,workbook.sheet_names()

def read_dict(sheet_by_name, sheetname):
    # 输入一个sheet实例
    table_dict = {}
    # { "table":[("col1","type","字段中文名1"),("col2","type","字段中文名2")],"table_comment":"表中文名"}
    cell_c2 = sheet_by_name.cell(1,2).value
    table_name = cell_c2
    cell_c3 = sheet_by_name.cell(2,2).value
    table_name_comment = ''
    if cell_c3 is not None and cell_c3 != '':
        table_name_comment = cell_c3
    else:
        table_name_comment = sheetname
    table_dict[table_name + 'comment'] = table_name_comment
    # table_dict[table_name] = []
    cols_list = []
    nrow = sheet_by_name.nrows
    ncol = sheet_by_name.ncols
    i = 7
    while i:
        # {i,2}:colname;(i,3):type;(i,4):colcomment;(i,5):not null;(i,6):PK
        if i < nrow:
            if sheet_by_name.cell(i,2).value is not None and sheet_by_name.cell(i,2).value != '':
                col = (sheet_by_name.cell(i,2).value, sheet_by_name.cell(i,3).value, sheet_by_name.cell(i,4).value, sheet_by_name.cell(i,5).value, sheet_by_name.cell(i,6).value,)
                cols_list.append(col)
                i += 1
            else:
                break
        else:
            break
    table_dict[table_name] = cols_list
    print( "return dict about %s" % table_name)
    return table_dict,table_name

def dict2ddl(table_dict,table_name):
    # 把dict转换成ddl语句
    ddl = """"""
    env = Environment(loader=PackageLoader('html', 'templates'))  # html 为包名 templates为包中读取report.html的路径名
    template = env.get_template('template_oracle_ddl.sql')
    ddl = template.render(
        col_lists = table_dict[table_name],
        table_name = table_name,
        table_name_comment = table_dict[table_name + 'comment']
    )
    print("return ddl about %s" % table_name)
    return ddl

if __name__ == '__main__':
    excel_file = "D:/000-知因智慧/018_KW/001_数据字典/KW-数据中心-数据集市清单表.xlsx"
    workbook,sheet_list = read_excel(excel_file)
    ddl = ""
    ddl_drop = ""
    for sheetname in sheet_list:
        if sheetname != "目录":
            sheet_by_name = workbook.sheet_by_name(sheetname)
            print("start to make dict about %s" % sheetname)
            table_dict, table_name = read_dict(sheet_by_name, sheetname)
            ddl += dict2ddl(table_dict, table_name)
            ddl_drop += "DROP TABLE %s;\n" % table_name
        else:
            print("sheet$首页 跳过")
    ddl += "\n COMMIT;"
    with open('KW_oracle_drop.ddl', mode='w',encoding='utf-8') as file:
        file.writelines(ddl_drop)
    with open('KW_oracle.ddl', mode='w',encoding='utf-8') as file:
        file.writelines(ddl)
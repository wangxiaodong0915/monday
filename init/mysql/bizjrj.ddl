CREATE TABLE biejrj_news
(
title varchar(100) COMMENT '标题' ,
release_time TIMESTAMP COMMENT '发布时间',
news_source varchar(50) COMMENT '新闻来源',
body varchar(5000) COMMENT '正文',
editor varchar(20) COMMENT '责任编辑',
source_path varchar(100) COMMENT '来源网址',
swoop_path varchar(100) COMMENT '抓取网址',
swoop_time TIMESTAMP COMMENT '抓取时间'
) COMMENT '金融界';


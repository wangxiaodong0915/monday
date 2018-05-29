# monday
commit monday v1.0

/monday
    /conf #配置信息
    /lib
        /html/templates #jinja2的html模板
        /config.py #读取conf目录里的配置信息
        /mondayAES.py #加密，暂没有用
        /mondayDate.py #时间处理模块
        /mondayLog.py #日志模块
        /mondayMysql.py #Mysql引擎
        /mondayTimer.py #任务计时器
        /sendmail.py #邮件发送模块
    /init
        /mysql #mysql初始化语句
    /script #单独运行脚本
        /pistatussend.py #发送宿主机的内存、CPU状态
        /pistatussend_V2.py #发送宿主机的内存、CPU状态,使用jinja2模块
    /UCAS #国科大信息采集
        /getclassmsg.py #采集国科大每周末课程安排信息，并与周五前发送到邮箱
    /zz_gov #新闻信息采集

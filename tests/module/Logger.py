#!/usr/bin/python
# -*- coding: utf-8 -*-

#import basic modules
import sys,os
import logging
import logging.config
import logging.handlers

CurrentDir = os.path.dirname(os.path.abspath(__file__))
print("Logger.CurrentDir="+str(CurrentDir))

Python_Log_Dir = CurrentDir
Python_Log_Dir = os.path.dirname(Python_Log_Dir)
Python_Log_Dir = os.path.join(Python_Log_Dir,"PythonLog")
print("Logger.Python_Log_Dir="+str(Python_Log_Dir))

if not os.path.isdir(Python_Log_Dir):
  os.makedirs(Python_Log_Dir)
# logging.config.fileConfig(logger_config_path)
# logger = logging.getLogger("root")

logger = logging.getLogger()
logger.setLevel(level=logging.DEBUG)

logfile =  os.path.join(Python_Log_Dir,"PythonRunningLog.log")
print("Logger.logfile="+str(logfile))
file_loghandler = logging.FileHandler(logfile, mode='a',encoding='utf-8')
file_loghandler.setLevel(logging.DEBUG)
file_logformatter = logging.Formatter('%(asctime)s %(filename)s [line:%(lineno)d] %(levelname)s %(message)s ([processid:%(process)d] %(threadName)s [threadid:%(thread)d])')
file_loghandler.setFormatter(file_logformatter)
logger.addHandler(file_loghandler)



# 定义一个Handler打印INFO及以上级别的日志到sys.stderr
console_loghandler = logging.StreamHandler()
console_loghandler.setLevel(logging.DEBUG)
console_logformatter = logging.Formatter('%(asctime)s %(filename)s [line:%(lineno)d] %(levelname)s %(message)s ([processid:%(process)d] %(threadName)s [threadid:%(thread)d])')
console_loghandler.setFormatter(console_logformatter)
logger.addHandler(console_loghandler)




logger.debug("Logger.called")



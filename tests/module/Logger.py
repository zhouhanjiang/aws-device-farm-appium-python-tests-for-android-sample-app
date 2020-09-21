#!/usr/bin/python
# -*- coding: utf-8 -*-

#import basic modules
import sys,os
import logging
import logging.config
import logging.handlers



if not os.path.isdir("../PythonLog"):
  os.makedirs("../PythonLog")
logging.config.fileConfig("../Config/logger.conf")
logger = logging.getLogger("root")






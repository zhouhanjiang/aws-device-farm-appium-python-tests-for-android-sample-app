#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright 2016 Amazon.com, Inc. or its affiliates. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License").
# You may not use this file except in compliance with the License.
# A copy of the License is located at
#
# http://aws.amazon.com/apache2.0
#
# or in the "license" file accompanying this file. This file is distributed
# on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either
# express or implied. See the License for the specific language governing
# permissions and limitations under the License.

import unittest
from appium import webdriver
from tests.pages import *
import time,os
from tests.module.Logger import logger

class BaseTest(unittest.TestCase):
    """Basis for all tests."""
    def setUp(self):
        """Sets up desired capabilities and the Appium driver."""
        url = 'http://127.0.0.1:4723/wd/hub'
        desired_caps = {}

        """
        The following desired capabilities must be set when running locally.
        Make sure they are NOT set when uploading to Device Farm.

        desired_caps['platformName'] = 'Android'
        desired_caps['deviceName'] = 'aPhone'
        """
        desired_caps['platformName'] = 'Android'
        desired_caps['deviceName'] = 'aPhone'
        desired_caps['appPackage'] = 'com.amazonaws.devicefarm.android.referenceapp'
        desired_caps['appActivity'] = 'com.amazonaws.devicefarm.android.referenceapp.Activities.MainActivity'
        desired_caps['appWaitDuration'] = '300000'
        desired_caps['unicodeKeyboard'] = True  # 输入中文时要加，要不然输入不了中文
        desired_caps['resetKeyboard'] = True  # 输入中文时要加，要不然输入不了中文
        #desired_caps["autoGrantPermissions"] = True  # 设置自动授权权限

        logger.debug("base_test.setUp.url="+str(url))
        logger.debug("base_test.setUp.desired_caps="+str(desired_caps))

        logger.debug("base_test.setUp.driver-->webdriver.Remote")
        self.driver = webdriver.Remote(url, desired_caps)

        for try_time in range(2):
          time.sleep(1)

          try:
            reinstall_continue_btn = self.driver.find_element_by_id("com.android.permissioncontroller:id/continue_button")
            logger.debug("BaseTest.setUp.reinstall_continue_btn="+str(reinstall_continue_btn))
            logger.debug("base_test.setUp.try_time="+str(try_time)+";reinstall_continue_btn="+str(reinstall_continue_btn))
            if reinstall_continue_btn is not None:
              time.sleep(5)
              reinstall_continue_btn.click()
          except Exception,msg:
            logger.debug("BaseTest.setUp.err,msg="+str(msg))

          try:
            time.sleep(1)
            reinstall_cfm_btn = self.driver.find_element_by_id("android:id/button1")
            #print("BaseTest.setUp.reinstall_continue_btn="+str(reinstall_continue_btn))
            logger.debug("base_test.setUp.try_time="+str(try_time)+";reinstall_continue_btn="+str(reinstall_continue_btn))
            if reinstall_cfm_btn is not None:
              time.sleep(5)
              reinstall_cfm_btn.click()
          except Exception,msg:
            logger.debug("BaseTest.setUp.err,msg="+str(msg))

        logger.debug("base_test.setUp.navigation_page-->NavigationPage")
        self.navigation_page = NavigationPage(self.driver)

    def tearDown(self):
        CurrentDir = os.path.dirname(os.path.abspath(__file__))

        if "DEVICEFARM_LOG_DIR" in os.environ:
          DEVICEFARM_LOG_DIR = os.environ["DEVICEFARM_LOG_DIR"]
        else:
          DEVICEFARM_LOG_DIR = CurrentDir
        DEVICEFARM_PYTHON_LOG = os.path.join(DEVICEFARM_LOG_DIR,"PythonRunningLog.log")
        logger.debug("base_test.tearDown.DEVICEFARM_LOG_DIR="+str(DEVICEFARM_LOG_DIR))
        logger.debug("base_test.tearDown.DEVICEFARM_PYTHON_LOG="+str(DEVICEFARM_PYTHON_LOG))
        if os.path.isfile(DEVICEFARM_PYTHON_LOG):
          os.remove(DEVICEFARM_PYTHON_LOG)

        print("base_test.setUp.CurrentDir="+str(CurrentDir))
        if str(CurrentDir).find("base_tests")>=0:
          PythonLogDir = os.path.dirname(CurrentDir)
          PythonLogDir = os.path.dirname(PythonLogDir)
          PythonLogDir = os.path.join(PythonLogDir,"PythonLog")
          logger.debug("base_test.tearDown.PythonLogDir="+str(PythonLogDir))
          if os.path.isdir(PythonLogDir):
            PythonLogFile = os.path.join(PythonLogDir,"PythonRunningLog.log")
            logger.debug("base_test.tearDown.PythonLogFile="+str(PythonLogFile))
            if os.name == "nt":
              cmd_str = os.system('copy ' +str(PythonLogFile)+' '+str(DEVICEFARM_PYTHON_LOG))
            else:
              cmd_str = os.system('cp ' +str(PythonLogFile)+' '+str(DEVICEFARM_PYTHON_LOG))
          else:
            PythonLogDir = ""

        """Shuts down the driver."""
        self.driver.quit()

    def get_name(self):
        logger.debug("base_test.get_name-->NotImplementedError")
        raise NotImplementedError

    def navigate_to_page(self):
        """Navigates to desired page."""
        logger.debug("base_test.navigate_to_page-->go_to_category")
        self.navigation_page.go_to_category(self.get_name())

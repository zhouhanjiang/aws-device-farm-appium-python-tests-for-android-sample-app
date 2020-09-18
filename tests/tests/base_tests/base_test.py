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
import time

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
        self.driver = webdriver.Remote(url, desired_caps)

        for try_time in range(2):
          time.sleep(1)

          try:
            reinstall_continue_btn = self.driver.find_element_by_id("com.android.permissioncontroller:id/continue_button")
            print("BaseTest.setUp.reinstall_continue_btn="+str(reinstall_continue_btn))
            if reinstall_continue_btn is not None:
              time.sleep(5)
              reinstall_continue_btn.click()
          except Exception,msg:
            print("BaseTest.setUp.err,msg="+str(msg))

          try:
            time.sleep(1)
            reinstall_cfm_btn = self.driver.find_element_by_id("android:id/button1")
            print("BaseTest.setUp.reinstall_continue_btn="+str(reinstall_continue_btn))
            if reinstall_cfm_btn is not None:
              time.sleep(5)
              reinstall_cfm_btn.click()
          except Exception,msg:
            print("BaseTest.setUp.err,msg="+str(msg))



        self.navigation_page = NavigationPage(self.driver)

    def tearDown(self):
        """Shuts down the driver."""
        self.driver.quit()

    def get_name(self):
        raise NotImplementedError

    def navigate_to_page(self):
        """Navigates to desired page."""
        self.navigation_page.go_to_category(self.get_name())

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

from base_tests.base_test import BaseTest
from tests.pages import LoginPage
from tests.module.Logger import logger

class LoginTest(BaseTest):
    """Container for all login page tests."""
    LOGIN_SUCCESS_MESSAGE = 'You are logged on as admin'
    LOGIN_FAILURE_MESSAGE = 'You gave me the wrong username and password'
    #PAGE_NAME = 'Login Page'
    PAGE_NAME = '(//android.widget.TextView[@content-desc="Row Category Name"])[8]'
    USERNAME = 'admin'
    VALID_PASSWORD = 'password'
    INVALID_PASSWORD = 'passwrod'

    logger.debug("LoginTest.__init__.LOGIN_SUCCESS_MESSAGE="+str(LOGIN_SUCCESS_MESSAGE)+";LOGIN_FAILURE_MESSAGE="+str(LOGIN_FAILURE_MESSAGE)+";PAGE_NAME="+str(PAGE_NAME))
    logger.debug("LoginTest.__init__.USERNAME="+str(USERNAME)+";VALID_PASSWORD="+str(VALID_PASSWORD)+";INVALID_PASSWORD="+str(INVALID_PASSWORD))

    def setUp(self):
        """Set up Appium connection and navigate to login page."""
        logger.debug("LoginTest.setUp.BaseTest.setUp")
        BaseTest.setUp(self)
        logger.debug("LoginTest.setUp.BaseTest.navigate_to_page")
        BaseTest.navigate_to_page(self)
        logger.debug("LoginTest.setUp.login.LoginPage")
        self.login = LoginPage(self.driver)

    def get_name(self):
        logger.debug("LoginTest.get_name.login.LoginPage")
        page_name = self.PAGE_NAME
        logger.debug("LoginTest.get_name.page_name="+str(page_name))
        return page_name


    def test_valid_login(self):
        """Login with valid credentials, verify valid login message, log out, verify back at log in."""
        logger.debug("LoginTest.test_valid_login.log_in")
        self.login.log_in(self.USERNAME, self.VALID_PASSWORD)
        self.assertEquals(self.login.get_message(), self.LOGIN_SUCCESS_MESSAGE)
        logger.debug("LoginTest.test_valid_login.login.click_alt_button")
        self.login.click_alt_button()
        self.assertTrue(self.login.is_at_login())

    def test_invalid_login(self):
        """Login with invalid credentials, verify invalid login message, try again, verify back at log in."""
        logger.debug("LoginTest.test_invalid_login.login.log_in")
        self.login.log_in(self.USERNAME, self.INVALID_PASSWORD)
        self.assertEquals(self.login.get_message(), self.LOGIN_FAILURE_MESSAGE)
        logger.debug("LoginTest.test_invalid_login.login.click_alt_button")
        self.login.click_alt_button()
        self.assertTrue(self.login.is_at_login())

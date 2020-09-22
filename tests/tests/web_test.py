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
from tests.pages import WebPage
from tests.module.Logger import logger


class WebTest(BaseTest):
    """Container for all web page tests."""
    URL = 'https://aws.amazon.com/documentation/devicefarm/'
    BAD_INTERNET_CONNECTION_MSG = 'Likely a bad internet connection.'
    logger.debug("WebTest.__init__.BAD_INTERNET_CONNECTION_MSG="+str(BAD_INTERNET_CONNECTION_MSG)+";URL="+str(URL))

    def setUp(self):
        """Sets up Appium connection and navigates to web page."""
        logger.debug("WebTest.setUp.BaseTest.setUp")
        BaseTest.setUp(self)
        logger.debug("WebTest.setUp.BaseTest.navigate_to_page")
        BaseTest.navigate_to_page(self)
        logger.debug("WebTest.setUp.web_view.WebPage")
        self.web_view = WebPage(self.driver)

    def get_name(self):
        #return 'Web'
        xpath_name = '(//android.widget.TextView[@content-desc="Row Category Name"])[2]'
        logger.debug("WebTest.get_name.xpath_name="+str(xpath_name))
        return xpath_name

    def test_web_view(self):
        """Goes to url, verifies web description is loaded."""
        logger.debug("WebTest.test_web_view.web_view.go_to_url")
        self.web_view.go_to_url(self.URL)
        self.assertTrue(self.web_view.web_description_is_loaded(), msg=self.BAD_INTERNET_CONNECTION_MSG)

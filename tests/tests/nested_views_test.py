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
from tests.pages import NestedViewsPage
import time
from tests.module.Logger import logger

class NestedViewsTest(BaseTest):
    """Container for all nested view page tests."""
    NEXT_LEVEL_CLICKS = 3
    BACK_BUTTON_CLICKS = 2
    BEFORE_COUNTER = 4
    AFTER_COUNTER = 2
    logger.debug("NestedViewsTest.__init__.NEXT_LEVEL_CLICKS="+str(NEXT_LEVEL_CLICKS)+";BACK_BUTTON_CLICKS="+str(BACK_BUTTON_CLICKS)+";BEFORE_COUNTER="+str(BEFORE_COUNTER)+";AFTER_COUNTER="+str(AFTER_COUNTER))

    def setUp(self):
        """Set up Appium connection and navigates to nested views page."""
        logger.debug("NestedViewsTest.setUp ---> BaseTest.setUp")
        BaseTest.setUp(self)
        logger.debug("NestedViewsTest.setUp ---> BaseTest.navigate_to_page")
        BaseTest.navigate_to_page(self)
        logger.debug("NestedViewsTest.setUp ---> NestedViewsPage")
        self.nested_views = NestedViewsPage(self.driver)

    def get_name(self):
        #return 'Nested Views'
        xpath_name = '	(//android.widget.TextView[@content-desc="Row Category Name"])[5]'
        logger.debug("NestedViewsTest.get_name.xpath_name="+str(xpath_name))
        return xpath_name

    def test_up_navigation(self):
        """Goes up a level, verifies text, goes down a level, verifies text."""
        time.sleep(1)
        logger.debug("NestedViewsTest.test_up_navigation.nested_views ---> press_up_navigation")
        self.nested_views.press_up_navigation()
        self.assertTrue(self.nested_views.first_level_text_is_displayed())

        time.sleep(1)
        logger.debug("NestedViewsTest.test_up_navigation.nested_views ---> press_next_level")
        self.nested_views.press_next_level()
        self.assertTrue(self.nested_views.final_level_text_is_displayed())

        time.sleep(1)
        logger.debug("NestedViewsTest.test_up_navigation.nested_views ---> press_up_navigation_back_button")
        #self.nested_views.press_up_navigation_back_button()
        self.nested_views.press_back_button()
        self.assertTrue(self.nested_views.first_level_text_is_displayed())

    def test_back_navigation(self):
        """Get initial page counter, press next level a NEXT_LEVEL_CLICKS times, verifies counter.
        Press back button BACK_BUTTON_CLICKS times, verifies counter.
        """
        time.sleep(1)
        logger.debug("NestedViewsTest.test_back_navigation.nested_views ---> press_back_navigation")
        self.nested_views.press_back_navigation()

        for __ in range(self.NEXT_LEVEL_CLICKS):
            logger.debug("NestedViewsTest.test_back_navigation.nested_views ---> press_next_level")
            self.nested_views.press_next_level()
            time.sleep(1)

        self.assertEquals(self.nested_views.get_counter(), self.BEFORE_COUNTER)

        for __ in range(self.BACK_BUTTON_CLICKS):
            logger.debug("NestedViewsTest.test_back_navigation.nested_views ---> press_back_button")
            self.nested_views.press_back_button()
            time.sleep(1)

        self.assertEquals(self.nested_views.get_counter(), self.AFTER_COUNTER)

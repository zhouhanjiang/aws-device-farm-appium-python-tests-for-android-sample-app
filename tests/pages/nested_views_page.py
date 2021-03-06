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

from tests.pages.base_pages.base_page import BasePage
import time
from tests.module.Logger import logger

class NestedViewsPage(BasePage):
    """Nested views page representation."""
    #UP_NAVIGATION_NAME = 'UP NAVIGATION'
    UP_NAVIGATION_ID = 'com.amazonaws.devicefarm.android.referenceapp:id/nested_up_button'
    #BACK_NAVIGATION_NAME = 'BACK NAVIGATION'
    BACK_NAVIGATION_ID = 'com.amazonaws.devicefarm.android.referenceapp:id/nested_back_button'
    #FIRST_LEVEL_TEXT_NAME = 'Press to go to the next level'
    FIRST_LEVEL_TEXT_ID = 'com.amazonaws.devicefarm.android.referenceapp:id/up_navigation_content_text'
    #FINAL_LEVEL_TEXT_NAME = 'Final Level'
    #FINAL_LEVEL_TEXT_ID = 'com.amazonaws.devicefarm.android.referenceapp:id/up_navigation_content_text'
    FINAL_LEVEL_TEXT_XPATH = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.TextView'
    #NEXT_LEVEL_BUTTON_NAME = 'NEXT LEVEL'
    #NEXT_LEVEL_BUTTON_ID = 'com.amazonaws.devicefarm.android.referenceapp:id/nested_up_button'
    NEXT_LEVEL_XPATH = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.Button'
    #COUNTER_NAME = 'Level Display'
    COUNTER_ID = 'com.amazonaws.devicefarm.android.referenceapp:id/back_navigation_counter'
    #UP_NAVIGATION_BACK_BUTTON_NAME = 'Navigate up'
    #UP_NAVIGATION_BACK_BUTTON_ID = '转到上一层级'
    UP_NAVIGATION_BACK_BUTTON_XPATH = '//android.widget.ImageButton[@content-desc="转到上一层级"]'
    logger.debug("NestedViewsPage.__init__.UP_NAVIGATION_ID="+str(UP_NAVIGATION_ID)+";BACK_NAVIGATION_ID="+str(BACK_NAVIGATION_ID)+";FIRST_LEVEL_TEXT_ID="+str(FIRST_LEVEL_TEXT_ID))
    logger.debug("NestedViewsPage.__init__.FINAL_LEVEL_TEXT_XPATH="+str(FINAL_LEVEL_TEXT_XPATH)+";NEXT_LEVEL_XPATH="+str(NEXT_LEVEL_XPATH)+";COUNTER_ID="+str(COUNTER_ID))
    logger.debug("NestedViewsPage.__init__.UP_NAVIGATION_BACK_BUTTON_XPATH="+str(UP_NAVIGATION_BACK_BUTTON_XPATH))

    def press_up_navigation(self):
        """Press up navigation button."""
        #up_navigation = self.driver.find_element_by_name(self.UP_NAVIGATION_NAME)
        time.sleep(1)
        up_navigation = self.driver.find_element_by_id(self.UP_NAVIGATION_ID)
        logger.debug("NestedViewsPage.press_up_navigation.up_navigation="+str(up_navigation))
        time.sleep(1)
        logger.debug("NestedViewsPage.press_up_navigation.up_navigation.click")
        up_navigation.click()

    def press_back_navigation(self):
        """Press back navigation button."""
        #back_navigation = self.driver.find_element_by_name(self.BACK_NAVIGATION_NAME)
        time.sleep(1)
        back_navigation = self.driver.find_element_by_id(self.BACK_NAVIGATION_ID)
        logger.debug("NestedViewsPage.press_back_navigation.back_navigation="+str(back_navigation))
        time.sleep(1)
        logger.debug("NestedViewsPage.press_back_navigation.back_navigation.click")
        back_navigation.click()

    def first_level_text_is_displayed(self):
        """Returns visibility of first level text as a boolean."""
        #first_level_text = self.driver.find_element_by_name(self.FIRST_LEVEL_TEXT_NAME)
        time.sleep(1)
        first_level_text = self.driver.find_element_by_id(self.FIRST_LEVEL_TEXT_ID)
        logger.debug("NestedViewsPage.first_level_text_is_displayed.first_level_text="+str(first_level_text))
        time.sleep(1)
        return first_level_text.is_displayed()

    def final_level_text_is_displayed(self):
        """Returns visibility of final level text as a boolean."""
        #final_level_text = self.driver.find_element_by_name(self.FINAL_LEVEL_TEXT_NAME)
        time.sleep(1)
        #final_level_text = self.driver.find_element_by_id(self.FINAL_LEVEL_TEXT_ID)
        final_level_text = self.driver.find_element_by_xpath(self.FINAL_LEVEL_TEXT_XPATH)
        logger.debug("NestedViewsPage.final_level_text_is_displayed.final_level_text="+str(final_level_text))
        time.sleep(1)
        return final_level_text.is_displayed()

    def press_up_navigation_back_button(self):
        """Press up navigation back button."""
        #back_button = self.driver.find_element_by_id(self.UP_NAVIGATION_BACK_BUTTON_NAME)
        time.sleep(1)
        #back_button = self.driver.find_element_by_accessibility_id(self.UP_NAVIGATION_BACK_BUTTON_ID)
        back_button = self.driver.find_element_by_xpath(self.UP_NAVIGATION_BACK_BUTTON_XPATH)
        logger.debug("NestedViewsPage.press_up_navigation_back_button.back_button="+str(back_button))
        time.sleep(1)
        logger.debug("NestedViewsPage.press_up_navigation_back_button.back_button.click")
        back_button.click()

    def press_next_level(self):
        """Press next level button."""
        #next_level_button = self.driver.find_element_by_name(self.NEXT_LEVEL_BUTTON_NAME)
        #next_level_button = self.driver.find_element_by_id(self.NEXT_LEVEL_BUTTON_ID)
        time.sleep(1)
        next_level_button = self.driver.find_element_by_xpath(self.NEXT_LEVEL_XPATH)
        logger.debug("NestedViewsPage.press_next_level.next_level_button="+str(next_level_button))
        time.sleep(1)
        logger.debug("NestedViewsPage.press_next_level.next_level_button.click")
        next_level_button.click()

    def get_counter(self):
        """Returns the current page counter as an int."""
        #counter = self.driver.find_element_by_name(self.COUNTER_NAME)
        time.sleep(1)
        counter = self.driver.find_element_by_id(self.COUNTER_ID)
        logger.debug("NestedViewsPage.get_counter.counter="+str(counter))
        time.sleep(1)
        return int(counter.text)

    def press_back_button(self):
        """Press phone's back button."""
        logger.debug("NestedViewsPage.press_back_button.driver.click")
        self.driver.back()

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

from time import sleep
from tests.pages.base_pages.base_page import BasePage
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.touch_actions import TouchActions
from tests.module.Logger import logger


class NavigationPage(BasePage):
    """Class that handles navigation to different pages within the application."""
    NAV_DRAWER_TOGGLE_ID = 'ReferenceApp'
    RECYCLER_VIEW_ID = 'drawerList'
    NAV_DRAWER_ANIMATION_DELAY = 2
    MAX_ATTEMPTS = 5
    logger.debug("NavigationPage.__init__.NAV_DRAWER_TOGGLE_ID="+str(NAV_DRAWER_TOGGLE_ID)+";RECYCLER_VIEW_ID="+str(RECYCLER_VIEW_ID)
                 +";NAV_DRAWER_ANIMATION_DELAY="+str(NAV_DRAWER_ANIMATION_DELAY)+";MAX_ATTEMPTS="+str(MAX_ATTEMPTS))

    def scroll_nav_drawer_down(self):
        """Scroll the navigation drawer down."""
        recycler_view = self.driver.find_element_by_id(self.RECYCLER_VIEW_ID)
        logger.debug("NavigationPage.scroll_nav_drawer_down.recycler_view="+str(recycler_view))

        recycler_location_x = recycler_view.location['x']
        recycler_location_y = recycler_view.location['y']
        logger.debug("NavigationPage.scroll_nav_drawer_down.recycler_location_x="+str(recycler_location_x)+";recycler_location_y="+str(recycler_location_y))

        recycler_x_offset = recycler_view.size['width'] / 2
        recycler_height = recycler_view.size['height']
        recycler_y_start_offset = recycler_height * .95
        recycler_y_end_offset = recycler_height * .05
        logger.debug("NavigationPage.scroll_nav_drawer_down.recycler_x_offset="+str(recycler_x_offset)+";recycler_height="+str(recycler_height)
              +";recycler_y_start_offset="+str(recycler_y_start_offset)+";recycler_y_end_offset="+str(recycler_y_end_offset))

        mid_x = recycler_location_x + recycler_x_offset
        start_y = recycler_location_y + recycler_y_start_offset
        end_y = recycler_location_y + recycler_y_end_offset
        logger.debug("NavigationPage.scroll_nav_drawer_down.mid_x="+str(mid_x)+";start_y="+str(start_y)+";end_y="+str(end_y))

        action = TouchActions(self.driver)
        logger.debug("NavigationPage.scroll_nav_drawer_down.action="+str(action))
        logger.debug("NavigationPage.scroll_nav_drawer_down.action.tap_and_hold")
        action.tap_and_hold(mid_x, start_y).move(mid_x, end_y).release(mid_x, end_y).perform()

    def go_to_category(self, category_name):
        """Clicks appropriate button in the navigation drawer."""
        logger.debug("NavigationPage.go_to_category.category_name="+str(category_name)+";NAV_DRAWER_TOGGLE_ID="+str(self.NAV_DRAWER_TOGGLE_ID))
        NAV_DRAWER_TOGGLE = self.driver.find_element_by_accessibility_id(self.NAV_DRAWER_TOGGLE_ID)
        logger.debug("NavigationPage.go_to_category.NAV_DRAWER_TOGGLE="+str(NAV_DRAWER_TOGGLE))
        logger.debug("NavigationPage.go_to_category.NAV_DRAWER_TOGGLE.click")
        NAV_DRAWER_TOGGLE.click()

        sleep(self.NAV_DRAWER_ANIMATION_DELAY)

        category_element = None
        num_attempts = 0
        logger.debug("NavigationPage.go_to_category.category_element="+str(category_element)+";num_attempts="+str(num_attempts))

        while category_element is None and num_attempts < self.MAX_ATTEMPTS:
            try:
                #category_element = self.driver.find_element_by_name(category_name)
                #category_element = self.driver.find_element("xpath","//android.widget.TextView[@text='"+str(category_name)+"']")
                category_element = self.driver.find_element_by_xpath(category_name)
                num_attempts += 1
                logger.debug("NavigationPage.go_to_category.loop.category_element="+str(category_element)+";num_attempts="+str(num_attempts))
            except NoSuchElementException:
                self.scroll_nav_drawer_down()

        logger.debug("NavigationPage.go_to_category.loop.category_element.click")
        category_element.click()

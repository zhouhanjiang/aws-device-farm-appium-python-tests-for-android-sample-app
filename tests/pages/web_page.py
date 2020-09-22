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
from selenium.common.exceptions import NoSuchElementException
from tests.pages.base_pages.base_page import BasePage
from tests.module.Logger import logger

class WebPage(BasePage):
    """Custom web page representation."""
    NAV_BAR_SELECTOR = 'new UiSelector().textContains("http://www.amazon.com")'
    #FOCUSED_WEB_VIEW_SELECTOR = 'new UiSelector().focused(true).descriptionContains("aws")'
    FOCUSED_WEB_VIEW_SELECTOR = 'new UiSelector().textContains("Amazon")'
    KEYBOARD_ANIMATION_DELAY = 1
    WEBSITE_LOAD_TIME = 7
    logger.debug("WebPage.__init__.NAV_BAR_SELECTOR="+str(NAV_BAR_SELECTOR)+";FOCUSED_WEB_VIEW_SELECTOR="+str(FOCUSED_WEB_VIEW_SELECTOR)
                 +";KEYBOARD_ANIMATION_DELAY="+str(KEYBOARD_ANIMATION_DELAY)+";WEBSITE_LOAD_TIME="+str(WEBSITE_LOAD_TIME))

    def tap_screen_center(self):
        """Taps screen center."""
        window_size = self.driver.get_window_size()
        logger.debug("WebPage.tap_screen_center.window_size="+str(window_size))
        mid_x = window_size['width'] / 2
        mid_y = window_size['height'] / 2
        logger.debug("WebPage.tap_screen_center.mid_x="+str(mid_x)+";mid_y="+str(mid_y))
        self.driver.tap([(mid_x, mid_y)])

    def go_to_url(self, url):
        """Inputs url and presses enter."""
        logger.debug("WebPage.go_to_url.url="+str(url))
        nav_bar = self.driver.find_element_by_android_uiautomator(self.NAV_BAR_SELECTOR)
        logger.debug("WebPage.go_to_url.nav_bar="+str(nav_bar))
        sleep(self.KEYBOARD_ANIMATION_DELAY)  # keyboard will automatically pop up on some devices
        logger.debug("WebPage.go_to_url.nav_bar.send_keys")
        nav_bar.send_keys(url + '\n')
        sleep(self.WEBSITE_LOAD_TIME)

    def web_description_is_loaded(self):
        """Returns visibility of web view with appropriate description.

        Slight work around for consistency: tap the middle of the screen to give the web view focus,
        then check its description.
        """
        logger.debug("WebPage.web_description_is_loaded.tap_screen_center")
        self.tap_screen_center()
        try:
            web_view_loaded = self.driver.find_element_by_android_uiautomator(self.FOCUSED_WEB_VIEW_SELECTOR)
            logger.debug("WebPage.web_description_is_loaded.web_view_loaded="+str(web_view_loaded))
            return web_view_loaded.is_displayed()
        except NoSuchElementException:
            return False

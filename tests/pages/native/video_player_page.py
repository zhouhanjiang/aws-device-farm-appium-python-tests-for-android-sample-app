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
from selenium.common.exceptions import NoSuchElementException
from tests.module.Logger import logger

class VideoPlayerPage(BasePage):
    """Video player page representation."""
    VIDEO_VIEW_CLASS = 'android.widget.VideoView'
    #BAD_VIDEO_ALERT_NAME = "Can't play this video."
    BAD_VIDEO_ALERT_XPATH = '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.TextView'

    def video_is_displayed(self):
        """Returns visibility of video as boolean.

        Media player is incompatible with a small number of devices,
        checks for "Can't play this video" alert in this case.
        """
        logger.debug("VideoPlayerPage.video_is_displayed.VIDEO_VIEW_CLASS="+str(self.VIDEO_VIEW_CLASS)+";BAD_VIDEO_ALERT_XPATH="+str(self.BAD_VIDEO_ALERT_XPATH))
        try:
            video_element = self.driver.find_element_by_class_name(self.VIDEO_VIEW_CLASS)
        except NoSuchElementException:
            #video_element = self.driver.find_element_by_name(self.BAD_VIDEO_ALERT_NAME)
            video_element = self.driver.find_element_by_xpath(self.BAD_VIDEO_ALERT_XPATH)

        logger.debug("VideoPlayerPage.video_is_displayed.video_element="+str(video_element))
        return video_element.is_displayed()

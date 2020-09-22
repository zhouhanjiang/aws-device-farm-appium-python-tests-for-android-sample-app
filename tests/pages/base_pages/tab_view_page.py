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

from base_page import BasePage
from tests.module.Logger import logger

class TabViewPage(BasePage):
    """Base for a tab view page."""
    START_OFFSET = 0.85
    END_OFFSET = 0.15
    SWIPE_DURATION = 1000

    def go_to_next_page(self):
        """Swipes left to go to next page in tab view drawer."""
        logger.debug("TabViewPage.go_to_next_page.START_OFFSET="+str(self.START_OFFSET)+";END_OFFSET="+str(self.END_OFFSET)+";SWIPE_DURATION="+str(self.SWIPE_DURATION))
        size = self.driver.get_window_size()
        logger.debug("TabViewPage.go_to_next_page.size="+str(size))
        start_x = size['width'] * self.START_OFFSET
        end_x = size['width'] * self.END_OFFSET
        mid_y = size['height'] / 2
        logger.debug("TabViewPage.go_to_next_page.start_x="+str(start_x)+";end_x="+str(end_x)+";mid_y="+str(mid_y))

        logger.debug("TabViewPage.go_to_next_page.driver-->swipe")
        self.driver.swipe(start_x, mid_y, end_x, mid_y, self.SWIPE_DURATION)

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
from base_test import BaseTest
from tests.pages import TabViewPage
from tests.module.Logger import logger

class BaseTabTest(BaseTest):
    """Basis for any test for a page that must be swiped to."""
    ANIMATION_DELAY = 1
    logger.debug("BaseTabTest.__init__.ANIMATION_DELAY="+str(ANIMATION_DELAY))

    def get_name(self):
        """Returns name of view."""
        logger.debug("BaseTabTest.get_name.NotImplementedError")
        raise NotImplementedError

    def get_page_index(self):
        """Returns index of page within the drawer."""
        logger.debug("BaseTabTest.get_page_index.NotImplementedError")
        raise NotImplementedError

    def navigate_to_page(self):
        """Navigate to the drawer and swipe until it gets to desired page."""
        logger.debug("BaseTabTest.navigate_to_page.BaseTest.navigate_to_page")
        BaseTest.navigate_to_page(self)
        tab_view = TabViewPage(self.driver)
        logger.debug("BaseTabTest.navigate_to_page.tab_view="+str(tab_view))
        sleep(self.ANIMATION_DELAY)

        for __ in range(self.get_page_index()):
            logger.debug("BaseTabTest.navigate_to_page.tab_view.go_to_next_page")
            tab_view.go_to_next_page()
            sleep(self.ANIMATION_DELAY)

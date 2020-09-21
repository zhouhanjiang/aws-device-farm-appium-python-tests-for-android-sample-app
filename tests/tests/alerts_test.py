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
from tests.pages import AlertsPage
#from __init__ import *
from tests.module.Logger import logger

class AlertsTest(BaseTest):
    """Container for all alerts page tests."""
    #PAGE_NAME = 'Alerts'
    PAGE_NAME = '(//android.widget.TextView[@content-desc="Row Category Name"])[7]'

    def setUp(self):
        """Set up Appium connection and navigate to image gallery page."""
        logger.info("alerts_test.setUp-->BaseTest.setUp")
        BaseTest.setUp(self)
        logger.info("alerts_test.setUp-->BaseTest.navigate_to_page")
        BaseTest.navigate_to_page(self)
        logger.info("alerts_test.setUp-->self.alerts")
        self.alerts = AlertsPage(self.driver)

    def get_name(self):
        logger.info("alerts_test.get_name.PAGE_NAME="+str(self.PAGE_NAME))
        return self.PAGE_NAME

    def test_alert(self):
        """Clicks alert button, verifies alert text, accepts the alert message."""
        logger.info("alerts_test.test_alert.click_alert_button")
        self.alerts.click_alert_button()
        logger.info("alerts_test.test_alert.assertTrue--->alert_text_is_displayed")
        self.assertTrue(self.alerts.alert_text_is_displayed())
        logger.info("alerts_test.test_alert.accept_alert_message")
        self.alerts.accept_alert_message()

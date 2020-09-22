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

from tests.module.Logger import logger

class BasePage:
    """The basis for all pages."""
    IMPLICIT_WAIT_TIME = 10
    TIMEOUT = 30

    def __init__(self, driver):
        """Base constructor.

        Sets driver, implicit wait, and timeout.
        """
        logger.debug("BasePage.__init__.driver="+str(driver))
        logger.debug("BasePage.__init__.IMPLICIT_WAIT_TIME="+str(self.IMPLICIT_WAIT_TIME))
        logger.debug("BasePage.__init__.TIMEOUT="+str(self.TIMEOUT))
        self.driver = driver
        self.driver.implicitly_wait(self.IMPLICIT_WAIT_TIME)
        self.timeout = self.TIMEOUT

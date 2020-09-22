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
from tests.module.Logger import logger


class LoginPage(BasePage):
    """Login page representation."""
    #USERNAME_FIELD_ID = 'Username Input Field'
    USERNAME_FIELD_ID = 'com.amazonaws.devicefarm.android.referenceapp:id/username_text_input'
    #PASSWORD_FIELD_ID = 'Password Input Field'
    PASSWORD_FIELD_ID = 'com.amazonaws.devicefarm.android.referenceapp:id/password_text_input'
    #ALT_MESSAGE_ID = 'Alt Message'
    ALT_MESSAGE_ID = 'com.amazonaws.devicefarm.android.referenceapp:id/login_alt_message_textView'
    #ALT_BUTTON_ID = 'Alt Button'
    ALT_BUTTON_ID = 'com.amazonaws.devicefarm.android.referenceapp:id/alt_button'
    #LOG_IN_BUTTON_ID = 'Login Button'
    LOG_IN_BUTTON_ID = 'com.amazonaws.devicefarm.android.referenceapp:id/login_button'
    KEYBOARD_ANIMATION_DELAY = 1
    logger.debug("LoginPage.__init__.USERNAME_FIELD_ID="+str(USERNAME_FIELD_ID)+";PASSWORD_FIELD_ID="+str(PASSWORD_FIELD_ID)+";ALT_MESSAGE_ID="+str(ALT_MESSAGE_ID))
    logger.debug("LoginPage.__init__.ALT_BUTTON_ID="+str(ALT_BUTTON_ID)+";LOG_IN_BUTTON_ID="+str(LOG_IN_BUTTON_ID)+";KEYBOARD_ANIMATION_DELAY="+str(KEYBOARD_ANIMATION_DELAY))

    def log_in(self, username, password):
        """Types in inputted username and password and presses log in button."""
        logger.debug("LoginPage.log_in.username="+str(username)+";password="+str(password))
        username_field = self.driver.find_element_by_id(self.USERNAME_FIELD_ID)
        logger.debug("LoginPage.log_in.username_field="+str(username_field))
        password_field = self.driver.find_element_by_id(self.PASSWORD_FIELD_ID)
        logger.debug("LoginPage.log_in.password_field="+str(password_field))
        log_in_button = self.driver.find_element_by_id(self.LOG_IN_BUTTON_ID)
        logger.debug("LoginPage.log_in.log_in_button="+str(log_in_button))

        logger.debug("LoginPage.log_in.username_field.click")
        username_field.click()
        sleep(self.KEYBOARD_ANIMATION_DELAY)
        logger.debug("LoginPage.log_in.username_field.send_keys")
        username_field.send_keys(username)

        logger.debug("LoginPage.log_in.password_field.click")
        password_field.click()
        sleep(self.KEYBOARD_ANIMATION_DELAY)
        password_field.send_keys(password)
        logger.debug("LoginPage.log_in.password_field.send_keys")

        logger.debug("LoginPage.log_in.log_in_button.click")
        log_in_button.click()

    def get_message(self):
        """Returns the post-login page message."""
        message = self.driver.find_element_by_id(self.ALT_MESSAGE_ID)
        logger.debug("LoginPage.get_message.message="+str(message))
        return message.text

    def click_alt_button(self):
        """Tap try again or log in button."""
        alt_button = self.driver.find_element_by_id(self.ALT_BUTTON_ID)
        logger.debug("LoginPage.get_message.alt_button="+str(alt_button))
        alt_button.click()

    def is_at_login(self):
        """Returns whether or not we are back at the original login view as a boolean.

        Simply checks for the visibility of the login button.
        """
        log_in_button = self.driver.find_element_by_id(self.LOG_IN_BUTTON_ID)
        logger.debug("LoginPage.is_at_login.log_in_button="+str(log_in_button))
        return log_in_button.is_displayed()

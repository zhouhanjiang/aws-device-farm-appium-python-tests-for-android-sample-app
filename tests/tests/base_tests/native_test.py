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

from base_tab_test import BaseTabTest
from tests.module.Logger import logger

class NativeTest(BaseTabTest):
    """Basis for tests for pages within native drawer."""
    def get_page_index(self):
        logger.debug("NativeTest.get_page_index.NotImplementedError")
        raise NotImplementedError

    def get_name(self):
        native_xpath_name = '(//android.widget.TextView[@content-desc="Row Category Name"])[3]'
        logger.debug("NativeTest.get_name.native_xpath_name="+str(native_xpath_name))
        #return 'Native Components'
        return native_xpath_name

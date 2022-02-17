#  Copyright 2020-2022 Robert Bosch Car Multimedia GmbH
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
*** Settings ***
Documentation
...    First line.
...
...    Second paragraph

Resource    ./libs/testimport.resource

Library      RobotFramework_Testsuites    WITH NAME    testsuites

Suite Setup      testsuites.testsuite_setup
Suite Teardown   testsuites.testsuite_teardown
Test Setup       testsuites.testcase_setup
Test Teardown    testsuites.testcase_teardown


*** Test Cases ***
Test Case 0201
    [Documentation]    Documentation of test case
    Log    I am test '${TEST NAME}' of suite '${SUITE NAME}'    console=yes
    # TODO: Add return value to keyword implementation; check return value here
    test_keyword_1

Test Case 0201
    [Documentation]    Documentation of test case
    Log    I am test '${TEST NAME}' of suite '${SUITE NAME}'    console=yes




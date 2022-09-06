# **************************************************************************************************************
#  Copyright 2020-2022 Robert Bosch GmbH
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
# **************************************************************************************************************
#
# tutorial-03.robot
#
# dictionaries handling
#
# 0.2.0 / 06.09.2022
#
# --------------------------------------------------------------------------------------------------------------

*** Settings ***
Resource    ./libs/testimport.resource

Suite Setup       testsuites.testsuite_setup    ./config/testconfig.json
Suite Teardown    testsuites.testsuite_teardown
Test Setup        testsuites.testcase_setup
Test Teardown     testsuites.testcase_teardown

*** Test Cases ***
Test Case 03_01
    [documentation]    Log of a predefined dictionary
    Log    Test '${TEST NAME}' of suite '${SUITE NAME}'    console=yes
    log_dict    ${var_dict}

Test Case 03_02
    [documentation]    Access to dictionary keys
    Log    Test '${TEST NAME}' of suite '${SUITE NAME}'    console=yes

    # the key
    log_scalar    ${key_as_string}

    # -- accessing single elements

    # key name hard coded
    log_scalar    ${var_dict}[key_06]
    # key name as string type
    log_scalar    ${var_dict}[${key_as_string}]





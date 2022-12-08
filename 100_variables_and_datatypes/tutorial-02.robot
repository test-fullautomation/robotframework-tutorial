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
# tutorial-02.robot
#
# lists handling
#
# 0.2.1 / 08.12.2022
#
# --------------------------------------------------------------------------------------------------------------

*** Settings ***
Resource    ./libs/testimport.resource

Suite Setup       tm.testsuite_setup    ./config/testconfig.json
Suite Teardown    tm.testsuite_teardown
Test Setup        tm.testcase_setup
Test Teardown     tm.testcase_teardown

*** Test Cases ***

Test Case 02_01
    [documentation]    Log of a predefined list
    Log    Test '${TEST NAME}' of suite '${SUITE NAME}'    console=yes
    log_list    ${var_list}

Test Case 02_02
    [documentation]    Access to list elements
    Log    Test '${TEST NAME}' of suite '${SUITE NAME}'    console=yes

    # the indices
    log_scalar    ${index_as_string}
    log_scalar    ${index_as_integer}

    # -- accessing single elements

    # index hard coded
    log_scalar    ${var_list}[5]

    # index as string type
    log_scalar    ${var_list}[${index_as_string}]

    # index as integer type
    log_scalar    ${var_list}[${index_as_integer}]

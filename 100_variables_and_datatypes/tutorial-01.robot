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
# tutorial-01.robot
#
# scalar handling
#
# 0.1.0 / 05.09.2022
#
# --------------------------------------------------------------------------------------------------------------

*** Settings ***
Resource    ./libs/testimport.resource

Suite Setup       testsuites.testsuite_setup    ./config/testconfig.json
Suite Teardown    testsuites.testsuite_teardown
Test Setup        testsuites.testcase_setup
Test Teardown     testsuites.testcase_teardown

*** Test Cases ***
Test Case 01_01
    Log    Test '${TEST NAME}' of suite '${SUITE NAME}'    console=yes
    log_scalar    ${var_01}
    log_scalar    ${var_02}
    log_scalar    ${var_03}
    log_scalar    ${var_04}
    log_scalar    ${var_05}
    log_scalar    ${var_06}
    log_scalar    ${var_07}
    log_scalar    ${var_08}
    log_scalar    ${var_09}
    log_scalar    ${var_10}
    log_scalar    ${var_11}
    log_scalar    ${var_12}
    log_scalar    ${var_13}
    log_scalar    ${var_14}
    log_scalar    ${var_15}
    log_scalar    ${var_16}
    log_scalar    ${var_17}
    log_scalar    ${var_18}


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
Test Case 01_01
    [documentation]    Log of some predefined scalars
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

Test Case 01_02
    [documentation]    Arithmetical computation and concatenation of variables with different data types
    Log    Test '${TEST NAME}' of suite '${SUITE NAME}'    console=yes

    Set Test Variable    ${test_var_1}    1
    Set Test Variable    ${test_var_2}    2.3
    Set Test Variable    ${test_var_3}    ${3}
    Set Test Variable    ${test_var_4}    ${4.5}
    Set Test Variable    ${test_var_5}    A
    Set Test Variable    ${test_var_6}    B
    Set Test Variable    ${test_var_7}    'C'

    # arithmetical computation of two numbers defined as string
    ${result} =    Evaluate    ${test_var_1} + ${test_var_2}
    log_scalar     ${result}

    # arithmetical computation of two numbers defined as integer and float
    ${result} =    Evaluate    ${test_var_3} + ${test_var_4}
    log_scalar     ${result}

    # arithmetical computation of two numbers defined as string and float
    ${result} =    Evaluate    ${test_var_1} + ${test_var_4}
    log_scalar     ${result}

    # catenation of two numbers defined as string
    ${result} =    Catenate    ${test_var_1}    ${test_var_2}
    log_scalar     ${result}

    # catenation of two numbers defined as integer and float
    ${result} =    Catenate    ${test_var_3}    ${test_var_4}
    log_scalar     ${result}

    # catenation of two strings
    ${result} =    Catenate    ${test_var_5}    ${test_var_6}
    log_scalar     ${result}

    # catenation of an integer with a string (with quotes)
    ${result} =    Catenate    "${test_var_3}"    ${test_var_7}
    log_scalar     ${result}

    # catenation of two numbers defined as integer and float (with no space in between)
    ${test_var_7} =    Catenate    SEPARATOR=    ${test_var_3}    ${test_var_4}
    log_scalar     ${test_var_7}

    # arithmetical computation of the new variable test_var_7 (string) with an integer
    ${result} =    Evaluate    ${test_var_7} + ${test_var_3}
    log_scalar     ${result}



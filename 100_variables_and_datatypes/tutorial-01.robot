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


Test Case 01_03
    [documentation]    Comparison of variables in several combinations.
    Log    Test '${TEST NAME}' of suite '${SUITE NAME}'    console=yes

    # comparison of string variable with hard coded string
    ${status}=    Evaluate    "${var_01}" == "ABC"
    log_scalar    ${status}

    IF    ${status} == True
        Log    ${var_01} == ABC is True   console=yes
    ELSE
        Log    ${var_01} == ABC is False   console=yes
    END

    # comparison of two different kind of string variables (pay attention of the usage of the quotes)
    ${status}=    Evaluate    "${var_01}" == ${var_02}
    log_scalar    ${status}

    IF    ${status} == True
        Log    "${var_01}" == ${var_02} is True   console=yes
    ELSE
        Log    "${var_01}" == ${var_02} is False   console=yes
    END


    # comparison of a number (as string) with a number (as integer)
    ${status}=    Evaluate    ${var_04} == ${var_06}
    log_scalar    ${status}

    IF    ${status} == True
        Log    ${var_04} == ${var_06} is True   console=yes
    ELSE
        Log    ${var_04} == ${var_06} is False   console=yes
    END

    # comparison of a number (as string) with a number (as integer), (pay attention of the usage of the quotes)
    ${status}=    Evaluate    ${var_05} == "${var_06}"
    log_scalar    ${status}

    IF    ${status} == True
        Log    ${var_05} == "${var_06}" is True   console=yes
    ELSE
        Log    ${var_05} == "${var_06}" is False   console=yes
    END

    # comparison of boolean values
    ${status}=    Evaluate    ${var_10} == ${var_12}
    log_scalar    ${status}

    IF    ${status} == True
        Log    ${var_10} == ${var_12} is True   console=yes
    ELSE
        Log    ${var_10} == ${var_12} is False   console=yes
    END

    # comparison of numbers (as string)
    ${status}=    Evaluate    ${var_04} > ${var_07}
    log_scalar    ${status}

    IF    ${status} == True
        Log    ${var_04} > ${var_07} is True   console=yes
    ELSE
        Log    ${var_04} > ${var_07} is False   console=yes
    END

    # comparison of numbers (as string; short form)
    IF    ${var_04} > ${var_07}
        Log    ${var_04} > ${var_07} is True   console=yes
    ELSE
        Log    ${var_04} > ${var_07} is False   console=yes
    END

    # comparison of numbers (as integers; short form)
    IF    ${var_06} > ${var_09}
        Log    ${var_06} > ${var_09} is True   console=yes
    ELSE
        Log    ${var_06} > ${var_09} is False   console=yes
    END

    # comparison of numbers (one as string and one as integer; short form)
    IF    ${var_04} > ${var_09}
        Log    ${var_04} > ${var_09} is True   console=yes
    ELSE
        Log    ${var_04} > ${var_09} is False   console=yes
    END




# ${var_01}    ABC
# ${var_02}    "ABC"
# ${var_03}    ${ABC}
# ${var_04}    123
# ${var_05}    "123"
# ${var_06}    ${123}
# ${var_07}    4.56
# ${var_08}    "4.56"
# ${var_09}    ${4.56}
# ${var_10}    True
# ${var_11}    "True"
# ${var_12}    ${True}
# ${var_13}    False
# ${var_14}    "False"
# ${var_15}    ${False}
# ${var_16}    None
# ${var_17}    "None"
# ${var_18}    ${None}

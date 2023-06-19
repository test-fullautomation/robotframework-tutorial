# **************************************************************************************************************
#  Copyright 2020-2023 Robert Bosch GmbH
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
# 0.2.2 / 15.05.2023
#
# --------------------------------------------------------------------------------------------------------------

*** Settings ***
Resource    ./libs/testimport.resource

Suite Setup       tm.testsuite_setup    ./config/testconfig.jsonp
Suite Teardown    tm.testsuite_teardown
Test Setup        tm.testcase_setup
Test Teardown     tm.testcase_teardown

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

Test Case 01_04
    [documentation]    Working with variables taken from json configuration file
    Log    Test '${TEST NAME}' of suite '${SUITE NAME}'    console=yes

    # the content of the json parameters
    log_scalar    ${string_val}
    log_scalar    ${int_val}
    log_scalar    ${float_val}
    log_scalar    ${bool_val_1}
    log_scalar    ${bool_val_2}
    log_scalar    ${bool_val_3}
    log_scalar    ${bool_val_4}
    log_scalar    ${none_val}
    log_scalar    ${null_val}

    # comparisons between json parameters and resource parameters

    # comparison of numbers

    IF    ${int_val} == ${var_06}
        Log    ${int_val} == ${var_06} is True   console=yes
    ELSE
        Log    ${int_val} == ${var_06} is False   console=yes
    END

    # comparison of strings

    ${status}=    Evaluate    "${string_val}" != "${var_01}"
    log_scalar    ${status}

    IF    ${status} == True
        Log    "${string_val}" != "${var_01}" is True   console=yes
    ELSE
        Log    "${string_val}" != "${var_01}" is False   console=yes
    END

    IF    "${string_val}" != "${var_01}"
        Log    "${string_val}" != "${var_01}" is True   console=yes
    ELSE
        Log    "${string_val}" != "${var_01}" is False   console=yes
    END

    # comparison of boolean values

    IF    ${bool_val_1} == ${var_12}
        Log    ${bool_val_1} == ${var_12} is True   console=yes
    ELSE
        Log    ${bool_val_1} == ${var_12} is False   console=yes
    END

    IF    ${bool_val_1} == ${var_10}
        Log    ${bool_val_1} == ${var_10} is True   console=yes
    ELSE
        Log    ${bool_val_1} == ${var_10} is False   console=yes
    END

    IF    ${bool_val_2} != "true"
        Log    ${bool_val_2} != "true" is True   console=yes
    ELSE
        Log    ${bool_val_2} != "true" is False   console=yes
    END

    # comparison of None/null

    IF    ${none_val} == ${var_18}
        Log    ${none_val} == ${var_18} is True   console=yes
    ELSE
        Log    ${none_val} == ${var_18} is False   console=yes
    END

    IF    ${null_val} != "null"
        Log    ${null_val} != "null" is True   console=yes
    ELSE
        Log    ${null_val} != "null" is False   console=yes
    END


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
# 0.3.2 / 15.05.2023
#
# --------------------------------------------------------------------------------------------------------------

*** Settings ***
Resource    ./libs/testimport.resource

Suite Setup       tm.testsuite_setup    ./config/testconfig.jsonp
Suite Teardown    tm.testsuite_teardown
Test Setup        tm.testcase_setup
Test Teardown     tm.testcase_teardown

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

Test Case 03_03
    [documentation]    Working with nested dictionaries taken from json configuration file
    Log    Test '${TEST NAME}' of suite '${SUITE NAME}'    console=yes

    # log entire dictionary (scope: params/global)
    log_dict    ${dict_val}

    # log every single subkey to check the data types (notation 1)
    log_scalar    ${dict_val}[key_1][subkey_11][subsubkey_111]
    log_scalar    ${dict_val}[key_1][subkey_11][subsubkey_112]
    log_scalar    ${dict_val}[key_1][subkey_11][subsubkey_113]
    log_scalar    ${dict_val}[key_2][subkey_21][subsubkey_211]
    log_scalar    ${dict_val}[key_2][subkey_21][subsubkey_212]
    log_scalar    ${dict_val}[key_2][subkey_21][subsubkey_213]

    # log every single subkey to check the data types (notation 2)
    log_scalar    ${dict_val.key_1.subkey_11.subsubkey_111}
    log_scalar    ${dict_val.key_1.subkey_11.subsubkey_112}
    log_scalar    ${dict_val.key_1.subkey_11.subsubkey_113}
    log_scalar    ${dict_val.key_2.subkey_21.subsubkey_211}
    log_scalar    ${dict_val.key_2.subkey_21.subsubkey_212}
    log_scalar    ${dict_val.key_2.subkey_21.subsubkey_213}

    # define some variables containing names of keys
    Set Test Variable    ${key}    key_1
    Set Test Variable    ${subkey}    subkey_11
    Set Test Variable    ${subsubkey}    subsubkey_111

    # summary: access to single keys with several possible notations

    log_scalar    ${dict_val}[key_1][subkey_11][subsubkey_111]
    log_scalar    ${dict_val.key_1.subkey_11.subsubkey_111}
    log_scalar    ${dict_val['key_1']['subkey_11']['subsubkey_111']}
    log_scalar    ${dict_val}[${key}][${subkey}][${subsubkey}]
    log_scalar    ${dict_val['${key}']['${subkey}']['${subsubkey}']}


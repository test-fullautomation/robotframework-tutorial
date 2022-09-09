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
# tutorial-04.robot
#
# command line values
#
# 0.1.0 / 08.09.2022
#
# --------------------------------------------------------------------------------------------------------------

*** Settings ***
Resource    ./libs/testimport.resource

Suite Setup       testsuites.testsuite_setup    ./config/testconfig.json
Suite Teardown    testsuites.testsuite_teardown
Test Setup        testsuites.testcase_setup
Test Teardown     testsuites.testcase_teardown

*** Test Cases ***
Test Case 04_01
    [documentation]    Log of variables taken from a variable file or from single variables provided in command line
    Log    Test '${TEST NAME}' of suite '${SUITE NAME}'    console=yes

    # output of command line variables
    log_scalar    ${cmdline_var_1}
    log_scalar    ${cmdline_var_2}
    log_scalar    ${cmdline_var_3}
    log_scalar    ${cmdline_var_4}
    log_scalar    ${cmdline_var_5}
    log_scalar    ${cmdline_var_6}
    log_scalar    ${cmdline_var_7}

    # cross check: output of configuration variable
    log_scalar    ${string_val}


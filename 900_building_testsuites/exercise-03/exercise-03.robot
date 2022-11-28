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
# exercise-03.robot
#
# --------------------------------------------------------------------------------------------------------------

*** Settings ***

Library    RobotFramework_Testsuites    WITH NAME    testsuites

Suite Setup    testsuites.testsuite_setup

*** Test Cases ***
Test Case exercise-03
    [documentation]    exercise-03
    Log    teststring : ${teststring}    console=yes


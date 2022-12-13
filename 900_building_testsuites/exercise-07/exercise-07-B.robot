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
# exercise-07-B.robot
#
# --------------------------------------------------------------------------------------------------------------

*** Settings ***

# coming soon # Library    RobotFramework_TestsuitesManagement    WITH NAME    tm
Library    RobotFramework_Testsuites    WITH NAME    tm

Suite Setup    tm.testsuite_setup    ./config/exercise-07_variants.json

*** Test Cases ***
Test Case exercise-07-B
    [documentation]    exercise-07-B
    Log    teststring : ${teststring}    console=yes

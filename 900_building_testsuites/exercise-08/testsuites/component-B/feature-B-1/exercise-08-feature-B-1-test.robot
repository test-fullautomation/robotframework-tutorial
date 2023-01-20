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
# exercise-08-feature-B-1-test.robot
#
# --------------------------------------------------------------------------------------------------------------

*** Settings ***

*** Test Cases ***
Test Case exercise-08-feature-B-1-test
    [documentation]    exercise-08-feature-B-1-test
    Log    teststring_common : ${teststring_common} (exercise-08-feature-B-1-test.robot)    console=yes
    Log    teststring_variant : ${teststring_variant} (exercise-08-feature-B-1-test.robot)    console=yes
    Log    teststring_bench : ${teststring_bench} (exercise-08-feature-B-1-test.robot)    console=yes


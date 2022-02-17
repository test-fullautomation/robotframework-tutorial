#  Copyright 2020-2022 Robert Bosch Car Multimedia GmbH
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
*** Settings ***
Documentation
...    The __init__.robot file is used to define the first suite setup
...    and the last suite teardown when we trigger the robot testing 
...    for all testsuites in tutorial\900_Building_testsuites\components
Suite Setup      Initialized Suite Setup
Suite Teardown   Last Suite Teardown


*** Keywords ***
Initialized Suite Setup
    [Documentation]
    ...    This Suite Setup is executed at the begining when 
    ...    executing tutorial\900_Building_testsuites\components directory.
    ...    We can define anything we need in this setup keyword before 
    ...    executing all robot files in components directory.
    Log    "The initialized Suite setup"
    
Last Suite Teardown
    [Documentation]
    ...    This Suite Setup is executed at the end when executing
    ...    tutorial\900_Building_testsuites\components directory.
    ...    We can define anything we need in this teardown keyword after
    ...    executed all robot files in components directory. 
    Log    "Very End Suite Teardown"
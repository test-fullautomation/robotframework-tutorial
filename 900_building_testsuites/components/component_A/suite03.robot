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
Library      RobotFramework_Testsuites    WITH NAME    testsuites
Suite Setup      testsuites.testsuite_setup    ../../config/testsuites_config.json
Suite Teardown   testsuites.testsuite_teardown
Test Setup       testsuites.testcase_setup
Test Teardown    testsuites.testcase_teardown
 
*** Test Cases ***
Test Case 0301
   FOR    ${index}    IN RANGE    31    41
      Log  Hello world ${index}
   END
   
Test Case 0302
  Log    ${CONFIG}[WelcomeString]
  Log    ${CONFIG}[Project]


Test Case 0303
  Log    ${CONFIG}[version][majorversion] ${CONFIG}[version][minorversion] ${CONFIG}[version][patchversion]
    
Test Case 0304
  ${sum} =    Evaluate    ${gGlobalIntParam} + ${gGlobalIntParam}
  log   ${sum}   
    
Test Case 0305
  ${sum} =    Evaluate    ${gGlobalFloatParam} + ${gGlobalFloatParam}
  log   ${sum}  
  
Test Case 0306
  ${sum} =    Evaluate    "${gGlobalString}" + "${gGlobalString}"
  log   ${sum}

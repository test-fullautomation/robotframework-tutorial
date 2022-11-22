.. Copyright 2020-2022 Robert Bosch Car Multimedia GmbH

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

   http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.

suite05: prints some CONFIG parameters
======================================

**Data sets**

This testsuite simulates loading configuration level 3 when json config file is not set as input parameter 
of keyword testsuite_setup, then robot will find the json file which has the same name with test suite in 
``config`` directory. In this case, json file ``./config/robot_config.json`` is loaded causes there is no 
``suite05.json`` in ``config`` folder but ``robot_config.json`` exists as lower priority of configuration 
level 3.

.. code::

   *** Settings ***
   Library      RobotFramework_Testsuites    WITH NAME    testsuites
   Suite Setup      testsuites.testsuite_setup    
   Suite Teardown   testsuites.testsuite_teardown
   Test Setup       testsuites.testcase_setup
   Test Teardown    testsuites.testcase_teardown

**Robot file**

``suite05.robot`` prints parameters' value in CONFIG object which are set in json configuration file.

**Execution**

.. code::

   "%RobotPythonPath%/python.exe" -m robot -d ./logfiles -o suite05.xml -l suite05_log.html -r suite05_report.html -b suite05.log ./suite05.robot

Test Case 0501
--------------

In test case ``0501``, it just simply logs out the values of CONFIG parameters:

.. code::

   Log    ${CONFIG}[WelcomeString]
   Log    ${CONFIG}[Project]

**Outcome**

The values of parameters which are defined in ``./config/robot_config.json`` is logged out.

The information of configuration level also is printed out in log of ``Testsuite Setup``.

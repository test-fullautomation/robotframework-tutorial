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

suite04: prints some CONFIG parameters
======================================

**Data sets**

This testsuite simulates loading configuration level 3 when json config file is not set as input parameter 
of keyword testsuite_setup, then robot will find the json file which has the same name with test suite in 
``config`` directory. In this case, json file ``./config/suite04.json`` is loaded as higher priority of 
configuration level 3.

.. code::

   *** Settings ***
   Library      RobotFramework_Testsuites    WITH NAME    testsuites
   Suite Setup      testsuites.testsuite_setup    
   Suite Teardown   testsuites.testsuite_teardown
   Test Setup       testsuites.testcase_setup
   Test Teardown    testsuites.testcase_teardown

**Robot file**

``suite04.robot`` prints parameters' value in CONFIG object which are set in json configuration file.

**Execution**

.. code::

   "%RobotPythonPath%/python.exe" -m robot -d ./logfiles -o suite04.xml -l suite04_log.html -r suite04_report.html -b suite04.log ./suite04.robot

Test Case 0401
--------------

In test case ``0401``, it just simply logs out the values of CONFIG parameters:

.. code::

   Log    ${CONFIG}[WelcomeString]
   Log    ${CONFIG}[Project]

**Outcome**

The values of parameters which are defined in ``./config/suite04.json`` is logged out.

The information of configuration level also is printed out in log of ``Testsuite Setup``.

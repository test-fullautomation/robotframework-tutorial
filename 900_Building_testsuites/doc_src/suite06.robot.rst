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

suite06: prints some CONFIG parameters
======================================

**Data sets**

This testsuite simulates loading configuration level 4 when json config file is not set as input parameter 
of keyword testsuite_setup, and there is no json files ``suite06.json`` and ``robot_config.json`` in ``./config`` 
then robot will run with configuration level 4. In level 4, the default json configuration file is loaded. 
The default configuration file is located at ``<RobotFramework installation folder>\python39\lib\site-packages\RobotFramework_Testsuites\Config\robot_config.json``.

.. code::

   *** Settings ***
   Library      RobotFramework_Testsuites    WITH NAME    testsuites
   Suite Setup      testsuites.testsuite_setup    
   Suite Teardown   testsuites.testsuite_teardown
   Test Setup       testsuites.testcase_setup
   Test Teardown    testsuites.testcase_teardown

**Robot file**

``suite06.robot`` prints parameters' value in CONFIG object which are set in json configuration file.

**Execution**

.. code::

   "%RobotPythonPath%/python.exe" -m robot -d ./logfiles -o suite06.xml -l suite06_log.html -r suite06_report.html -b suite06.log ./suite06.robot

Test Case 0601
--------------

In test case ``0601``, it just simply logs out the values of CONFIG parameters:

.. code::

   Log    ${CONFIG}[WelcomeString]
   Log    ${CONFIG}[Project]

**Outcome**

The values of parameters which are defined in ``<RobotFramework installation folder>\python39\lib\site-packages\RobotFramework_Testsuites\Config\robot_config.json`` is logged out.

The information of configuration level also is printed out in log of ``Testsuite Setup``.

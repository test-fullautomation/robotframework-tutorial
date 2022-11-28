.. Copyright 2020-2022 Robert Bosch Car Multimedia GmbH

.. Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

.. http://www.apache.org/licenses/LICENSE-2.0

.. Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.

suite01: prints some CONFIG parameters
======================================

**Data sets**

The CONFIG and the global parameters will be loaded in

.. code::

   ../config/testsuites_config.json

according to the variant name, the robot run will choose the corresponding json configuration 
file. If variant name is not set, the robot will run with ``../config/robot_execution_config.json`` config file.

**Robot file**

``suite01.robot`` prints parameters' value in CONFIG object which are set in json configuration file.

**Execution**

.. code::

   "%RobotPythonPath%/python.exe" -m robot -d ./logfiles -o suite01.xml -l suite01_log.html -r suite01_report.html -b suite01.log ./suite01.robot

Test Case 0101
--------------

In test case ``0101``, it just simply logs out the values of CONFIG parameters:

.. code::

   Log    ${CONFIG}[WelcomeString]
   Log    ${CONFIG}[Project]

**Outcome**

The values of parameters which are defined in ``../config/common/test_config_common.json`` is logged out.

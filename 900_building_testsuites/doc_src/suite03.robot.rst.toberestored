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

suite03: Do some basic tests with global parameters
===================================================

**Data sets**

The CONFIG and the global parameters will be loaded in

.. code::

   ../config/testsuites_config.json

according to the variant name, the robot run will choose the corresponding json configuration 
file. If variant name is not set, the robot will run with ``../config/robot_execution_config.json`` config file.

**Robot file**

``suite03.robot`` do some basic testings with global variable which are set in json configuration file.

**Execution**

.. code::

   "%RobotPythonPath%/python.exe" -m robot -d ./logfiles -o suite03.xml -l suite03_log.html -r suite03_report.html -b suite03.log ./suite03.robot

Test Case 0301
--------------

In test case ``0301`` implement a simple ``FOR`` loop and log out string ``Hello world <loop_index>``:

.. code::

   FOR    ${index}    IN RANGE    31    41
      Log  Hello world ${index}
   END

**Outcome**

The string ``Hello world <loop_index>`` is logged out.

Test Case 0302
--------------

In test case ``0302`` just simply logs out the values of CONFIG parameters:

.. code::

   Log    ${CONFIG}[WelcomeString]
   Log    ${CONFIG}[Project]

**Outcome**

The values of parameters which are defined in ``../config/common/test_config_common.json`` is logged out.

Test Case 0303
--------------

In test case ``0303`` prints out the version of Testsuitesmanagement package which is stored in CONFIG object:

.. code::

   Log    ${CONFIG}[version][majorversion] ${CONFIG}[version][minorversion] ${CONFIG}[version][patchversion]

**Outcome**

The values of ``version.majorversion``, ``version.minorversion``, and ``version.patchversion`` are logged out 
alternately.

Test Case 0304
--------------

In test case ``0304`` sums two ``int`` datatype global variables which are defined in json configuration file, and print 
the result out:

.. code::

   ${sum} =    Evaluate    ${gGlobalIntParam} + ${gGlobalIntParam}
   log   ${sum}

**Outcome**

The result of sum operation between two global variables are printed out.

Test Case 0305
--------------

In test case ``0305`` sums two float datatype global variables which are defined in json configuration file, and print 
the result out:

.. code::

   ${sum} =    Evaluate    ${gGlobalFloatParam} + ${gGlobalFloatParam}
   log   ${sum}

**Outcome**

The result of sum operation between two global variables are printed out.

Test Case 0306
--------------

In test case ``0306`` sums two str datatype global variables which are defined in json configuration file, and print 
the result out:

.. code::

   ${sum} =    Evaluate    "${gGlobalString}" + "${gGlobalString}"
   log   ${sum}

**Outcome**

The result of sum operation between two global variables are printed out.
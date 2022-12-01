.. Copyright 2020-2022 Robert Bosch GmbH

.. Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

.. http://www.apache.org/licenses/LICENSE-2.0

.. Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.

exercise-01
===========

----

Content
-------

The first exercise contains the simplest realization of a test suites management.
*But this is only to demonstrate some basics! This implementation is not recommended!*

``exercise-01.robot`` imports the required library

.. code::

   Library    RobotFramework_TestsuitesManagement    WITH NAME    testsuites

and executes the ``testsuite_setup``

.. code::

   Suite Setup    testsuites.testsuite_setup

No further configuration file is given.

----

Command line
------------

.. code::

   "%RobotPythonPath%/python.exe" -m robot -d ./logfiles -o exercise-01.xml -l exercise-01_log.html -r exercise-01_report.html -b exercise-01.log "./exercise-01.robot"

----

Outcome
-------

Because of nothing more is specified the RobotFramework AIO falls back to the default configuration (level 4).

The test prints the ``Maximum_version`` and the ``Project`` name like defined in this default configuration.

Hint: The parameters are keys of an internal configuration dictionary. They have to be accessed in the following way:

.. code::

   Log    Maximum_version : ${CONFIG}[Maximum_version]    console=yes
   Log    Project : ${CONFIG}[Project]    console=yes

The logfile tells about the origin of the values:

.. code::

   Running with configuration level: 4
   CfgFile Path: <Robot Framework installation>\python39\lib\site-packages\RobotFramework_TestsuitesManagement\Config\robot_config.json

Hint: The *level 4* configuration is a fallback solution and should be avoided. In case you activate the **RobotFramework_TestsuitesManagement**,
you should also specify an own configuration file. This is handled in the following exercises.


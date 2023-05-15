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

exercise-03
===========

----

Content
-------

``exercise-03`` demonstrates several ways to load the configuration from a ``config`` folder.

This ``config`` folder has to be placed in the same folder than the test suites.

Parameter configuration files within this folder are considered under two different conditions:

* The configuration file has the name ``robot_config.jsonp``. That is a fix name predefined by the **RobotFramework_TestsuitesManagement**.
* The configuration file has the same name than a robot file inside the test suites folder, e.g.:

  * Name of test suite file: ``exercise-03-A.robot``
  * Path and name of corresponding parameter configuration file: ``./config/exercise-03-A.jsonp``

  With this rule it is possible to give every test suite in a certain folder an own individual configuration.

This exercise contains the following test suites:

* ``exercise-03.robot``
* ``exercise-03-A.robot``
* ``exercise-03-B.robot``

together with the following parameter configuration files:

* ``config/robot_config.jsonp``
* ``config/exercise-03-A.jsonp``
* ``config/exercise-03-B.jsonp``

Every of these configuration files define a test string containing an individual value, e.g. the file ``exercise-03-A.jsonp``
defines:

.. code::

   "teststring" : "I am the 'exercise-03-A' configuration of exercise 03"

With the following command lines we execute all test suites (without any configuration related command line extension).

Also the test suites itself do not contain any configuration information.

----

Command lines
-------------

.. code::

   "%RobotPythonPath%/python.exe" -m robot -d ./logfiles -o exercise-03.xml -l exercise-03_log.html -r exercise-03_report.html -b exercise-03.log "./exercise-03.robot"
   "%RobotPythonPath%/python.exe" -m robot -d ./logfiles -o exercise-03.xml -l exercise-03_log.html -r exercise-03_report.html -b exercise-03.log "./exercise-03-A.robot"
   "%RobotPythonPath%/python.exe" -m robot -d ./logfiles -o exercise-03.xml -l exercise-03_log.html -r exercise-03_report.html -b exercise-03.log "./exercise-03-B.robot"

----

Outcome
-------

The test suites ``exercise-03-A.robot`` and ``exercise-03-B.robot`` have the configuration counterparts (same file names) ``config/exercise-03-A.jsonp``
and ``config/exercise-03-B.jsonp``.

Therefore the value of the test string is taken out of these configuration files.

The test suite ``exercise-03.robot`` does not have a configuration counterpart. Therefore the Robot Framework AIO falls back to the configuration file with the
default name ``config/robot_config.jsonp`` and the value of the test string is:

.. code::

   I am the 'robot_config' configuration of exercise 03

The log file gives more information about the origin; in case of ``exercise-03.robot``:

.. code::

   Running with configuration level: 3
   CfgFile Path: config/robot_config.jsonp


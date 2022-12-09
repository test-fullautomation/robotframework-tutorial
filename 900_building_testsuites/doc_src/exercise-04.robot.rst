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

exercise-04
===========

----

Content
-------

In this exercise we introduce some extensions of features already known from the previous exercises.

We have a bunch of robot files, placed in several subfolders at several levels in the file system:

.. code::

   ./testsuites/exercise-04.robot
   ./testsuites/001/exercise-04-001.robot
   ./testsuites/001/001-01/exercise-04-001-01.robot
   ./testsuites/001/001-01/001-01-01/exercise-04-001-01-01.robot
   ./testsuites/002/exercise-04-002.robot

Every robot file logs the test string. Every robot file requires a variant handling, but we do not want to have the need to maintain the import code

.. code::

   Library    RobotFramework_TestsuitesManagement    WITH NAME    tm
   Suite Setup    tm.testsuite_setup    ../config/exercise-04_variants.json

in every of these files separately.

Therefore we use a feature of the Robot Framework and put this code into a file with name ``__init__.robot`` and we place this file 
at the top level of the test suites folder:

.. code::

   ./testsuites/__init__.robot

Definitions within this file will become valid for all tests inside the test suite. And the robot files do not need this code any more.

Our configuration files we still place inside a config folder:

.. code::
   
   ./config/exercise-04_config_default.json
   ./config/exercise-04_config_variant1.json
   ./config/exercise-04_config_variant2.json
   ./config/exercise-04_variants.json

Because of the robot files are placed at different levels within the file system, the variants configuration file ``exercise-04_variants.json``
requires the *three dots* syntax:

.. code::

   "name": "exercise-04_config_default.json",
   "path": ".../config/"

Within the exercise folder execute the following command line:

----

Command line
------------

.. code::

   "%RobotPythonPath%/python.exe" -m robot -d ./logfiles -o exercise-04.xml -l exercise-04_log.html -r exercise-04_report.html -b exercise-04.log "./testsuites"

----

Outcome
-------

The test string of all executed robot files will have the same content:

.. code::

   I am the 'default' variant configuration of exercise 04

The ``default`` variant is choosen because of the command line does not contain any variant specification.

In case you want to run all tests under the condition of a certain variant, you have to define this variant in the command line, e.g. ``variant2``:

----

Command line
------------

.. code::

   "%RobotPythonPath%/python.exe" -m robot -d ./logfiles -o exercise-04.xml -l exercise-04_log.html -r exercise-04_report.html -b exercise-04.log --variable variant:"variant2" "./testsuites"

----

Outcome
-------

The test string of all executed robot files now has the content:

.. code::

   I am the 'variant2' configuration of exercise 04

The log file gives more information about the origin:

.. code::

   Running with configuration level: 2
   CfgFile Path: ../config/exercise-04_config_variant2.json

Hint: Add robot files or rearrange the position of the available robot files and repeat the command lines. You will see that - without any path adaptions - all
robot files still run with the same configuration.




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

Building test suites in RobotFramework AIO
==========================================

----

Table of content
----------------

1. `Introduction`_

* `What is the initial situation?`_

* `How to handle configuration parameters in RobotFramework AIO?`_

* `How to realize a concrete test suites management?`_

* `How does the content of a configuration files in JSON format look like?`_

* `How does the RobotFramework AIO access configuration files?`_

* `How to enable the test suites management in RobotFramework AIO?`_

2. `Exercises`_


Introduction
------------

What is the initial situation?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In the scope of the RobotFramework AIO a test suite is either a single robot file containing one or more test cases, or a set of several robot files.

Usually all test cases of a test suite run under the same conditions - but these conditions may be different. For example the same test case is used
to test several different variants of a *System under Test*. Every variant requires individual values for certain configuration parameters.

Based on this consideration two different scenarios are thinkable:

1. A simple one

   Project *P* requires software for a target. There is only one variant *V* developed for this target.
   Tests developed for testing the target software, are carried out at several test benches.
   All test benches have the same hardware configuration.

   *Therefore all tests run at every time under the same conditions.*

2. A complicated one

   Project *P* requires software for a target. There are several variants *V1-Vx* developed for this target.
   Tests developed for testing the target software on several variants, are carried out at several test benches.
   All test benches have different hardware configurations.
   All variants and all test benches require individual values for configuration parameters used in the tests.

   *Therefore the same tests have to run under different conditions.*

We assume here that in most of the cases the world isn't so much easy like described in scenario 1. Therefore in this tutorial we concentrate on scenario 2.

TOC_

----

How to handle configuration parameters in RobotFramework AIO?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The RobotFramework AIO provides several places to define parameters: robot files, resource files, parameter files. But these parameters
are fixed - and therefore sufficient for the simple scenario 1 only.

For the complicated scenario 2 we need a more dynamic way of accessing parameters. And we postulate the following: When switching between
tests of several variants and test executions on several test benches, no changes shall be required within the test code.

The outcome is that another position has to be introduced to store values for variant and test bench specific parameters.
And a possibility has to be provided to dynamically make either the one or the other set of values vailable during the execution of tests - depending on
outer circumstances like "*which variant?*" and "*which test bench?*".

The RobotFramework AIO contains two components - the **RobotFramework_Testsuites** and the **JsonPreprocessor** - that allow the user
to define dynamic configuration values within separate configuration files in JSON format. The content of these files will be available
during the test execution.

In this set the **JsonPreprocessor** is responsible for reading in the values. This includes basic aspects like syntax checks and required data type
conversions (between JSON format and robot format).

The **RobotFramework_Testsuites** is responsible for making the values available during test execution - but under certain conditions that can be defined
by the user (e.g. to realize a variant handling). This means: Not all parameter values are available during test execution - only the ones that belong to
the current test scenario.

To realize this, the **RobotFramework_Testsuites** together with the **JsonPreprocessor** enables the user to do the following things:

* Split all possible configuration values into several JSON configuration files, with every configuration file contains a specific set of values
  for configuration parameter
* Use nested imports of JSON configuration files
* Follow up definitions in configuration files overwrite previous definitions (of the same parameter)
* Select between several criteria to let the RobotFramework AIO use a certain JSON configuration file

The RobotFramework AIO supports two different kinds of JSON configuration files:

* Configuration files containing the parameter definitions
* A certain single configuration file containing the mapping between the configuration files with parameter definitions and a name
  (usually the name of a variant). This name can be used in command line to select a certain configuration file containing the values
  for this variant.

More details about the structure of JSON files can be found in section `How does the content of a configuration files in JSON format look like?`_.

More informations about the **RobotFramework_Testsuites** and the **JsonPreprocessor** can be found here:

* `RobotFramework_Testsuites in PyPi <https://pypi.org/project/robotframework-testsuitesmanagement>`_
* `RobotFramework_Testsuites in GitHub <https://github.com/test-fullautomation/robotframework-testsuitesmanagement>`_
* `RobotFramework_Testsuites documentation <https://github.com/test-fullautomation/robotframework-testsuitesmanagement/blob/develop/RobotFramework_Testsuites/RobotFramework_Testsuites.pdf>`_
* `JsonPreprocessor in PyPi <https://pypi.org/project/JsonPreprocessor>`_
* `JsonPreprocessor in GitHub <https://github.com/test-fullautomation/python-jsonpreprocessor>`_
* `JsonPreprocessor documentation <https://github.com/test-fullautomation/python-jsonpreprocessor/blob/develop/JsonPreprocessor/JsonPreprocessor.pdf>`_

TOC_

----

How to realize a concrete test suites management?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In this section it is described in theory which steps have to be followed to realize a concrete test suites management.
The example we use here, is also the main topic of the test suites in this tutorial. Details about the internal structure of 
configuration files will be given in the next part of this introduction.

*Step 1: Analyze the current situation in your project*

An outcome of the analysis can be something like that:

* Three variants need to be tested (*V1-V3*)
* Two test benches are available (*B1-B2*)
* Three configuration parameter are needed (*P1-P3*)

Additionally we assume that all variants can be tested on all test benches, but the parameters need to be separated:

* *P1* has the same value in all variants and at all test benches
* *P2* is variant specific; *P2V1* != *P2V2* != *P2V3*
* *P3* is test bench specific; *P3B1* != *P3B2*

*Step 2: Implement the mapping configuration file for variant switching*

For every variant (*V1-V3*) make an entry referring to the configuration file in which the concrete values
for this variant are defined.

*Step 3: Define values for the identified parameters*

For every variant (*V1-V3*) introduce an individual configuration file containing the values for this variant.

*Step 4: Define values for all remaining parameters that are not specific for any variant or test bench*

How this does look like concretely is described in the next section.

TOC_

----

How does the content of a configuration files in JSON format look like?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In this part of the introduction we take a first look at the content of configuration files.

1. Configuration file defining the mapping between variant names and where to find the corresponding parameter values

   This file configures the access to all variant dependent ``robot_config*.json`` files.

   .. code:: python

      {
        "default": {
                     "name": "robot_execution_config.json",
                     "path": ".../config/"
                   },
        "variant_1": {
                       "name": "robot_config_variant_1.json",
                       "path": ".../config/"
                     },
        "variant_2": {
                       "name": "robot_config_variant_2.json",
                       "path": ".../config/"
                     },
        "variant_3": {
                       "name": "robot_config_variant_3.json",
                       "path": ".../config/"
                     }
      }

   The example above contains definitions for three variants with name ``variant_1``, ``variant_2`` and ``variant_3``.

   Additionally a variant named ``default`` is defined. This default configuration becomes active in case of no certain variant name is provided
   when the test suite is being executed.

   Another aspect is important: the *three dots*.
   The path to the ``robot_config*.json`` files depends on the test file location. A 
   different number of ``../`` is required dependent on the directory depth of the test 
   case location.

   Therefore we use here three dots to tell the Robot Framework AIO to search from the test 
   file location up till the ``robot_config*.json`` files are found:

   .. code:: python

      ./config/robot_config.json
      ../config/robot_config.json
      ../../config/robot_config.json
      ../../../config/robot_config.json

   and so on.

2. Configuration file defining all parameters that shall be available globally during test execution.

   Some of them are required. Optionally the user can add own ones. The following example shows the smallest version 
   of a configuration file containing only the required parameters. This version is a default version and part of the
   RobotFramework AIO installation.

   .. code:: python

      {
        "WelcomeString"   : "Hello... RobotFramework AIO is running now!",
        "Maximum_version" : "0.5.2",
        "Minimum_version" : "0.5.2",
        "Project"         : "RobotFramework AIO tutorial",
        "TargetName"      : "device"
      }

   ``Project``, ``WelcomeString`` and ``TargetName`` are simple strings that can be used anyhow. ``Maximum_version`` and ``Minimum_version``
   are part of a version control mechanism: In case of the version of the currently installed RobotFramework AIO is outside the range between
   ``Minimum_version`` and ``Maximum_version``, the test execution stops with an error message.

   The following example is an extended version of a configuration file containing also some user defined parameters.

   .. code:: python

      {
        "WelcomeString"   : "Hello... RobotFramework AIO is running now!",
        "Maximum_version" : "0.5.2",
        "Minimum_version" : "0.5.2",
        "Project"         : "RobotFramework AIO tutorial",
        "TargetName"      : "device",
        "params": {
                    // global parameters
                    "global" : {
                                 "param1" : "ABC",
                                 "param2" : 25
                               }
                  },
        "preprocessor": {
                          // feature switches
                          "definitions" : {
                                            "switch1" : true,
                                            "switch2" : false
                                          }
                        }
      }

   The user defined parameters are separated into **global parameters** and **preprocessor definitions**.

   *TODO: Explain differences; clarify implementation status.*

   And another feature can be seen in the example above: In the context of the RobotFramework AIO the JSON format is an extended one.
   Deviating from JSON standard it is possible to comment out lines with starting them with a double slash "``//``". This allows to
   add explanations about the meaning of the defined parameters already within the JSON file.

   Further JSON syntax extensions will be explained in the corresponding exercises.

TOC_

----

How does the RobotFramework AIO access configuration files?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Every test execution requires a configuration - that is the accessibility of a configuration file in JSON format. The RobotFramework AIO provides
four different possibilities - also called *level* - to realize such an access. These possibilities are sorted and the RobotFramework AIO tries to
access the configuration file in a certain order: Level 1 has the highest priority and level 4 has the lowest priority.

* Level 1

  Path and name of the configuration file is provided in command line of the RobotFramework AIO.

* Level 2

  The name of the variant is provided in command line of the RobotFramework AIO. This requires an additional configuration file
  that contains the mapping between the variant and the variant specific configuration
  (like described in `How does the content of a configuration files in JSON format look like?`_).

  This also requires that this mapping file is known to the test (path and name is an input parameter of the ``Suite Setup``).

  This is handled in exercise (**TODO: add name**).

* Level 3

  The RobotFramework AIO searches for configuration files within a folder ``config/`` in current test suite directory.
  In case of such a folder exists and configuration files are inside, they will be used.

  This is handled in exercise (**TODO: add name**).

* Level 4

  The RobotFramework AIO uses the default configuration file that is part of the installation.

  This is handled in ``exercise-01``.

*Summarized*:

* With highest priority a configuration file provided in command line, is considered - even in case of also other configuration files (level 2 - level 4)
  are available.

* If a configuration file is not provided in command line, but a variant name, then the configuration belonging to this variant, is loaded - even
  in case of also other configuration files (level 3 - level 4) are available.

* If nothing is specified in command line, then the RobotFramework AIO tries to find configuration files within a ``config/`` folder and take them if
  available - even in case of also the level 4 configuration file is available.

* In case of the user does not provide any information about configuration files to use, the RobotFramework AIO loads the default configuration
  from installation folder (fallback solution; level 4).

TOC_

----

How to enable the test suites management in RobotFramework AIO?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To enable the test suites management you have to import the **RobotFramework_Testsuites** library in the following way:

.. code::

   Library    RobotFramework_Testsuites    WITH NAME    testsuites

We recommend to use the ``WITH NAME`` option to shorten the robot code a little bit.

The next step is to call the ``testsuite_setup`` of the **RobotFramework_Testsuites** within the ``Suite Setup`` of your test:

.. code::

   Suite Setup    testsuites.testsuite_setup

As long as you

* do not provide a configuration file in command line when executing the test suite (level 1),
* do not provide a configuration files as parameter of the ``testsuite_setup`` (level 2),
* do not have a ``config`` folder containing configuration files in your test suites folder (level 3),

the **RobotFramework_Testsuites** falls back to the default configuration (level 4).

In case you want to realize a variant handling you have to provide the path and the name of a variant configuration file to the ``testsuite_setup``:

   .. code::

      Suite Setup    testsuites.testsuite_setup    ./config/exercise_variants.json

To ease the analysis of a test execution, the log file contains informations about the selected level and the path and the name of the used
configuration file, for example:

   .. code::

      Running with configuration level: 2
      CfgFile Path: ./config/exercise_config.json

Please consider: The ``testsuite_setup`` requires the mapping configuration file (containing the mapping between the variant names and the
corresponding parameter configuration files; in the example above: ``exercise_variants.json``) - whereas the log file contains the resulting
parameter configuration file (in the example above: ``exercise_config.json``), that is selected depending on the name of the variant provided
in command line of the RobotFramework AIO.

**For now it's enough theory - time for exercises.**

All further formats and features that need to be explained, will be explained in those test suites who use them.

The following part of this document contains an overview about all exercises available in this tutorial.

TOC_

----

Exercises
---------

Every exercise is placed in an own exercise folder (``exercise-01`` - ``exercise-x``) that is stand-alone.
Every exercise folder contains one or more robot files together with all additionally required files
and together with the documentation of the exercise.

We recommend to exexute every robot file in command line. This is because of in lots of cases command line parameters are required
when the tests are executed. Corresponding informations you will find in the documentation inside the exercise folder.

Every exercise folder will have it's own log files folder with the log files having the same name like the executed robot files:

* Test: exercise-x.robot
* Log: logfiles/exercise-x.log

exercise-01
~~~~~~~~~~~

Simple example referring to the default configuration



----


to be continued


TOC_

----

*Tutorial v. 0.3.0 / 25.11.2022 / by MS/EMC1-XC Mai Dinh Nam Son and XC-CT/ECA3-Queckenstedt*

.. _TOC: `Table of content`_


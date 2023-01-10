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

Building test suites in Robot Framework
=======================================

----

Table of content
----------------

1. `Introduction`_

* `What is the initial situation?`_

* `How to handle configuration parameters in Robot Framework?`_

* `How to realize a concrete test suites management?`_

* `How does the content of configuration files in JSON format look like?`_

* `How does the Robot Framework access configuration files?`_

* `How to activate the test suites management in Robot Framework?`_

2. `Exercises`_


Introduction
------------

What is the initial situation?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In the scope of the Robot Framework a test suite is either a single robot file containing one or more test cases, or a set of several robot files.

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

How to handle configuration parameters in Robot Framework?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The Robot Framework provides several places to define parameters: robot files, resource files, parameter files. But these parameters
are fixed - and therefore sufficient for the simple scenario 1 only.

For the complicated scenario 2 we need a more dynamic way of accessing parameters. And we postulate the following: When switching between
tests of several variants and test executions on several test benches, no changes shall be required within the test code.

The outcome is that another position has to be introduced to store values for variant and test bench specific parameters.
And a possibility has to be provided to dynamically make either the one or the other set of values vailable during the execution of
tests - depending on outer circumstances like "*which variant?*" and "*which test bench?*".

For the Robot Framework a component called **RobotFramework_TestsuitesManagement** is available, that allows users to define
dynamic configuration values within separate configuration files in JSON format. The content of these files will be available
during the test execution.

More detailled information about this component and about how to install you can find here:

* `RobotFramework_TestsuitesManagement in PyPi <https://pypi.org/project/robotframework-testsuitesmanagement>`_
* `RobotFramework_TestsuitesManagement in GitHub <https://github.com/test-fullautomation/robotframework-testsuitesmanagement>`_
* `RobotFramework_TestsuitesManagement documentation <https://github.com/test-fullautomation/robotframework-testsuitesmanagement/blob/develop/RobotFramework_TestsuitesManagement/RobotFramework_TestsuitesManagement.pdf>`_

In this tutorial we concentrate on how to use this component.

The **RobotFramework_TestsuitesManagement** is responsible for making the configuration values available during test execution - but under
certain conditions that can be defined by the user (e.g. to realize a variant handling). This means: Not all parameter values are available
during test execution - only the ones that belong to the current test scenario.

To realize this, the following features are available:

* Split all possible configuration values into several JSON configuration files, with every configuration file contains a specific set of values
  for configuration parameter
* Use nested imports of JSON configuration files
* Follow up definitions in configuration files overwrite previous definitions (of the same parameter)
* Select between several criteria to let the Robot Framework use a certain JSON configuration file

The **RobotFramework_TestsuitesManagement** supports two different kinds of JSON configuration files:

* *parameter configuration files*

  These configuration files contain all parameter definitions (can be more than one configuration file in a project)

* *variant configuration file*

  This is a single configuration file containing the mapping between the several parameter configuration files and a name
  (usually the name of a variant). This name can be used in command line to select a certain parameter configuration file
  containing the values for this variant.

  It's easier simply to use a name for referencing a certain variant instead of having the need always to mention the path and name
  of a configuration file.

More details about the structure of JSON files can be found in section `How does the content of configuration files in JSON format look like?`_.

TOC_

----

How to realize a concrete test suites management?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In this section it is described *in theory* which steps have to be followed to realize a concrete test suites management.
Details about the internal structure of configuration files are given in the next part of this introduction.

*Step 1: Analyze the current situation in your project*

An outcome of the analysis can be something like that:

* Three variants need to be tested (*V1-V3*)
* Two test benches are available (*B1-B2*)
* Three configuration parameter are needed (*P1-P3*)

Additionally we assume that all variants can be tested on all test benches, but the parameters need to be separated:

* *P1* has the same value in all variants and at all test benches
* *P2* is variant specific; *P2V1* != *P2V2* != *P2V3*
* *P3* is test bench specific; *P3B1* != *P3B2*

*Step 2: Implement the variant configuration file*

For every variant (*V1-V3*) make an entry referring to the corresponding parameter configuration file in which the concrete values
for this variant are defined.

*Step 3: Define values for all identified parameters*

For every variant (*V1-V3*) introduce a parameter configuration file containing the values for this variant.

*Step 4: Define values for all remaining parameters that are not specific for any variant or test bench*

Use a common parameter configuration files for this purpose (more details in ``exercise-05``).

How this does look like concretely is described in the next section.

TOC_

----

How does the content of configuration files in JSON format look like?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In this part of the introduction we take a first look at the content of configuration files.

1. *variant configuration file*

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

   Therefore we use here three dots to tell the **RobotFramework_TestsuitesManagement** to search from the test 
   file location up till the ``robot_config*.json`` files are found:

   .. code:: python

      ./config/robot_config.json
      ../config/robot_config.json
      ../../config/robot_config.json
      ../../../config/robot_config.json

   and so on.

   Hint: The paths to the ``robot_config*.json`` files are relative to the position of the test suite - **and not relative to the position of the
   mapping file in which they are defined!** You are free to move your test suites one or more level up or down in the file system, but using the
   *three dots* notation enables you to let the position of the ``config`` folder unchanged.

   It is of course still possible to use the standard notation for relative paths:

   .. code:: python

      "path": "./config/"


2. *parameter configuration files*

   In these configuration files all parameters are defined, that shall be available globally during test execution.

   Some parameters are required. Optionally the user can add own ones. The following example shows the smallest version 
   of a parameter configuration file containing only the most important parameters. This version is a default version and part of the
   **RobotFramework_TestsuitesManagement** installation.

   .. code:: python

      {
        "WelcomeString"   : "Hello... Robot Framework is running now!",
        "Maximum_version" : "1.0.0",
        "Minimum_version" : "0.6.0",
        "Project"         : "RobotFramework Testsuites",
        "TargetName"      : "Device_01"
      }

   ``Project``, ``WelcomeString`` and ``TargetName`` are simple strings that can be used anyhow. ``Maximum_version`` and ``Minimum_version``
   are part of a version control mechanism: In case of the version of the currently installed Robot Framework is outside the range between
   ``Minimum_version`` and ``Maximum_version``, the test execution stops with an error message.

   The version control mechanism is optional. In case you do not need to have your tests under version control, you can set 
   the versions to the value ``null``.

   .. code:: python

      "Maximum_version" : null,
      "Minimum_version" : null,

   As an alternative it is also possible to remove ``Minimum_version`` and ``Maximum_version`` completely.

   In case you define only one single version number, only this version number is considered. The following combination
   makes sure, that the installed Robot Framework at least is of version 0.6.0, but there is no upper version limit:
 
   .. code:: python

      "Maximum_version" : null,
      "Minimum_version" : "0.6.0",

   The following example is an extended version of a configuration file containing also some user defined parameters.

   .. code:: python

      {
        "WelcomeString"   : "Hello... Robot Framework is running now!",
        "Maximum_version" : "1.0.0",
        "Minimum_version" : "0.6.0",
        "Project"         : "RobotFramework Testsuites",
        "TargetName"      : "Device_01"
        "params": {
                    // global parameters
                    "global" : {
                                 "param1" : "ABC",
                                 "param2" : 25
                               }
                  }
      }

   User defined parameters have to be placed inside ``params:global``. The intermediate level ``global`` is introduced to enable further
   parameter scopes than ``global`` in future.

   And another feature can be seen in the example above: In the context of the **RobotFramework_TestsuitesManagement** the JSON format is an extended one.
   Deviating from JSON standard it is possible to comment out lines with starting them with a double slash "``//``". This allows to
   add explanations about the meaning of the defined parameters already within the JSON file.

   Further JSON syntax extensions - introduced by the **RobotFramework_TestsuitesManagement** - will be explained in the corresponding exercises.

TOC_

----

How does the Robot Framework access configuration files?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

With an installed **RobotFramework_TestsuitesManagement** every test execution requires a configuration - that is the accessibility
of a configuration file in JSON format. The **RobotFramework_TestsuitesManagement** provides four different possibilities - also
called *level* - to realize such an access. These possibilities are sorted and the **RobotFramework_TestsuitesManagement** tries
to access the configuration file in a certain order: Level 1 has the highest priority and level 4 has the lowest priority.

* Level 1

  Path and name of a parameter configuration file is provided in command line of the Robot Framework.

  This is handled in ``exercise-02``.

* Level 2 (**recommended**)

  The name of the variant is provided in command line of the Robot Framework.

  This level requires that a variant configuration file is passed to the suite setup of the **RobotFramework_TestsuitesManagement**
  (like described in `How does the content of configuration files in JSON format look like?`_).

  This is handled in ``exercise-02``.

* Level 3

  The **RobotFramework_TestsuitesManagement** searches for parameter configuration files within a folder ``config``
  in current test suite folder.
  In case of such a folder exists and parameter configuration files are inside, they will be used.

  This is handled in ``exercise-03``.

* Level 4 (**unwanted, fallback solution only**)

  The **RobotFramework_TestsuitesManagement** uses the default configuration file that is part of the installation.

  This is handled in ``exercise-01``.

**Summary**

* With highest priority a parameter configuration file provided in command line, is considered - even in case of also other configuration files (level 2 - level 4)
  are available.

* If a parameter configuration file is not provided in command line, but a variant name, then the configuration belonging to this variant, is loaded - even
  in case of also other configuration files (level 3 - level 4) are available.

* If nothing is specified in command line, then the **RobotFramework_TestsuitesManagement** tries to find parameter configuration files within a ``config``
  folder and take them if available - even in case of also the level 4 configuration file is available.

* In case of the user does not provide any information about parameter configuration files to use, the **RobotFramework_TestsuitesManagement** loads the default
  configuration from installation folder (fallback solution; level 4).

**In this context two aspects are important to know for users:**

1. *Which parameter configuration file is selected for the test execution?*

   To answer this question the log file contains the path and the name of the selected parameter configuration file.

2. *For which reason is this parameter configuration file selected?*

   To answer this question the log file also contains the level number. The level number indicates the reason.

With these log file entries the test execution is clearly understandable, traceable and scales for huge test suites.

**Why is level 2 the recommended one?**

Level 2 is the most flexible and extensible solution. Because the robot files contain a link to a variants configuration file,
the possible sets of parameter values can already be taken out of the code.

The values selected by level 1, you only see in the log files, but not in the code, because the selection happens in command line only.

Level 3 has a rather strong binding between robot files and configuration files. If you start the test implementation based on level 3
and after this want to have a variant handling, then you have to switch from level 3 to level 2 - and this causes effort in implementation.

Wherease if you start with level 2 immediately and need to consider another set of configuration values for the same tests, then you only have to add
another parameter configuration file and another entry in the variants configuration file, without changing any test implementation.

**We strongly recommend not to mix up several different configuration levels in one project!**

TOC_

----

How to activate the test suites management in Robot Framework?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To activate the test suites management you have to import the **RobotFramework_TestsuitesManagement** library in the following way:

.. code::

   Library    RobotFramework_TestsuitesManagement    WITH NAME    tm

We recommend to use the ``WITH NAME`` option to shorten the robot code a little bit.

The next step is to call the ``testsuite_setup`` of the **RobotFramework_TestsuitesManagement** within the ``Suite Setup`` of your test:

.. code::

   Suite Setup    tm.testsuite_setup

As long as you

* do not provide a parameter configuration file in command line when executing the test suite (level 1),
* do not provide a variants configuration file as parameter of the ``testsuite_setup`` (level 2),
* do not have a ``config`` folder containing parameter configuration files in your test suites folder (level 3),

the **RobotFramework_TestsuitesManagement** falls back to the default configuration (level 4).

In case you want to realize a variant handling you have to provide the path and the name of a variants configuration file to the ``testsuite_setup``:

.. code::

   Suite Setup    tm.testsuite_setup    ./config/exercise_variants.json

To ease the analysis of a test execution, the log file contains informations about the selected level and the path and the name of the used
configuration file, for example:

.. code::

   Running with configuration level: 2
   CfgFile Path: ./config/exercise_config.json

Please consider: The ``testsuite_setup`` requires a variants configuration file (in the example above: ``exercise_variants.json``) - whereas
the log file contains the resulting parameter configuration file (in the example above: ``exercise_config.json``), that is selected depending
on the name of the variant provided in command line of the Robot Framework.

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

We recommend to execute every robot file in command line. This is because of in lots of cases command line parameters are required
when the tests are executed. Corresponding informations you will find in the documentation inside the exercise folder.

Every exercise folder will have it's own log files folder with the log files having the same name like the executed robot files:

* Test: ``exercise-x.robot``
* Log: ``logfiles/exercise-x.log``

exercise-01
~~~~~~~~~~~

Simplest example referring to the default configuration from installation

exercise-02
~~~~~~~~~~~

Demonstrates several ways to define the configuration in command line

exercise-03
~~~~~~~~~~~

Demonstrates several ways to load the configuration from a ``config`` folder

exercise-04
~~~~~~~~~~~

Demonstrates the usage of an ``__init__.robot`` file in case of several robot files inside a testsuites folder shall run under the same conditions

exercise-05
~~~~~~~~~~~

Demonstrates the usage of nested parameter configuration files

exercise-06
~~~~~~~~~~~

Demonstrates the usage of local parameter configuration files

exercise-07
~~~~~~~~~~~

Demonstrates the priority of configuration parameters


TOC_

----

Hint: To learn more about how to work with parameters of different data types in JSON files please take a look at the tutorial ``100_variables_and_datatypes``.

----

*Tutorial v. 0.11.0 / 09.01.2023 / by MS/EMC1-XC Mai Dinh Nam Son and XC-CT/ECA3-Queckenstedt*

.. _TOC: `Table of content`_


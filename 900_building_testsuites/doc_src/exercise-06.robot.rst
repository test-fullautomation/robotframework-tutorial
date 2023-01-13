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

exercise-06
===========

----

Content
-------

``exercise-06`` demonstrates the usage of local parameter configuration files.

Background: In previous exercises we handled common parameters that are valid for all variants, and we handled variant specific parameters.
Already in the introduction we mentioned a third level: parameters that are specific for certain test benches.

The need to define test bench specific parameters is fulfilled by the *local configuration* feature of the **RobotFramework_TestsuitesManagement**.

The meaning of *local* in this context is: placed on a certain test bench - and valid for this bench only.

Also this local configuration is based on configuration files in JSON format. These files are the last ones that are considered when the configuration is loaded.
The outcome is that it is possible to define default values for test bench specific parameters in other configuration files - to be also test bench independent.
And it is possible to use the local configuration to overwrite these default values with values that are specific for a certain test bench.

Using this local configuration feature is an option and the **RobotFramework_TestsuitesManagement** provides two ways to realize it:

1. *per command line*

   Path and name of the local parameter configuration file is provided in command line of the Robot Framework with the following syntax:

   .. code::

      --variable local_config:"<path to localconfig file>"

2. *per environment variable*

   An environment variable named ``ROBOT_LOCAL_CONFIG`` exists and contains path and name of a local parameter configuration file.

   **The user has to create this environment variable!**

   This mechanism allows a user - without any command line extensions - automatically to refer on every test bench to an individual local configuration,
   simply by giving on every test bench this environment variable an individual value.

The command line has a higher priority than the environment variable. If both is available the local configuration is taken from command line.

Recommendation: *To avoid an accidental overwriting of local configuration files in version control systems we recommend to give those files
names that are test bench specific.*

In this exercise a local configuration is realized in the following way:

The ``config`` folder contains the already known configuration files

.. code::

   config/exercise-06_config_common.json
   config/exercise-06_variants.json
   config/exercise-06_config_default.json
   config/exercise-06_config_variant1.json
   config/exercise-06_config_variant2.json

The test strings have been extended. The file ``exercise-06_config_common.json`` now also contains two test bench specific default values:

.. code::

   "teststring_common" : "I am the common teststring valid for all variants and all test benches",
   "teststring_bench"  : "I am the teststring containing the default value for all test benches"

Every variant specific configuration file contains also values that are specific for the variant, but the default for the available test benches 1 and 2,
e.g. ``exercise-06_config_variant1.json``:

.. code::

   "[import]"           : "./exercise-06_config_common.json",
   "teststring_variant" : "I am the 'variant1' configuration of exercise 06"

New in this exercise is a ``localconfig`` folder with a local configuration for bench 1 and another one for bench 2:

.. code::

   localconfig/exercise-06_localconfig_bench1.json
   localconfig/exercise-06_localconfig_bench2.json

In every of theses files a test bench specific value is defined, e.g. in ``exercise-06_localconfig_bench1.json``:

.. code::

   ${params}['global']['teststring_bench'] : "I am the 'bench1' configuration of exercise 06"

Here the local configuration is used to overwrite a parameter that is already defined within the ``params:global`` section of
another configuration file. Therefore this scope has to be used:

.. code::

   ${params}['global']['teststring_bench']

In ``exercise-06.robot`` all test strings are logged: ``teststring_common``, ``teststring_variant`` and ``teststring_bench``.

We have now several possibilities:

1. No variant name given in command line, no local configuration

2. Variant name given in command line, no local configuration

3. No variant name given in command line, with local configuration

4. Variant name given in command line, with local configuration

Because every test string is initialized, every combination works - even in case of no variant and also no local configuration is given.
Default values are taken from ``exercise-06_config_default.json`` (``teststring_variant``) and ``exercise-06_config_common.json``
(``teststring_common`` and ``teststring_bench``).

----

Command line
------------

Starting with first option: no variant, no local configuration:

.. code::

   "%RobotPythonPath%/python.exe" -m robot -d ./logfiles -o exercise-06.xml -l exercise-06_log.html -r exercise-06_report.html -b exercise-06.log "./exercise-06.robot"

----

Outcome
-------

The parameter values are:

.. code::

   teststring_common : I am the common teststring valid for all variants and all test benches
   teststring_variant : I am the 'default' variant configuration of exercise 06
   teststring_bench : I am the teststring containing the default value for all test benches

----

Command line
------------

To cover the remaining three options use the following command lines:

Variant 1, no local configuration

.. code::

   "%RobotPythonPath%/python.exe" -m robot -d ./logfiles -o exercise-06.xml -l exercise-06_log.html -r exercise-06_report.html -b exercise-06.log --variable variant:"variant1" "./exercise-06.robot"

No variant, with local bench1 configuration

.. code::

   "%RobotPythonPath%/python.exe" -m robot -d ./logfiles -o exercise-06.xml -l exercise-06_log.html -r exercise-06_report.html -b exercise-06.log --variable local_config:"./localconfig/exercise-06_localconfig_bench1.json" "./exercise-06.robot"

Variant 2, with local bench2 configuration

.. code::

   "%RobotPythonPath%/python.exe" -m robot -d ./logfiles -o exercise-06.xml -l exercise-06_log.html -r exercise-06_report.html -b exercise-06.log --variable variant:"variant2" --variable local_config:"./localconfig/exercise-06_localconfig_bench2.json" "./exercise-06.robot"

----

Outcome
-------

The values of ``teststring_variant`` and ``teststring_bench`` are updated accordingly to the settings in command line.
The value of ``teststring_common`` stays unchanged.

Also the log file reflects the fact that an additional configuration file is involved.

For example, in case of the local configuration for bench1 is requested, but no certain variant (possibility 3),
the log file contains the following entries:

.. code::

   Running with configuration level: 2
   CfgFile Path: ./config/exercise-06_config_default.json
   Local config file: ./localconfig/exercise-06_localconfig_bench1.json

Extension I
-----------

Instead of defining the local configuration in command line with

.. code::

   --variable local_config:"<path to localconfig file>"

define now the local configuration within an environment variable.

Create an environment variable with name ``ROBOT_LOCAL_CONFIG`` and value 

.. code::

   <tutorial root path>/exercise-06/localconfig/exercise-06_localconfig_bench1.json

With this change execute the next command line.

Command line
------------

This command line selects ``variant1``:

.. code::

   "%RobotPythonPath%/python.exe" -m robot -d ./logfiles -o exercise-06.xml -l exercise-06_log.html -r exercise-06_report.html -b exercise-06.log --variable variant:"variant1" "./exercise-06.robot"

Outcome
-------

Because ``ROBOT_LOCAL_CONFIG`` points to ``exercise-06_localconfig_bench1.json``, the value of ``teststring_bench``
is the ``bench1`` specific one.

.. code::

   teststring_common : I am the common teststring valid for all variants and all test benches
   teststring_variant : I am the 'variant1' configuration of exercise 06
   teststring_bench : I am the 'bench1' configuration of exercise 06

What will happen in case you extend the command line above with:

.. code::

   --variable local_config:"./localconfig/exercise-06_localconfig_bench2.json"

Then you have two contradicting settings in environment variable and in command line. Because the command line has a higher priority
than other settings, the output changes to:

.. code::

   teststring_common : I am the common teststring valid for all variants and all test benches
   teststring_variant : I am the 'variant1' configuration of exercise 06
   teststring_bench : I am the 'bench2' configuration of exercise 06

What will happen in case you extend the (already extended) command line again, but now with:

.. code::

   --variable teststring_bench:"teststring_bench command line value"

Single parameter definitions mady by ``--variable`` in command line have higher priority than any other settings.
Because of this the ``teststring_bench`` now has the value provided in command line immediately.

.. code::

   teststring_common : I am the common teststring valid for all variants and all test benches
   teststring_variant : I am the 'variant1' configuration of exercise 06
   teststring_bench : teststring_bench command line value

Extension II
------------

It might be required to support parameters that are both together: specific for a variant and additionally specific for a test bench also.
In this case you should initialize these parameters in the variant specific configuration files and make them specific for a certain test bench
in the local configuration files. Give it a try.




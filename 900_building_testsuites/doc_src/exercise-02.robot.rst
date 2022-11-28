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

exercise-02
===========

----

Content
-------

``exercise-02`` demonstrates several ways to define the configuration in command line. This can be used to realize a variant handling.

We assume to have the variants ``variant1``, ``variant2`` and a ``default`` variant. For every variant we need a configuration file defining the
parameter values that are specific for this variant. In this exercise that are the files

* ``config/exercise-02_config_default.json``
* ``config/exercise-02_config_variant1.json``
* ``config/exercise-02_config_variant2.json``

Every of these files define a test string containing an individual value, e.g. ``exercise-02_config_variant1.json``:

.. code::

   "teststring" : "I am the 'variant1' configuration of exercise 02"

Additionally we need another configuration file defining a mapping between the variant name and the corresponding configuration file:

* ``config/exercise-02_variants.json``

With the following content:

.. code::

   {
     "default": {
                  "name": "exercise-02_config_default.json",
                  "path": "./config/"
                },
     "variant1": {
                  "name": "exercise-02_config_variant1.json",
                  "path": "./config/"
                 },
     "variant2": {
                  "name": "exercise-02_config_variant2.json",
                  "path": "./config/"
                 }
   }

In exercise-02.robot we execute the ``testsuites.testsuite_setup`` without providing any configuration file:

.. code::

   Suite Setup    testsuites.testsuite_setup

In exercise-02-B.robot we hand over the mapping configuration file to the ``testsuites.testsuite_setup``:

.. code::

   Suite Setup    testsuites.testsuite_setup    ./config/exercise-02_variants.json

And we print the content of the test string:

.. code::

   Log    teststring : ${teststring}    console=yes

Now we have several possibilities:

1. Define a variant specific configuration file directly in command line (``exercise-02.robot``)
2. Execute the test without any variant specific command line extensions (``exercise-02-B.robot``)
3. Define only the name of a variant in command line (``exercise-02-B.robot``)

Starting with the first option ...

----

1. Define a variant specific configuration file directly in command line (``exercise-02.robot``)

Command line
------------

.. code::

   "%RobotPythonPath%/python.exe" -m robot -d ./logfiles -o exercise-02.xml -l exercise-02_log.html -r exercise-02_report.html -b exercise-02.log --variable config_file:"./config/exercise-02_config_variant1.json" "./exercise-02.robot"

----

Outcome
-------

A variant specific configuration file can be set with the following command line extension:

.. code::

   --variable config_file:"<path to configuration file>"

Here we selected the one for ``variant1``. Therefore the test string has the value

.. code::

   I am the 'variant1' configuration of exercise 02

The log file gives more information about the origin

.. code::

   Running with configuration level: 1
   CfgFile Path: ./config/exercise-02_config_variant1.json

*TODO: Explain the background of the level warning* :

``[ WARN ] The configuration level 1 is set for this Robot run!``

Continuing with the second option ...

----

2. Execute the test without any variant specific command line extensions (``exercise-02-B.robot``)

Command line
------------

.. code::

   "%RobotPythonPath%/python.exe" -m robot -d ./logfiles -o exercise-02.xml -l exercise-02_log.html -r exercise-02_report.html -b exercise-02.log "./exercise-02-B.robot"

----

Outcome
-------

Because no variant name is provided in command line, the defined ``default`` variant is loaded and the test string has the value

.. code::

   I am the 'default' variant configuration of exercise 02

The log file gives more information about the origin

.. code::

   Running with configuration level: 2
   CfgFile Path: ./config/exercise-02_config_default.json

Continuing with the third option ...

----

3. Define only the name of a variant in command line (``exercise-02-B.robot``)

Command line
------------

.. code::

   "%RobotPythonPath%/python.exe" -m robot -d ./logfiles -o exercise-02.xml -l exercise-02_log.html -r exercise-02_report.html -b exercise-02.log --variable variant:"variant2" "./exercise-02-B.robot"

----

Outcome
-------

A variant name can be provided with the following command line extension

.. code::

   --variable variant:"<variant name>"

Choosing the variant name ``variant2`` cause the following results:

The test string

.. code::

    I am the 'variant2' configuration of exercise 02

The log file

.. code::

   Running with configuration level: 2
   CfgFile Path: ./config/exercise-02_config_variant2.json

----

Further hints
-------------

A certain aspect needs more consideration: How to access configuration parameter in robot files?

Remember the content of one of the configuration files:

.. code::

   {
     "WelcomeString": "Hello... RobotFramework AIO is running now!",

     "Maximum_version": "0.5.2",
     "Minimum_version": "0.5.2",

     "Project": "RobotFramework Testsuites",
     "TargetName" : "Device_01",

     "params" : {
                 "global": {
                            "teststring" : "I am the 'default' variant configuration of exercise 02"
                           }
                }
   }

The parameters ``WelcomeString``, ``Maximum_version``, ``Minimum_version``, ``Project`` and ``TargetName`` are mandatory default parameters of the
**RobotFramework_Testsuites**. They are realized as keys of a global dictionary. Therefore the have to be accessed e.g. in this way:

.. code::

   ${CONFIG}[Maximum_version]

All user defined parameters within ``params:global`` are accessible directly, e.g.:

.. code::

   ${teststring}




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

exercise-07
===========

----

Content
-------

``exercise-07`` demonstrates the priority of configuration parameters.

Background: In previous exercises we handled the level concept. This concept introduces four levels of priority
that define, which of the possible sources of configuration parameters are processed.
But there are other rules involved that influence the priority:

* *The local configuration has higher priority than other parameter configurations*
* *The command line has higher priority than definitions within configuration files*

Already in command line we have several possibilities to make settings:

* *Set a parameter configuration file* (with **RobotFramework_TestsuitesManagement** command line variable ``config_file``, *level 1*)
* *Set a variant name* (with **RobotFramework_TestsuitesManagement** command line variable ``variant``, *level 2*)
* *Set a local configuration* (with **RobotFramework_TestsuitesManagement** command line variable ``local_config``)
* *Set any other variables* (directly with Robot Framework command line variable ``--variable``)

And it is possible that in all four use cases the same parameters are used. Or in other words: It is possible to use the
``--variable`` mechanism to define a parameter that is also defined within a parameter configuration or within a local configuration - or
in both together.

Finally this is the order of processing (with highest priority first):

1. Single command line variable (``--variable``)
2. Local configuration (``local_config``)
3. Variant specific configuration (``config_file`` or ``variant``)

Meaning:

1. Variant specific configuration is overwritten by local configuration
2. Local configuration is overwritten by single command line variable

What happens in case of a command line contains both a ``config_file`` and a ``variant``?

``config_file`` is level 1 and ``variant`` is level 2. Level 1 has higher priority than level 2. Therefore ``config_file``
is the valid one. This does **not** mean that ``config_file`` overwrites ``variant``! In case of a certain level is identified
(here: level 1), all other levels are ignored. The outcome is that - in this example - the ``variant`` has no meaning.
Between different levels there is an *either or* relationship. And that is the reason for that it makes no sense to define both in command line,
a ``config_file`` and a ``variant``. The **RobotFramework_TestsuitesManagement** throws an error in this case.

But when additionally ``--variable`` is used to define a new value for a parameter that is already defined in one of the involved configuration files,
then the configuration file value is overwritten by the command line value.

In this exercise the configuration is realized in the following way:

The ``config`` folder contains the already known configuration files

.. code::

   config/exercise-07_variants.jsonp
   config/exercise-07_config_default.jsonp
   config/exercise-07_config_variant1.jsonp
   config/exercise-07_config_variant2.jsonp

The ``localconfig`` folder contains the already known local configuration files

.. code::

   localconfig/exercise-07_localconfig_bench1.jsonp
   localconfig/exercise-07_localconfig_bench2.jsonp

The test strings from previous exercises are reduced to one single test string: ``teststring``.
Every configuration file contains an individual value indicating also the origin: variant configuration or local configuration.

``exercise-07.robot`` uses the ``testsuite_setup`` without a variant configuration file and ``exercise-07-B.robot`` uses
``testsuite_setup`` with a variant configuration file.

Both robot files log the test string.

We have now several possibilities to execute the robot files in this exercise with several combinations of all possible ways to define
configuration parameter:

* ``--variable`` and ``config_file``

  Variant configuration is overwritten by command line variable.

* ``--variable`` and ``local_config`` and ``config_file``

  Variant configuration is overwritten by local configuration.
  Local configuration is overwritten by command line variable.

* ``--variable`` and ``local_config`` and ``variant``

  Variant configuration is overwritten by local configuration.
  Local configuration is overwritten by command line variable.

* ``--variable`` and ``local_config``

  Local configuration is overwritten by command line variable.

The order of these settings in command line of the Robot Framework has no meaning!

Depending on the combination and depending on the priorities in this combination, the test string has a corresponding value.

----

Command line
------------

For example we take a look at the second option:

``--variable`` and ``local_config`` and ``config_file``

.. code::

   "%RobotPythonPath%/python.exe" -m robot -d ./logfiles -o exercise-07.xml -l exercise-07_log.html -r exercise-07_report.html -b exercise-07.log --variable teststring:"command line test string" --variable local_config:"./localconfig/exercise-07_localconfig_bench1.jsonp" --variable config_file:"./config/exercise-07_config_variant1.jsonp" "./exercise-07.robot"

----

Outcome
-------

The command line value overwrites the variant configuration and also the local configuration and therefore the value of the test string is:

.. code::

   teststring : command line test string

----

Now it's on you to explore the other combinations.





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

exercise-08
===========

----

Content
-------

``exercise-08`` is the final example in this tutorial. Similar to ``exercise-04`` the test files can be found within a ``testsuites`` folder.

We assume here that the software under test consists of two components: ``component-A`` and ``component-B``. The corresponding test files are placed
in the following sub folders:

.. code::

   testsuites/component-A
   testsuites/component-B

Every component has two features. Altogether the following test files are involved:

The common ones:

.. code::

   testsuites/__init__.robot
   testsuites/exercise-08.robot

Together with the feature specific ones:

.. code::

   testsuites/component-A/feature-A-1/exercise-08-feature-A-1-test.robot
   testsuites/component-A/feature-A-2/exercise-08-feature-A-2-test.robot
   testsuites/component-B/feature-B-1/exercise-08-feature-B-1-test.robot
   testsuites/component-B/feature-B-2/exercise-08-feature-B-2-test.robot

Similar to previous exercises the ``config`` folder contains the variant specific configuration files:

.. code::

   config/exercise-08_config_common.json
   config/exercise-08_config_default.json
   config/exercise-08_config_variant1.json
   config/exercise-08_config_variant2.json
   config/exercise-08_variants.json

and the ``localconfig`` folder contains the test bench specific configuration files:

.. code::

   localconfig/exercise-08_localconfig_bench1.json
   localconfig/exercise-08_localconfig_bench2.json

Also this exercise works with the already known common, variant specifc and test bench specific test strings:

.. code::

   teststring_common
   teststring_variant
   teststring_bench

To test your knowledge try to answer the following questions:

* What is the meaning of ``.../config/`` inside file ``exercise-08_variants.json``?
* A parameter shall have the same value in all variants. Where to define this parameter?
* What is the difference between a variant configuration file and a parameter configuration file?
* Which possibilities do you have to define a variant in command line of Robot Framework?
* A parameter shall have different values on different test benches. Where to initialize this parameter and
  where to define the test bench specific value?
* A parameter is defined within a variant specific parameter configuration file. Which possibilities do you have
  to change the value of this parameter without changing the code of this definition?
* A parameter is defined at three positions: within a variant specific parameter configuration file,
  within a local configuration file and within command line with ``--variable``.
  Which position will define the resulting value of this parameter?

In case you are not sure, use the test files in this exercise to get the answer.

*Good luck!*






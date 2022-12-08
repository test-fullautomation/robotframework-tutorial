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

exercise-05
===========

----

Content
-------

``exercise-05`` demonstrates the usage of nested parameter configuration files.

Background: In case of a project requires more and more parameters, it makes sense to split the growing configuration file into smaller ones.
In previous exercises all variant specific configuration files contain all parameters required for this variant - separately.
But *required* is not *specific*. There might parameters be required, that have the same value in all variants. If we put them
into every variant specific configuration file, we create a lot of redundancy. And we complicate the maintenance.

The solution is to use the variant specific configuration files only for variant specific parameters and to put all common parameters in
a separate configuration file. This common parameter file has to be imported in every variant specific parameter file.

The outcome is that still with the selection of a certain variant specific parameter file both types of parameters are available:
the variant specific ones and the common ones.

In this exercise this concept is realized in the following way:

The config folder contains the already known variants configuration file

.. code::

   config/exercise-05_variants.json

together with variant specific parameter configuration files

.. code::

   config/exercise-05_config_default.json
   config/exercise-05_config_variant1.json
   config/exercise-05_config_variant2.json

New in this exercise is a common parameter configuration file

.. code::

   config/exercise-05_config_common.json

containing a parameter that shall have the same value for every variant:

.. code::

   "teststring_common" : "I am the common teststring valid for all variants"

The variant specific parameter configuration files still contain their own specific parameter definitions and additionally
the import of the common configuration file, e.g.:

.. code::

   "params" : {
               "global": {
                          "[import]"   : "./exercise-05_config_common.json",
                          "teststring" : "I am the 'variant1' configuration of exercise 05"
                         }
              }

The key ``[import]`` indicates the import of another configuration file. The value of the key is the path and name of this file.

The content of the importing file and the content of all imported files are merged. In case of duplicate parameter names follow up definitions
overwrite previous definitions of the same parameter! Also imported files need to follow the JSON syntax rules. This means, at least they have
to start with an opening curly bracket and they have to end with a closing curly bracket.

The full code of ``exercise-05_config_common.json`` therefore is

.. code::

   {
      "teststring_common" : "I am the common teststring valid for all variants"
   }

The test suite ``exercise-05.robot`` of this exercise prints the value of both the common parameter and the specific parameter

.. code::

   Log    teststring_common : ${teststring_common}    console=yes
   Log    teststring : ${teststring}    console=yes

We have now the same possibilities like in previous exercies: We can execute the test suite with providing a variant name and without.
In second case the ``default`` variant is choosed automatically.

----

Command line
------------

Selecting variant1:

.. code::

   "%RobotPythonPath%/python.exe" -m robot -d ./logfiles -o exercise-05.xml -l exercise-05_log.html -r exercise-05_report.html -b exercise-05.log --variable variant:"variant1" "./exercise-05.robot"

----

Outcome
-------

The parameter values are:

.. code::

   teststring_common : I am the common teststring valid for all variants
   teststring : I am the 'variant1' configuration of exercise 05

Select another variant in command line - and you will see: The ``teststring`` changes, the ``teststring_common`` stays unchanged.



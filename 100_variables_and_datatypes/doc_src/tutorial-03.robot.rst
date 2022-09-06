.. Copyright 2020-2022 Robert Bosch GmbH

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

   http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.

tutorial-03: working with dictionaries
======================================

**Data sets**

Within

.. code::

   ./libs/testimport.resource

the scalars of tutorial-01 are put together within a dictionary

.. code::

   &{var_dict}    key_01=${var_01}
   ...            key_02=${var_02}
              ...
   ...            key_18=${var_18}

The keyword library

.. code::

   ./libs/testlibrary.py

contains the keyword ``log_dict`` that logs the value and the type of all keys of a given dictionary (``param``):

.. code::

   for key in param:
      key_value = str(param[key])
      key_type  = str(type(param[key]))
      BuiltIn().log(f"+ key: '{key}' / value: '{key_value}' / type: {key_type}", "INFO", console=True)

**Robot file**

``tutorial-03.robot`` demonstrates how to work with dictionaries.

**Execution**

.. code::

   "%RobotPythonPath%/python.exe" -m robot -d ./logfiles -o tutorial-03.xml -l tutorial-03_log.html -r tutorial-03_report.html -b tutorial-03.log ./tutorial-03.robot

Test case 03_01
---------------

In test case ``03_01`` all dictionary keys are logged with ``log_dict``:

.. code::

   log_dict    ${var_dict}

**Outcome**

Values and data types are the same like in tutorial-01 and tutorial-02.

Test case 03_02
---------------

In test case ``03_02`` single keys of the dictionary are accessed in two ways:

1. Key name is hard coded
2. Key name is variable of type string

.. code::

   log_scalar    ${var_dict}[key_06]
   log_scalar    ${var_dict}[${key_as_string}]

The following key variable is used:

.. code::

   ${key_as_string}    key_06

**Outcome**

In both cases the result is the same (``123``). The Robot Framework documentation tells that when using this syntax: ``${var}``, this expression
is replaced by the value of the variable (``var``) *as-is*.

Therefore ``${key_as_string}`` is replaced by ``key_06``. The result is that in both cases ``${var_dict}[key_06]`` is the expression to be evaluated.




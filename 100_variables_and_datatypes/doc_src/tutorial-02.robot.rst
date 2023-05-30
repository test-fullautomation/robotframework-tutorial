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

tutorial-02: working with lists
===============================

**Data sets**

Before we go to the tests of this tutorial we take a look at the variables used here:

Within

.. code::

   ./libs/testimport.resource

the scalars of tutorial-01 are put together within a list

.. code::

   @{var_list}    ${var_01}
   ...            ${var_02}
              ...
   ...            ${var_18}

The keyword library

.. code::

   ./libs/testlibrary.py

contains the keyword ``log_list`` that logs the value and the type of all elements of a given list (``param``):

.. code::

   for element in param:
      elem_value = str(element)
      elem_type  = str(type(element))
      BuiltIn().log(f"+ value: '{elem_value}' / type: {elem_type}", "INFO", console=True)

**Robot file**

``tutorial-02.robot`` demonstrates how to work with lists.

**Execution**

.. code::

   "%RobotPythonPath%/python.exe" -m robot -d ./logfiles -o tutorial-02.xml -l tutorial-02_log.html -r tutorial-02_report.html -b tutorial-02.log ./tutorial-02.robot

Test case 02_01
---------------

In test case ``02_01`` all list elements are logged with ``log_list``:

.. code::

   log_list    ${var_list}

**Outcome**

Values and data types are the same like in tutorial-01.

Test case 02_02
---------------

In test case ``02_02`` single elements of the list are accessed in three ways:

1. Index is hard coded
2. Index is variable of type string
3. Index is variable of type integer

.. code::

   log_scalar    ${var_list}[5]
   log_scalar    ${var_list}[${index_as_string}]
   log_scalar    ${var_list}[${index_as_integer}]

The following index variables are used:

.. code::

   ${index_as_string}    5
   ${index_as_integer}   ${5}

**Outcome**

In all three cases the result is the same (``123``). The Robot Framework documentation tells that when using this syntax: ``${var}``, this expression
is replaced by the value of the variable (``var``) *as-is*.

Therefore ``${index_as_string}`` is replaced by ``5`` and also ``${index_as_integer}`` is replaced by ``5``. The result is that in all three cases
``${var_list}[5]`` is the expression to be evaluated.

**Addendum**

Instead of using resource files it is also possible to define lists in JSON configuration files.

Example:

.. code::

   "params" : {
                "global" : {
                             "string_val" : "string",
                             "int_val"    : 123,
                             "bool_val"   : True,
                             "list_val"   : ["also string",
                                             456,
                                             ${params}['global']['string_val'],
                                             ${params}['global']['int_val'],
                                             ${params}['global']['bool_val']]
                           }
              }

The handling of JSON configuration files is explained in more detail in

* file `tutorial-03 <https://htmlpreview.github.io/?https://github.com/test-fullautomation/robotframework-tutorial/blob/develop/100_variables_and_datatypes/tutorial-03.robot.html>`_ of this tutorial
* tutorial `900_building_testsuites <https://htmlpreview.github.io/?https://github.com/test-fullautomation/robotframework-tutorial/blob/develop/900_building_testsuites/building_testsuites.html>`_

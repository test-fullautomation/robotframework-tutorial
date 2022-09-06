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

tutorial-01: working with scalars
=================================

**Data sets**

Within

.. code::

   ./libs/testimport.resource

the following scalars are defined:

.. code::

   ${ABC}    ABC

   ${var_01}    ABC
   ${var_02}    "ABC"
   ${var_03}    ${ABC}
   ${var_04}    123
   ${var_05}    "123"
   ${var_06}    ${123}
   ${var_07}    4.56
   ${var_08}    "4.56"
   ${var_09}    ${4.56}
   ${var_10}    True
   ${var_11}    "True"
   ${var_12}    ${True}
   ${var_13}    False
   ${var_14}    "False"
   ${var_15}    ${False}
   ${var_16}    None
   ${var_17}    "None"
   ${var_18}    ${None}

Every value is defined in three different ways:

1. immediately as literal
2. literal wrapped in quotes
3. literal wrapped in curly brackets with dollar operator

*What will be the data types of the variables* ``var_01`` - ``var_18`` *?*

To answer this question the keyword library

.. code::

   ./libs/testlibrary.py

contains the keyword ``log_scalar`` that logs the value and the type of a given scalar (``param``):

.. code::

   scalar_value = str(param)
   scalar_type  = str(type(param))
   BuiltIn().log(f"+ value: '{scalar_value}' / type: {scalar_type}", "INFO", console=True)

**Robot file**

``tutorial-02.robot`` demonstrates how to work with scalars.

**Execution**

.. code::

   "%RobotPythonPath%/python.exe" -m robot -d ./logfiles -o tutorial-01.xml -l tutorial-01_log.html -r tutorial-01_report.html -b tutorial-01.log ./tutorial-01.robot

**Test case 01_01**

In test case ``01_01`` all variables listed above are logged with ``log_scalar``:

.. code::

   log_scalar    ${var_01}
   ...
   log_scalar    ${var_18}

**Outcome**

* Without quotes and curly brackets all values are interpreted as string - even in case they can be interpreted as
  integer (``var_04``) or keywords (``var_10``) also.
* In case of values are wrapped in quotes, these quotes are part of the string (e.g. ``var_02``).
* With the dollar notation ``${...}`` numerical data types like ``integer`` or ``float`` are kept (``var_06``, ``var_09``).
* With the dollar notation ``${...}`` Python keywords like the boolean ``True`` and ``False`` and also the Python singleton ``None`` are kept
  (``var_12``, ``var_15`` and ``var_18``).
* The dollar notation with an argument that cannot be interpreted as a numrical value (e.g. ``${ABC}``), requires that the argument is the name
  of an existing variable (``var_03``).

**Test case 01_02**

Test case ``01_02`` contains some arithmetical computation and concatenations of variables with different data types.

To go also some other ways like before the variables of this test are defined as test variable.
We have two numbers defined as string (``test_var_1`` and ``test_var_2``).
We have two numbers defined as integer (``test_var_3`` and ``test_var_4``).
And we have three strings (``test_var_5``, ``test_var_6`` and ``test_var_7``).

.. code::

   Set Test Variable    ${test_var_1}    1
   Set Test Variable    ${test_var_2}    2.3
   Set Test Variable    ${test_var_3}    ${3}
   Set Test Variable    ${test_var_4}    ${4.5}
   Set Test Variable    ${test_var_5}    A
   Set Test Variable    ${test_var_6}    B
   Set Test Variable    ${test_var_7}    'C'

With these variables test case ``01_02`` does the following arithmetical computations and concatenations:

1. Arithmetical computation of two numbers defined as string

   .. code::

      ${result} =    Evaluate    ${test_var_1} + ${test_var_2}
      log_scalar     ${result}

2. Arithmetical computation of two numbers defined as integer and float

   .. code::

      ${result} =    Evaluate    ${test_var_3} + ${test_var_4}
      log_scalar     ${result}

3. Arithmetical computation of two numbers defined as string and float

   .. code::

      ${result} =    Evaluate    ${test_var_1} + ${test_var_4}
      log_scalar     ${result}

4. Catenation of two numbers defined as string

   .. code::

      ${result} =    Catenate    ${test_var_1}    ${test_var_2}
      log_scalar     ${result}

5. Catenation of two numbers defined as integer and float

   .. code::

      ${result} =    Catenate    ${test_var_3}    ${test_var_4}
      log_scalar     ${result}

6. Catenation of two strings

   .. code::

      ${result} =    Catenate    ${test_var_5}    ${test_var_6}
      log_scalar     ${result}

7. Catenation of an integer with a string (with quotes)

   .. code::

      ${result} =    Catenate    "${test_var_3}"    ${test_var_7}
      log_scalar     ${result}


8. Catenation of two numbers defined as integer and float (with no space in between)

   .. code::

      ${test_var_7} =    Catenate    SEPARATOR=    ${test_var_3}    ${test_var_4}
      log_scalar     ${test_var_7}

9. Arithmetical computation of the new variable test_var_7 (string) with an integer

   .. code::

      ${result} =    Evaluate    ${test_var_7} + ${test_var_3}
      log_scalar     ${result}




**Outcome**

Where necessary the Robot Framework automatically converts the data types to enable arithmetic computations and catenations.


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

Test case 01_01
---------------

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

Test case 01_02
---------------

Test case ``01_02`` contains some arithmetical computation and concatenations of variables with different data types.

To go also some other ways like before the variables of this test are defined as test variable.
We have two numbers defined as string (``test_var_1`` and ``test_var_2``).
We have two numbers defined as integer (``test_var_3``) and float (``test_var_4``).
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

Test case 01_03
---------------

Test case ``01_03`` contain the comparison of variables in several combinations. This test case works again with the variables from

.. code::

   ./libs/testimport.resource``

Comparisons:

1. Comparison of string variable with hard coded string

   .. code::

      ${status}=    Evaluate    "${var_01}" == "ABC"

2. Comparison of two different kind of string variables (pay attention of the usage of the quotes)

   .. code::

      ${status}=    Evaluate    "${var_01}" == ${var_02}

3. Comparison of a number (as string) with a number (as integer)

   .. code::

      ${status}=    Evaluate    ${var_04} == ${var_06}

4. Comparison of a number (as string) with a number (as integer), (pay attention of the usage of the quotes)

   .. code::

      ${status}=    Evaluate    ${var_05} == "${var_06}"

5. Comparison of boolean values

   .. code::

      ${status}=    Evaluate    ${var_10} == ${var_12}

6. Comparison of numbers (as string)

   .. code::

      ${status}=    Evaluate    ${var_04} > ${var_07}

7. Comparison of numbers (as string; short form)

   .. code::

      IF    ${var_04} > ${var_07}

8. Comparison of numbers (as integers; short form)

   .. code::

      IF    ${var_06} > ${var_09}

9. Comparison of numbers (one as string and one as integer; short form)

   .. code::

      IF    ${var_04} > ${var_09}

**Outcome**

All comparisons are ``True``.


Test case 01_04
---------------

Test case ``01_04`` contains the computation of variables defined within the following json configuration file:

.. code::

   ./config/tutorialconfig.json

Within the global params section of this configuration file the following scalars are defined (also lists and dictionaries, but they will be handled
in other parts of this tutorial):

.. code::

   "string_val" : "test string",
   "int_val" : 123,
   "float_val" : 4.56,
   "bool_val_1" : True,
   "bool_val_2" : true,
   "bool_val_3" : False,
   "bool_val_4" : false,
   "none_val" : None,
   "null_val" : null

*Background:*

Basically the json configuration files of the Robot Framework AIO have to follow the syntax rules of the json format. But the Robot Framework AIO extends
this syntax by some additional features like

* the possibility to add comments,
* the possibility to use the ``${}`` syntax to refer to parameters,
* the possibility to use also the Python syntax for certain keywords (relevant because there are differences between Python and json).

In Python the boolean values are written with the first letter capitalized (``True``, ``False``). In json they are written in small letters completely
(``true``, ``false``). The Python singleton ``None`` is ``null`` in json.

Now it is obvious that the parameters ``bool_val_1``, ``bool_val_3`` and ``none_val`` follow the Python way of typing them and the parameters
``bool_val_2``, ``bool_val_4`` and ``null_val`` follow the json way of typing them.

*Possible is both!*

But this has to be considered: In case of the json way of typing is choosed, internally the values are converted to the Python way of typing.
If you implement own keyword libraries in Python you have to use the way of typing keywords, that is Python specific.

In this test case at first the content of every parameter is logged with the already knwon ``log_scalar`` keyword:

.. code::

   log_scalar    ${string_val}
   log_scalar    ${int_val}
   log_scalar    ${float_val}
   log_scalar    ${bool_val_1}
   log_scalar    ${bool_val_2}
   log_scalar    ${bool_val_3}
   log_scalar    ${bool_val_4}
   log_scalar    ${none_val}
   log_scalar    ${null_val}

**Outcome**

* The value of ``bool_val_2`` is ``True`` - even in case of the parameter is defined with ``true`` within the json file.
* The value of ``bool_val_4`` is ``False`` - even in case of the parameter is defined with ``false`` within the json file.
* The value of ``null_val`` is ``None`` - even in case of the parameter is defined with ``null`` within the json file.

This test case finishes with some comparisons between parameters defined in json file and parameters defined in the resource file.

Because of the internal conversion of keywords take a deeper look at the following expressions:

.. code::

   IF    ${bool_val_2} != "true"

   IF    ${null_val} != "null"

**Outcome**

All comparisons are ``True``.


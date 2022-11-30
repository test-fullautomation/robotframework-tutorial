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

tutorial-04: working with variable files in command line
========================================================

**Data sets**

Before we go to the tests of this tutorial we take a look at the variables used here.

Providing additional informations and settings in command line is an option. To be on the save side,
every variable should be initialized

The variables of this tutorial are initialized within

.. code::

   ./libs/testimport.resource

in the following way:

.. code::

   ${cmdline_var_1}    ${None}
   ${cmdline_var_2}    ${None}
   ${cmdline_var_3}    ${None}
   ${cmdline_var_4}    ${None}
   ${cmdline_var_5}    ${None}
   ${cmdline_var_6}    ${None}
   ${cmdline_var_7}    ${None}

Valid values are defined within the Python variable file

.. code::

   ./variables/testvariables.py

in the following way:

.. code::

   cmdline_var_1 = "variable file test string"
   cmdline_var_2 = 234
   cmdline_var_3 = 5.67
   cmdline_var_4 = ['A', 'B', 'C']
   cmdline_var_5 = {'A' : 1, 'B' : 2, 'C' : 3}
   cmdline_var_6 = True
   cmdline_var_7 = None

**Robot file**

``tutorial-04.robot`` demonstrates how to work with variable files and single variables in command line.

Test case 04_01
---------------

In test case ``04_01`` all variables are logged with ``log_scalar``:

.. code::

   log_scalar    ${variablefile_val_1}
   log_scalar    ${variablefile_val_2}
   log_scalar    ${variablefile_val_3}
   log_scalar    ${variablefile_val_4}
   log_scalar    ${variablefile_val_5}
   log_scalar    ${variablefile_val_6}
   log_scalar    ${variablefile_val_7}

**Execution**

Now we go through several ways to execute the test.

*Standard execution without any command line extensions*

.. code::

   "%RobotPythonPath%/python.exe" -m robot -d ./logfiles -o tutorial-04.xml -l tutorial-04_log.html -r tutorial-04_report.html -b tutorial-04.log ./tutorial-04.robot

**Outcome**

The value of all variables is ``None`` (like initialized).

----

*Execution with variable file in command line*

Now we add a variable file to command line:

.. code::

   --variablefile ./variables/testvariables.py

Complete command line:

.. code::

   "%RobotPythonPath%/python.exe" -m robot --variablefile ./variables/testvariables.py -d ./logfiles -o tutorial-04.xml -l tutorial-04_log.html -r tutorial-04_report.html -b tutorial-04.log ./tutorial-04.robot

**Outcome**

Value and data type of all variables are like defined in ``testvariables.py``.

----

*Execution with single variable in command line*

Instead of using a file containing definitions of variables it is also possible to provide single variables in command line.

But here we have a limitation: It is only possible to use string values!

Now we add a single variable to command line:

.. code::

   --variable cmdline_var_1:"command line test string"

Complete command line:

.. code::

   "%RobotPythonPath%/python.exe" -m robot --variable cmdline_var_1:"command line test string" -d ./logfiles -o tutorial-04.xml -l tutorial-04_log.html -r tutorial-04_report.html -b tutorial-04.log ./tutorial-04.robot

**Outcome**

The variable ``cmdline_var_1`` has the new value ``command line test string``. The value of all other variables is still ``None``.

----

*Execution with several variables in command line*

Now we provide two variables in command line: an integer and a boolean value:

.. code::

   --variable cmdline_var_2:234 --variable cmdline_var_6:True

Complete command line:

.. code::

   "%RobotPythonPath%/python.exe" -m robot --variable cmdline_var_2:234 --variable cmdline_var_6:True -d ./logfiles -o tutorial-04.xml -l tutorial-04_log.html -r tutorial-04_report.html -b tutorial-04.log ./tutorial-04.robot

**Outcome**

Both variables are strings! Like already mentioned above: Only string values can be defined in command line. Or in other words:
Every command line value will be interpreted as string. In case you need to work also with other data types you have to use the variable file mechanism
(``--variablefile``).

----

**Command line variables and RobotFramework_Testsuites configuration**

Up to now for command line tests we have only used variables that are not already defined within a JSON file of the **RobotFramework_Testsuites** configuration.
What will happen, when we try to overwrite such a configuration value in command line? The answer is: This will not work!

The **RobotFramework_Testsuites** configuration of the RobotFramework AIO is a certain extension of the Robot Framework. The possibility to
define values in several JSON files under certain conditions is a powerful feature - but this feature currently has the limitation
that the JSON file values cannot be overwritten in command line (with both ``--variablefile`` and ``--variable``).

Remember:

In the global params section of ``tutorialconfig.json`` the following string variable is defined:

.. code::

   "string_val" : "test string",

Use the following command line to (try to) overwrite this value:

.. code::

   "%RobotPythonPath%/python.exe" -m robot --variable string_val:"command line test string" -d ./logfiles -o tutorial-04.xml -l tutorial-04_log.html -r tutorial-04_report.html -b tutorial-04.log ./tutorial-04.robot

**Outcome**

The configuration variable ``string_val`` still has the original value ``test string``.

*Please be aware of this effect when you design your tests.*


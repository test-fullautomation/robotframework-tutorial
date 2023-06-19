.. Copyright 2020-2023 Robert Bosch GmbH

.. Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

.. http://www.apache.org/licenses/LICENSE-2.0

.. Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.

tutorial-03: working with dictionaries
======================================

**Data sets**

Before we go to the tests of this tutorial we take a look at the variables used here:

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

Test case 03_03
---------------

In test case ``03_03`` we work with nested dictionaries defined within the JSON configuration file of this tutorial.

.. code::

   ./config/tutorialconfig.jsonp

But before we start, some internals need to be mentioned: The JSON format and the robot code format are two different worlds.
Both have their own formats. But the **RobotFramework_TestsuitesManagement** is able to convert the formats, and when the JSON
file content is passed to the Robot Framework, then the content is adapted.

But behind the curtain still JSON parsing mechanisms are used to get the content and therefore it is not possible to align already
the structure of the JSON files itself to the requirements of the Robot Framework. The differences are still present.

*Therefore be aware of the differences and be careful when you copy&paste content between JSON and robot!*

**JSON file content**

Now we take a look at the content of the JSON file. The global params section defines the dictionary ``dict_val``
step by step in the following way:

.. code::

   "dict_val" : {},
   ${params}['global']['dict_val']['key_1'] : {},
   ${params}['global']['dict_val']['key_1']['subkey_11'] : {},
   ${params}['global']['dict_val']['key_1']['subkey_11']['subsubkey_111'] : ${params}['global']['string_val'],
   ${params}['global']['dict_val']['key_1']['subkey_11']['subsubkey_112'] : ${params}['global']['int_val'],
   ${params}['global']['dict_val']['key_1']['subkey_11']['subsubkey_113'] : ${params}['global']['float_val'],
   ${params.global.dict_val.key_2} : {},
   ${params.global.dict_val.key_2.subkey_21} : {},
   ${params.global.dict_val.key_2.subkey_21.subsubkey_211} : ${params.global.bool_val_1},
   ${params.global.dict_val.key_2.subkey_21.subsubkey_212} : ${params.global.bool_val_2},
   ${params.global.dict_val.key_2.subkey_21.subsubkey_213} : ${params.global.null_val}

This is a nested dictionary - the values of keys are also dictionaries. Every dictionary (at each level)
needs to be initialized by ``{}`` before keys can be added.

In case of the dollar operator is used to refer to already existing parameters it is not necessary to wrap the expression in quotes.
If you use quotes at the right hand side of the colon, you will get values of type ``string``!

The dictionary ``dict_val`` contains two keys (``key_1`` and ``key_2``). Every key contains one single key
at the level below (``subkey_11`` and ``subkey_21``). The lowest level consists of the keys ``subsubkey_111``
to ``subsubkey_213``.

Two different types of assignments are used:

* ``key_1`` in standard dictionary notation
* ``key_2`` in alternative ``dotdict`` notation

The ``dotdict`` notation is shorter and therefore easier to read, but requires that no key name contains a dot.

To every ``subsubkey`` a scalar is assigned - and we use here the scalars (of the configuration file),
that already have been used in tutorial-01:

.. code::

   "string_val" : "test string",
   "int_val" : 123,
   "float_val" : 4.56,
   "bool_val_1" : True,
   "bool_val_2" : true,
   "bool_val_3" : False,
   "bool_val_4" : false,
   "none_val" : None,
   "null_val" : null,

Within ``tutorialconfig.jsonp`` all parameter definitions are put into the following code:

.. code::

   "params" : {
               "global": {
                          (definitions of global params)
                         }
              }

Meaning: The scope of all of these user defined parameters is: ``params:global``. In case you want to use
inside a JSON configuration file a parameter that is defined within this file also, you have to set this scope.

This is a valid assignment (containing the scope ``${params}['global']``):

.. code::

      ${params}['global']['dict_val']['key_1']['subkey_11']['subsubkey_111'] : ${params}['global']['string_val'],

For comparison: These are invalid assignments (where the scope is missing at any position):

.. code::

      ${params}['global']['dict_val']['key_1']['subkey_11']['subsubkey_111'] : ${string_val},
      ${dict_val}['key_1']['subkey_11']['subsubkey_111'] : ${params}['global']['string_val'],
      ${dict_val}['key_1']['subkey_11']['subsubkey_111'] : ${string_val},

And very important: In robot code the scope ``params:global`` is the default. In your tests you have to refer to ``subsubkey_111``
in the following way:

.. code::

   ${dict_val}[key_1][subkey_11][subsubkey_111]

**Test case content**

Test case ``03_03`` starts with the log of the entire user defined dictionary ``dict_val``.

.. code::

   log_dict    ${dict_val}

With the help of the already known keyword ``log_scalar`` we take a look at every low level key manually:

.. code::

   log_scalar    ${dict_val}[key_1][subkey_11][subsubkey_111]
   log_scalar    ${dict_val}[key_1][subkey_11][subsubkey_112]
   log_scalar    ${dict_val}[key_1][subkey_11][subsubkey_113]
   log_scalar    ${dict_val}[key_2][subkey_21][subsubkey_211]
   log_scalar    ${dict_val}[key_2][subkey_21][subsubkey_212]
   log_scalar    ${dict_val}[key_2][subkey_21][subsubkey_213]

*Be aware of: No quotes are used here around the key names. In JSON it's different: Quotes are required.*

Like in:

.. code::

   ${params}['global']['dict_val']['key_1']['subkey_11']['subsubkey_111']

Above we mentioned that in the context of the Robot Framework a dictionary is a certain one: a ``dotdict``.

The impact is:

1. Like demonstrated in the previous robot code example, the standard syntax of accessing dictionary values is still valid.
2. Alternatively it is possible to use the reduced ``dotdict`` syntax.

``dotdict`` syntax:

.. code::

   log_scalar    ${dict_val.key_1.subkey_11.subsubkey_111}
   log_scalar    ${dict_val.key_1.subkey_11.subsubkey_112}
   log_scalar    ${dict_val.key_1.subkey_11.subsubkey_113}
   log_scalar    ${dict_val.key_2.subkey_21.subsubkey_211}
   log_scalar    ${dict_val.key_2.subkey_21.subsubkey_212}
   log_scalar    ${dict_val.key_2.subkey_21.subsubkey_213}

But this notation requires that the key names do not contain dots. In case they do, you have to switch back to the standard notation.

Up to now we have used hard coded strings as key names. The last step in this tutorial is to use the content of variables as key names.

The following key name variables are defined:

.. code::

   Set Test Variable    ${key}    key_1
   Set Test Variable    ${subkey}    subkey_11
   Set Test Variable    ${subsubkey}    subsubkey_111

**Summary**

The following ways of accessing a dictionary value are possible in robot code:

.. code::

   log_scalar    ${dict_val}[key_1][subkey_11][subsubkey_111]
   log_scalar    ${dict_val.key_1.subkey_11.subsubkey_111}
   log_scalar    ${dict_val['key_1']['subkey_11']['subsubkey_111']}
   log_scalar    ${dict_val}[${key}][${subkey}][${subsubkey}]
   log_scalar    ${dict_val['${key}']['${subkey}']['${subsubkey}']}


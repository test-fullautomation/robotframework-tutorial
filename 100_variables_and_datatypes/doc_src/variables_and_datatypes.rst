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

Variables and datatypes in Robot Framework
==========================================

Version 0.2.1 / 07.09.2022 / by XC-CT/ECA3-Queckenstedt

Table of content
----------------

| `Introduction`_
| `Tutorial files`_

Introduction
------------

The Robot Framework supports several types of variables and variables can be defined at several positions.

These are the types:

* scalar
* list
* dictionary

These are the positions:

* command line
* ``Variable`` section of test file
* imported resource file
* imported variable file
* during test execution
* json configuration file (RobotFramework AIO addon)

This part of the tutorial contains examples that demonstrate how to handle the definition of variables and how to access them.

We also take a look behind the curtain to observe what happen with the data types of variables depending on the way they are handled and defined.

For this we use a Python based keyword library of this tutorial, that prints informations like type and content of a given variable to console.

The names of the robot files of this tutorial are ``tutorial-01``, ``tutorial-02``, ``tutorial-03`` ... The content of every robot file is explained
in more detail in a HTML file with same name.

Most of the robot files can be executed directly. But some of them require command line extensions. Therefore this tutorial contains for all robot files
a command line that demonstates how to execute the file.

All command lines let the Robot Framework save the log files in a local ``logfiles`` folder within this tutorial.

The syntax of all command lines belong to Windows. In case you work with this tutorial under Linux you have to modify the way, environment variables are accessed:

* ``%RobotPythonPath%`` under Windows
* ``${RobotPythonPath}`` under Linux

For best results while working with this tutorial, a basic knowledge of Robot Framework is recommended.

It is also recommended to explore the tutorial files in the order of their numbers.

A lot of things can go wrong in all examples of this tutorial (e.g. missing quotes, too much quotes, wrong operators, missing keywords like ``Evaluate``, and so on).
Not all of these things cause syntax errors immediately. But if it's not a syntax issue, there will be no direct feedback in form of an error message.
Only the result of the test execution is not like expected.

It is not the intention of this tutorial to go through all possible error scenarios while working with variables. We concentrate here on *what works*. And the way
we do it, might also not be the *only* way to do it in a proper way.

TOC_


Tutorial files
--------------

* ``config/tutorialconfig.json``

  Json configuration file containing the definition of some test variables

* ``libs/testimport.resource``

  Resource file containing the definition of some test variables

* ``libs/arguments.robot``

  Arguments file containing the definition of some test variables

* ``libs/testlibrary.py``

  Python based keyword library containing some test keywords to support this tutorial

* ``tutorial-01.robot``

  Tutorial file to handle scalars

* ``tutorial-02.robot``

  Tutorial file to handle lists

* ``tutorial-03.robot``

  Tutorial file to handle dictionaries


TOC_

.. _TOC: `Table of content`_

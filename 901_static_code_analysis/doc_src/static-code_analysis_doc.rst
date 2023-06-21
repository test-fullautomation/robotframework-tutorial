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

Static code analysis in Robot Framework
=======================================

Version 0.2.1 / 21.06.2023 / by XC-CT/ECA3-Queckenstedt

Table of content
----------------

| `Tutorial main sections <https://htmlpreview.github.io/?https://github.com/test-fullautomation/robotframework-tutorial/blob/develop/robot_framework_tutorial.html>`_

| `Introduction`_
| `Configuration`_
| `Tutorial files`_

Introduction
------------

Robot Framework sources are present in robot files (``.robot``) and in resource files (``.resource``). The maturity of these files can be checked
by a static code analyser called Robocop.

Robocop is integrated in Visual Studio Code and and is triggered automatically in case of

1. a file is opened in editor,
2. a file is changed and saved.

The results of the check are listed in the PROBLEMS window of Visual Studio Code:

.. image:: ./doc_src/images/ProblemsWindow.png

A left click on a findings line opens the affected file at the position of the finding. Every result also contains the id of the rule that causes the finding.
The id (colored in blue) is a link to the documentation of the rule in the web:

.. image:: ./doc_src/images/ProblemsWindow2.png

Warnings are indicated by a dark orange symbol, errors are indicated by a red symbol at the beginning of a findings line:

.. image:: ./doc_src/images/ProblemsWindow3.png

The same color code is used within the Explorer:

.. image:: ./doc_src/images/Explorer.png


Caution: Robocop does not consider imports! If a robot file is checked and this robot file imports a resource file, then this resource file
is *not* also checked. The resource file has to be opened separately.


TOC_


Configuration
-------------

Robocop can be configured by a ``.robocop`` file that has to be placed within the project folder. The ``.robocop`` file within this tutorial excludes some checks,
that are not really helpful or against internal coding conventions.

The file also contains some parameter values belonging to rules, that can be modified. The currently used values are the default values.


TOC_



Tutorial files
--------------

This tutorial contains two robot files (``suite01.robot`` and ``suite01.robot``) and one resource file (``testimport.resource``).

Open the files in Visual Studio Code and let Robocop list all the findings inside.

TOC_

.. _TOC: `Table of content`_


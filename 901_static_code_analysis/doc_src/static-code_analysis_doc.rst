.. Copyright 2020-2022 Robert Bosch Car Multimedia GmbH

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

   http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.

Static code analysis in Robotframework
======================================

Version 0.1.0 / 05.08.2021 / by XC-CI1/ECA3-Queckenstedt

Table of content
----------------

| `Introduction`_
| `Executing Robocop`_
| `Preconfigured settings`_
| `Output`_
| `Additional hints`_
| `Tutorial files`_

Introduction
------------

Robotframework sources are present in robot files (``.robot``) and in resource files (``.resource``). The maturity of these files can be checked
by a static code analyser called Robocop.

Robocop is integrated in Eclipse and can be accessed by the External Tools menu.

It is possible to check a single file only and it is also possible to check complete folders. In case of a folder is checked, Robocop searches
within this folder recursively for robot and resource files.

Caution: Robocop does not consider imports! If a single robot file is checked and this robot file imports a resource file, then this resource file
is *not* also checked. The resource file has to be selected separately.

TOC_

Executing Robocop
-----------------

1. In Eclipse Project Explorer select a single Robotframework file or a folder.

2. Open the External Tools menu and select one of the listed items belonging to Robocop. Currently available are the following preconfigured settings:

   .. image:: ./doc_src/images/RCExtToolsMenu.png

   **RF SCAn** is the abbreviation for **R**\ obot\ **F**\ ramework **S**\ tatic **C**\ ode **An**\ alysis.

   The results of the execution are available either within the Eclipse console window or within a separate log file
   (depending on the selected item, for details see `Preconfigured settings`_).

TOC_


Preconfigured settings
----------------------

**RF SCAn (console)**

   * Robocop executes a relevant subset of available checks (some checks that are not really helpful or against internal coding conventions, are excluded).

   * The output of Robocop is listed within the Eclipse console window.

   * The advantage of the console window is that every finding is a link to the position at which the finding occurs.
     A double click on the link causes the Red editor to open the affected file at this position.

**RF SCAn (log file)**

   * Robocop executes a relevant subset of available checks (some checks that are not really helpful or against internal coding conventions, are excluded).

   * The output of Robocop is written to the following log file: ``%ROBOTLOGPATH%\Robocop.log``

   * This option is mostly for documentation purposes.

**TODO list (console)**

   * Robocop executes only a single check that searches for the string ``TODO`` within comment blocks.

   * The idea behind this is: Every developer who needs a reminder about what still has to be done before the next release,
     uses the ``TODO`` string to mark the corresponding position in the code. Before a release this check tells if all things are done
     or if something has been forgotten.

   * Therefore the ``TODO`` string inside code comments should be used for developer internal communication and not to give common hints
     to customer. A released code should not contain any ``TODO`` strings any more, except a good reason is added why it is not possible
     to resolve the TODO.

TOC_


Output
------

The output of Robocop is the same in console and in log file, and consists of two parts:

**Part 1: A list of findings**

Every line within the list is a finding. Every finding contains the following informations:

1. Path and name of file in which the finding occurred
2. Line number
3. Column number
4. Type of finding (error, warning or info; represented by one capital letter in squared brackets)
5. ID of the Robocop internal rule behind the finding
6. Short description of the rule
7. Short name of the rule (single string in round brackets)

Example:

.. image:: ./doc_src/images/ConsoleList.png


**Part 2: A final statistic**

The final statistic tells how often every type of finding has been found in the entire checked code, sorted by the number of occurrances.

Example:

.. image:: ./doc_src/images/ConsoleStatistics.png

TOC_


Additional hints
----------------

The output of Robocop starts with a ``DEPRECATION WARNING``. This warning informs about changes between the current version and the previous version of Robocop
and can be ignored.

TOC_


Tutorial files
--------------

The files within this tutorial show some examples for Robocop findings.

* Findings in file ``suite01.robot``

  * *Warning 0203 : Missing documentation in suite*

    Tells that the documentation of the suite is missing.

  * *Warning 1003 : Invalid number of empty lines between sections (1/2)*

    Within ``suite01.robot`` there is only one blank line between the end of the ``*** Settings ***`` section and the ``*** Test Cases ***`` section.

    .. image:: ./doc_src/images/InvalidNumberOfEmptyLines.png

    To ease the readability of the code Robocop wants to have exactly two blank lines between sections.

  * *Warning 0202 : Missing documentation in test case*

    Tells that the documentation of the test case is missing.

* Findings in file ``suite02.robot``

  * *Error 0801 : Multiple test cases with name "Test Case 0201" in suite*

    Accidently two tests inside the suite have the same name. This error is listed multiple times (every single occurrance of the same name is a separate finding).

    .. image:: ./doc_src/images/MultipleTestCases.png

    Test names must be unique.

  * *Warning 0701 : Found TODO in comment*

    A ``TODO`` marker indicates that still something is to do in the code.

    .. image:: ./doc_src/images/ToDo.png

    A ``TODO`` marker needs to have an own line and must not be placed at the end of a line containing code!

  * *Warning 1010 : Too many blank lines at the end of file*

    .. image:: ./doc_src/images/BlankLinesAtEndOfFile.png

    Only one blank line is expected at the end of a file.

* Findings in file ``testimport.resource``

  * *Warning 1001 : Trailing whitespace at the end of line*

    Tells that there is additional whitespace (here: 4 blanks) at the end of the line.

    .. image:: ./doc_src/images/TrailingWhitespace.png

    No additional whitespace is expected at the end of a line.
  
**Summary:**

Checking the complete Robocop tutorial section causes the following list of findings (the file paths are shortened):

| ``libs/testimport.resource:9:65 [W] 1001 Trailing whitespace at the end of line (trailing-whitespace)``
| ``suite01.robot:1:0 [W] 0203 Missing documentation in suite (missing-doc-suite)``
| ``suite01.robot:10:0 [W] 1003 Invalid number of empty lines between sections (1/2) (empty-lines-between-sections)``
| ``suite01.robot:12:0 [W] 0202 Missing documentation in test case (missing-doc-test-case)``
| ``suite02.robot:18:0 [E] 0801 Multiple test cases with name "Test Case 0201" in suite (duplicated-test-case)``
| ``suite02.robot:21:4 [W] 0701 Found TODO in comment (todo-in-comment)``
| ``suite02.robot:24:0 [E] 0801 Multiple test cases with name "Test Case 0201" in suite (duplicated-test-case)``
| ``suite02.robot:30:0 [W] 1010 Too many blank lines at the end of file (too-many-trailing-blank-lines)``
| 
| ``Processed 3 file(s) from which 3 file(s) contained issues``

TOC_


.. _TOC: `Table of content`_


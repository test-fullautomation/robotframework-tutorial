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

Building testsuites in RobotFrameowork AIO
==========================================

Version 0.1.0 / 25.10.2022 / by MS/EMC1-XC Mai Dinh Nam Son

Table of content
----------------

| `Introduction`_
| `Tutorial files`_

Introduction
------------

The RobotFramework AIO supports configuration files with Json format and 4 configuration levels 
with different prority for various purpose during using RobotFramework AIO to create automation 
testing project.

The json configuration files is handled by `JsonPreprocessor package <https://github.com/test-fullautomation/python-jsonpreprocessor>`_ 
which is embbeded into RobotFrameowork AIO installation package:

* Adding the comments to the json configuration file is allowed.
* Import the content of another json files.
* Allow python datatypes ``True``, ``False`` and ``None`` as json syntax elements.
* Be able to use nested variable.

The RobotFramework AIO defines 4 different configuration levels, from level 1 -> level 4, where Level 1 
is highest priority and level 4 is lowest priority:

**Level 1: Loads configuration file while executing robot testsuite by command**

User can address the json configuration file when executing robot testsuite with input parameter 
``--variable config_file:"<path_to_json_file>"``

Ex: ``robot --variable config_file:"<path_to_json_file>" <path_to_testsuite>``

**Level 2: Loads Json configuration according to variant name**

This level 2 is designed for the scenario that user creates the automation testing project which running 
for many different variants. Base on variant name input when trigger robot run, it will load the appropriate 
json configuration file.

To set RobotFrameowork AIO run with level 2, first user has to create a json file which contains different 
variants point to different configuration files.

For example, we create the ``variants_cfg.json`` with content below:

.. code-block:: json

   {
     "default": {
       "name": "<default_cfg_file>",
       "path": "<path>"
     },
     "variant_0": {
       "name": "<file_name_variant_0>",
       "path": "<path>"
     },
     "variant_1": {
       "name": "<file_name_variant_1>",
       "path": "<path>"
     },
     "variant_2": {
       "name": "<file_name_variant_2>",
       "path": "<path>"
     }
   }

Then the path of ``variants_cfg.json`` file has to add as input parameter of ``testsuites.testsuite_setup`` 
in ``Suite Setup`` of a testsuite.

In case of user wants to set configuration level 2 for entire RobotFrameowork test project instead of 
indiviual robot testsuite file, ``__init__.robot`` file has to be created at the highest folder of 
RobotFrameowork test project, and the path of ``variants_cfg.json`` file has to add as input parameter of 
``testsuites.testsuite_setup`` in ``Suite Setup`` of the ``__init__.robot`` file.

.. code-block::

   *** Settings ***
   Library      RobotFramework_Testsuites    WITH NAME    testsuites
   Suite Setup      testsuites.testsuite_setup    <Path_to_the_file_variants_cfg.json>

**Level 3: Find the ``config/`` folder in current testsuite directory**

Configuration level 3 is triggered only in case of level 1 and level 2 were not set.

The configuration level 3 will check in ``config/`` folder in current testsuite directory, if there has json 
file which has the same name with testsuite file (ex: ``abc.rotbot`` & ``./config/abc.json``), then it will 
load this configuration file. In case there is no json file has the same name with robot testsuite file, it will 
check the existence of ``./config/robot_config.json`` then load this ``./config/robot_config.json`` file as 
configuration file.  

**Level 4: Lowest priority level, it reads default configuration file**

The default configuration file (``robot_config.json``) in installation directory:

``\RobotFramework_Testsuites\Config\robot_config.json``

TOC_


Tutorial files
--------------

* ``config\common\test_config_common.json``
  
  Json configuration file containing common parameters which are stored ``${CONFIG}`` object. This Json file is 
  imported to the main json configuration file.

* ``config\common\preprocessor_definitions_common.json``

  Json configuration file containing preprocessor parameters which are set as global variable of robot run, we 
  can call these parameters in robot test script using ``${<parameter_name>}``. This json configuration file is 
  imported to the main json configuration file in ``"preprocessor" { "definitions" : {...} }``.

* ``config\common\params_global_common.json``

  Json configuration file containing global parameters which are set as global variable of robot run, we 
  can call these parameters in robot test script using ``${<parameter_name>}``. This json configuration file is 
  imported to the main json configuration file in ``"params" { "global" : {...} }``.

* ``config\robot_config_noimport.json``

  This is the main json configuration file without the import for ``preprocessor definitions`` and ``params global``

* ``config\robot_config_variant_1.json``

  This is the main json configuration file for variant with name ``variant_1``.

* ``config\robot_config_variant_2.json``

  This is the main json configuration file for variant with name ``variant_2``.

* ``config\robot_execution_config.json``

  This is the main json configuration file in case variant name is not set or default.

* ``config\testsuites_config.json``

  This is the json configuration file uses for configuration level 2 only, it contains the path to the main 
  configuration file appropriate with variant name is set while executing robot run.

* ``components\suite01.robot``

  This is robot test script which is using configuration level 2 with default variant. It will load the main 
  configuration file ``config\robot_execution_config.json``.

* ``components\suite02.robot``

  This is robot test script which is using configuration level 2 with variant name ``variant_2``. it will 
  load the main configuration file ``config\robot_config_variant_2.json``.

* ``components\__init__.robot``

  This ``__init__.robot`` robot test script using to set configuration level 2 when we execute all testsuites 
  in ``components`` with default variant. In this case, ``components`` robot run will load the main configuration 
  file ``config\robot_execution_config.json``.

* ``components\component_A\suite03.robot``

  This is robot test script which using configuration level 2 with default variant. It will load the main 
  configuration file ``config\robot_execution_config.json``. 

  This test script logs out some parameters in ``config\common\test_config_common.json`` via ``${CONFIG}`` 
  object, and parameters in ``config\common\params_global_common.json`` and ``config\common\preprocessor_definitions_common.json``.

* ``components\component_B\config\suite04.json``

  This is the main json configuration file which using for ``components\component_B\suite04.robot`` robot test script using 
  configuration level 3.

* ``components\component_B\config\robot_config.json``

  This is the main json configuration file which using for ``components\component_B\suite05.robot`` robot test script using 
  configuration level 3.

* ``components\component_B\suite04.robot``

  Robot test script using configuration level 3 with the main json configuration file ``components\component_B\config\suite04.json``.

* ``components\component_B\suite05.robot``

  Robot test script using configuration level 3 with the main json configuration file ``components\component_B\config\robot_config.json``.

* ``components\component_C\config\robot_config_B.json`` and ``components\component_C\config\suite.json``

  These json configuration files are named with invalid naming convention which is defined in configuration level 3, 
  so the robot test script ``components\component_C\suite06.robot`` will use configuration level 4 with the default main 
  json configuration file ``\RobotFramework_Testsuites\Config\robot_config.json``.

* ``components\component_C\suite06.robot``

  Robot test script using configuration level 4 with the default json configuration file ``\RobotFramework_Testsuites\Config\robot_config.json``.


TOC_

.. _TOC: `Table of content`_
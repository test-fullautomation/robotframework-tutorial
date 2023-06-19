#  Copyright 2020-2023 Robert Bosch GmbH
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
#################################################################################

# -- import standard Python modules
import pickle, os, time, random

# -- import Robotframework API
from robot.api.deco import keyword, library # required when using @keyword, @library decorators
from robot.libraries.BuiltIn import BuiltIn

from PythonExtensionsCollection.String.CString import CString
from PythonExtensionsCollection.Utils.CUtils import *

# --------------------------------------------------------------------------------------------------------------

sThisModuleName    = "testlibrary.py"
sThisModuleVersion = "0.1.0"
sThisModuleDate    = "05.09.2022"
sThisModule        = f"{sThisModuleName} v. {sThisModuleVersion} / {sThisModuleDate}"

# --------------------------------------------------------------------------------------------------------------
#
@library
class testlibrary():
   """ generic system methods
   """

   ROBOT_AUTO_KEYWORDS   = False # only decorated methods are keywords
   ROBOT_LIBRARY_VERSION = sThisModuleVersion
   ROBOT_LIBRARY_SCOPE   = 'GLOBAL'

   # --------------------------------------------------------------------------------------------------------------
   #TM***

   def __init__(self, sThisModule=sThisModule):

      self.__sThisModule = sThisModule

   def __del__(self):
       pass

   # --------------------------------------------------------------------------------------------------------------
   #TM***

   @keyword
   def log_scalar(self, param=None):
      """Logs the value and the type of the given parameter 'param'
         (assuming that param is a scalar)
      """
      scalar_value = str(param)
      scalar_type  = str(type(param))
      BuiltIn().log(f"+ value: '{scalar_value}' / type: {scalar_type}", "INFO", console=True)

      return True
   # eof def log_scalar(self, param=None):

   # --------------------------------------------------------------------------------------------------------------

   @keyword
   def log_list(self, param=None):
      """Logs the value and the type of every element of the given parameter 'param'
         (assuming that param is a list)
      """
      for element in param:
         elem_value = str(element)
         elem_type  = str(type(element))
         BuiltIn().log(f"+ value: '{elem_value}' / type: {elem_type}", "INFO", console=True)

      return True

   # eof def log_list(self, param=None):

   # --------------------------------------------------------------------------------------------------------------

   @keyword
   def log_dict(self, param=None):
      """Logs the value and the type of every key of the given parameter 'param'
         (assuming that param is a dictionary)
      """
      for key in param:
         key_value = str(param[key])
         key_type  = str(type(param[key]))
         BuiltIn().log(f"+ key: '{key}' / value: '{key_value}' / type: {key_type}", "INFO", console=True)

      return True

   # eof def log_dict(self, param=None):

   # --------------------------------------------------------------------------------------------------------------

# eof class testlibrary():


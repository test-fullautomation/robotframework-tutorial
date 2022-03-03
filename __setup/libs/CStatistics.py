# **************************************************************************************************************
#
#  Copyright 2020-2022 Robert Bosch GmbH
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
#
# **************************************************************************************************************
#
# CStatistics.py
#
# XC-CT/ECA3-Queckenstedt
#
# Initial version 02/2022
#
# --------------------------------------------------------------------------------------------------------------

import os, sys, platform
import colorama as col
import pypandoc

from PythonExtensionsCollection.String.CString import CString

col.init(autoreset=True)
COLBR = col.Style.BRIGHT + col.Fore.RED
COLBG = col.Style.BRIGHT + col.Fore.GREEN

# --------------------------------------------------------------------------------------------------------------

class CStatistics():

   def __init__(self):
      self.__nCntInternalErrors                     = 0
      self.__nCntSections                           = 0
      self.__nCntInputFiles                         = 0
      self.__nCntOutputFilesExisting                = 0
      self.__nCntOutputFilesNotExisting             = 0
      self.__nCntConverterReturnedNotZero           = 0
      self.__listInputFilesConverterReturnedNotZero = []
      self.__listOutputFilesNotCreated              = []

   def __del__(self):
      del self.__nCntInternalErrors
      del self.__nCntSections
      del self.__nCntInputFiles
      del self.__nCntOutputFilesExisting
      del self.__nCntOutputFilesNotExisting
      del self.__nCntConverterReturnedNotZero
      del self.__listInputFilesConverterReturnedNotZero
      del self.__listOutputFilesNotCreated

   # -- count internal errors
   def IncCntInternalErrors(self, nDigits=0):
      self.__nCntInternalErrors = self.__nCntInternalErrors + 1
      return self.GetCntInternalErrors(nDigits)

   def GetCntInternalErrors(self, nDigits=0):
      if nDigits == 0:
         return self.__nCntInternalErrors
      else:
         return str(self.__nCntInternalErrors).rjust(nDigits,'0')

   # -- count sections
   def IncCntSections(self, nDigits=0):
      self.__nCntSections = self.__nCntSections + 1
      return self.GetCntSections(nDigits)

   def GetCntSections(self, nDigits=0):
      if nDigits == 0:
         return self.__nCntSections
      else:
         return str(self.__nCntSections).rjust(nDigits,'0')

   # -- count input files
   def IncCntInputFiles(self, nDigits=0):
      self.__nCntInputFiles = self.__nCntInputFiles + 1
      return self.GetCntInputFiles(nDigits)

   def GetCntInputFiles(self, nDigits=0):
      if nDigits == 0:
         return self.__nCntInputFiles
      else:
         return str(self.__nCntInputFiles).rjust(nDigits,'0')

   # -- count existing output files
   def IncCntOutputFilesExisting(self, nDigits=0):
      self.__nCntOutputFilesExisting = self.__nCntOutputFilesExisting + 1
      return self.GetCntOutputFilesExisting(nDigits)

   def GetCntOutputFilesExisting(self, nDigits=0):
      if nDigits == 0:
         return self.__nCntOutputFilesExisting
      else:
         return str(self.__nCntOutputFilesExisting).rjust(nDigits,'0')

   # -- count not existing output files
   def IncCntOutputFilesNotExisting(self, nDigits=0):
      self.__nCntOutputFilesNotExisting = self.__nCntOutputFilesNotExisting + 1
      return self.GetCntOutputFilesNotExisting(nDigits)

   def GetCntOutputFilesNotExisting(self, nDigits=0):
      if nDigits == 0:
         return self.__nCntOutputFilesNotExisting
      else:
         return str(self.__nCntOutputFilesNotExisting).rjust(nDigits,'0')

   # -- count files for converter returned a value != 0
   def IncCntConverterReturnedNotZero(self, nDigits=0):
      self.__nCntConverterReturnedNotZero = self.__nCntConverterReturnedNotZero + 1
      return self.GetCntConverterReturnedNotZero(nDigits)

   def GetCntConverterReturnedNotZero(self, nDigits=0):
      if nDigits == 0:
         return self.__nCntConverterReturnedNotZero
      else:
         return str(self.__nCntConverterReturnedNotZero).rjust(nDigits,'0')

   # -- list of input files for converter returned a values != 0
   def AppendFileForConverterReturnedNotZero(self, sFile=None):
      self.__listInputFilesConverterReturnedNotZero.append(str(sFile))

   def GetFileListForConverterReturnedNotZero(self):
      return self.__listInputFilesConverterReturnedNotZero

   # -- list of (possible) output files that are not created
   def AppendOutputFileNotCreated(self, sFile=None):
      self.__listOutputFilesNotCreated.append(str(sFile))

   def GetListOfOutputFilesNotCreated(self):
      return self.__listOutputFilesNotCreated

# eof class CStatistics():

# --------------------------------------------------------------------------------------------------------------

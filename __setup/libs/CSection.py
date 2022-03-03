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
# CSection.py
#
# XC-CT/ECA3-Queckenstedt
#
# Initial version 02/2022
#
# --------------------------------------------------------------------------------------------------------------

import os, sys
import colorama as col

from PythonExtensionsCollection.String.CString import CString

col.init(autoreset=True)
COLBR = col.Style.BRIGHT + col.Fore.RED
COLBG = col.Style.BRIGHT + col.Fore.GREEN

# --------------------------------------------------------------------------------------------------------------

class CSection():

   def __init__(self, sSectionRootPath=None, oRepositoryConfig=None, oStatistics=None):

      sMethod = "CSection.__init__"

      if sSectionRootPath is None:
         bSuccess = None
         sResult  = "sSectionRootPath is None"
         raise Exception(CString.FormatResult(sMethod, bSuccess, sResult))

      if oRepositoryConfig is None:
         bSuccess = None
         sResult  = "oRepositoryConfig is None"
         raise Exception(CString.FormatResult(sMethod, bSuccess, sResult))

      if oStatistics is None:
         bSuccess = None
         sResult  = "oStatistics is None"
         raise Exception(CString.FormatResult(sMethod, bSuccess, sResult))

      self.__sSectionRootPath  = sSectionRootPath
      self.__oRepositoryConfig = oRepositoryConfig
      self.__oStatistics       = oStatistics

      self.__oRepositoryConfig.Set("sSectionRootPath", self.__sSectionRootPath)

   def __del__(self):
      pass

   def GetDocumentsList(self):

      sMethod = "GetDocumentsList"

      tupleSupportedFileExtensions = (".robot", ".resource", ".rst", ".py")

      listDocuments = []
      bSuccess      = None
      sResult       = None

      for sLocalRootPath, listFolderNames, listFileNames in os.walk(self.__sSectionRootPath):
         for sFileName in listFileNames:
            bFileSupported = False
            for sExtension in tupleSupportedFileExtensions:
               if sFileName.lower().endswith(sExtension):
                  bFileSupported = True
                  break
            if bFileSupported is True:
               sDocument = CString.NormalizePath(os.path.join(sLocalRootPath, sFileName))
               listDocuments.append(sDocument)
         # eof for sFileName in listFileNames:
      # eof for sLocalRootPath, listFolderNames, listFileNames in os.walk(self.__sSectionRootPath):

      listDocuments.sort()
      nNrOfDocuments = len(listDocuments)

      bSuccess = True
      sResult  = f"Found {nNrOfDocuments} tutorial documents within '{self.__sSectionRootPath}'"

      return listDocuments, bSuccess, CString.FormatResult(sMethod, bSuccess, sResult)

# eof class CSection():

# --------------------------------------------------------------------------------------------------------------

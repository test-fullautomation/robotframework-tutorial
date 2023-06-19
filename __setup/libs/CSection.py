# **************************************************************************************************************
#
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
#
# **************************************************************************************************************
#
# CSection.py
#
# XC-CT/ECA3-Queckenstedt
#
# 20.01.2023
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

      self.__listRstFiles      = []
      self.__dictTutorialFiles = {}

      self.__oRepositoryConfig.Set("dictTutorialFiles", self.__dictTutorialFiles)

   def __del__(self):
      pass

   # --------------------------------------------------------------------------------------------------------------
   def GetDocumentsList(self):
      """Computes a list of documents within a tutorial section.
      """

      sMethod = "GetDocumentsList"

      tupleSupportedFileExtensions = (".rst", ".robot", ".resource", ".py", ".json")

      bSuccess = None
      sResult  = None

      for sLocalRootPath, listFolderNames, listFileNames in os.walk(self.__sSectionRootPath):
         for sFileName in listFileNames:
            bFileSupported = False
            for sExtension in tupleSupportedFileExtensions:
               if sFileName.lower().endswith(sExtension):
                  bFileSupported = True
                  break
            if bFileSupported is True:
               sFile = CString.NormalizePath(os.path.join(sLocalRootPath, sFileName))
               if sFileName.lower().endswith('.rst'):
                  self.__listRstFiles.append(sFile)
               else:
                  # duplicate check
                  if sFileName in self.__dictTutorialFiles:
                     # File with same name previously found in this tutorial section.
                     # Such ambiguous files cannot be documented, because as per tutorial documentation concept
                     # we need a 1x1 naming relationship between documentation files in RST format and tutorial files.
                     # But this also means that duplicate file names only cause a problem in case of such a file shall be documented.
                     # As long as no corresponding RST file is found, there is no problem. Therefore we do not stop here, but we mark
                     # the file with ambiguous name with None. Later, when both file lists are completed and we start rendering the
                     # html files, then we check against None and we throw an error in case we have a match between an RST file
                     # and a tutorial file with path None.
                     self.__dictTutorialFiles[sFileName] = None
                  else:
                     self.__dictTutorialFiles[sFileName] = sLocalRootPath
            # eof if bFileSupported is True:
         # eof for sFileName in listFileNames:
      # eof for sLocalRootPath, listFolderNames, listFileNames in os.walk(self.__sSectionRootPath):

      self.__oRepositoryConfig.Set("dictTutorialFiles", self.__dictTutorialFiles)

      self.__listRstFiles.sort()
      nNrOfRstFiles = len(self.__listRstFiles)

      bSuccess = True
      sResult  = f"Found {nNrOfRstFiles} tutorial rst files within '{self.__sSectionRootPath}'"

      return self.__listRstFiles, bSuccess, CString.FormatResult(sMethod, bSuccess, sResult)

   # --------------------------------------------------------------------------------------------------------------
   def DumpSectionFileList(self, oLogfile=None):
      """Dumps the list of all files within the current tutorial section to log file
      """

      if oLogfile is not None:
         oLogfile.Append("                                                RST FILES")
         oLogfile.Append()

         for sRstFile in self.__listRstFiles:
            oLogfile.Append(f"* '{sRstFile}'")

         oLogfile.Append()
         oLogfile.Append(120*"=")
         oLogfile.Append()
         oLogfile.Append("                                                TUTORIAL SECTION FILES")
         oLogfile.Append()
         oLogfile.Append("                  (either all files or subset of files detected until a duplicate has been found)")
         oLogfile.Append()

         for sTutorialFileName in self.__dictTutorialFiles:
            sTutorialFilePath = self.__dictTutorialFiles[sTutorialFileName]
            sTutorialFile = CString.NormalizePath(os.path.join(sTutorialFilePath, sTutorialFileName))
            oLogfile.Append(f"* '{sTutorialFile}'")

# eof class CSection():

# --------------------------------------------------------------------------------------------------------------

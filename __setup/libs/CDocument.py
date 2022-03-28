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
# CDocument.py
#
# XC-CT/ECA3-Queckenstedt
#
# 28.03.2022
#
# --------------------------------------------------------------------------------------------------------------

import os, sys, shlex, subprocess
import colorama as col

from PythonExtensionsCollection.String.CString import CString
from PythonExtensionsCollection.File.CFile import CFile

col.init(autoreset=True)
COLBR = col.Style.BRIGHT + col.Fore.RED
COLBG = col.Style.BRIGHT + col.Fore.GREEN
COLBY = col.Style.BRIGHT + col.Fore.YELLOW

# --------------------------------------------------------------------------------------------------------------

class CDocument():

   def __init__(self, sDocument=None, oRepositoryConfig=None, oStatistics=None):

      sMethod = "CDocument.__init__"

      if sDocument is None:
         bSuccess = None
         sResult  = "sDocument is None"
         raise Exception(CString.FormatResult(sMethod, bSuccess, sResult))

      if oRepositoryConfig is None:
         bSuccess = None
         sResult  = "oRepositoryConfig is None"
         raise Exception(CString.FormatResult(sMethod, bSuccess, sResult))

      if oStatistics is None:
         bSuccess = None
         sResult  = "oStatistics is None"
         raise Exception(CString.FormatResult(sMethod, bSuccess, sResult))

      if not sDocument.lower().endswith(".rst"):
         bSuccess = None
         sResult  = f"File with unsupported extension given: '{self.__sDocument}'"
         raise Exception(CString.FormatResult(sMethod, bSuccess, sResult))

      self.__sDocument         = sDocument
      self.__oRepositoryConfig = oRepositoryConfig
      self.__oStatistics       = oStatistics

   def __del__(self):
      pass

   def Convert(self):
      """Converts an rst file to HTML format
      """

      sMethod = "Convert"

      bConverterIssue = False

      bSuccess        = None
      sResult         = "Result UNKNOWN"

      sSectionRootPath  = self.__oRepositoryConfig.Get('sSectionRootPath')
      dictTutorialFiles = self.__oRepositoryConfig.Get('dictTutorialFiles')

      listCmdLineParts = []

      # -- computing path and name of destination file
      sDstFile = None
      sSrcFile = self.__sDocument
      oSrcFile = CFile(sSrcFile)
      dSrcFileInfo = oSrcFile.GetFileInfo()
      sSrcFileNameOnly = dSrcFileInfo['sFileNameOnly'] # => without extension '.rst'
      if sSrcFileNameOnly in dictTutorialFiles:
         # counterpart available
         sDstFilePath = dictTutorialFiles[sSrcFileNameOnly]
         sDstFile = f"{sDstFilePath}/{sSrcFileNameOnly}.html"
      else:
         # no counterpart available => standalone rst file
         sDstFile = f"{sSectionRootPath}/{sSrcFileNameOnly}.html"

      # -- preparing command line
      sPython = self.__oRepositoryConfig.Get('sPython')
      sRST2HTML = self.__oRepositoryConfig.Get('sRST2HTML')
      listCmdLineParts.append(f"\"{sPython}\"")
      listCmdLineParts.append(f"\"{sRST2HTML}\"")
      listCmdLineParts.append("--input-encoding=\"utf-8\"")
      listCmdLineParts.append("--output-encoding=\"utf-8\"")
      listCmdLineParts.append(f"\"{sSrcFile}\"")
      listCmdLineParts.append(f"\"{sDstFile}\"")

      # -- executing command line

      print(f"* converting '{sSrcFile}'")

      self.__oStatistics.IncCntInputFiles()

      sCmdLine = " ".join(listCmdLineParts)
      del listCmdLineParts
      listCmdLineParts = shlex.split(sCmdLine)
      ## -- debug
      ## sCmdLine = " ".join(listCmdLineParts)
      ## print("Now executing command line:\n" + sCmdLine + "\n")

      try:
         nReturn = subprocess.call(listCmdLineParts)
         if nReturn == 0:
            bSuccess = True
            sResult  = f"File '{self.__sDocument}' converted"
         else:
            bSuccess = True # Not handled as error here because we do not want to quit this script for such a reason.
                            # Instead of this we want to continue the computation with the next file.
            bConverterIssue = True
            sResult = f"Caution: Converter returned value != 0 : {nReturn} for file '{self.__sDocument}'."
            self.__oStatistics.IncCntConverterReturnedNotZero()
            self.__oStatistics.AppendFileForConverterReturnedNotZero(self.__sDocument)
      except Exception as ex:
         bSuccess = None
         sResult  = str(ex)

      # -- checking the outcome
      if sDstFile is None: # (paranoia)
         bSuccess = None
         sResult  = "sDstFile is None"
         self.__oStatistics.IncCntInternalErrors()
      else:
         if os.path.isfile(sDstFile) is True:
            self.__oStatistics.IncCntOutputFilesExisting()
         else:
            self.__oStatistics.IncCntOutputFilesNotExisting()
            self.__oStatistics.AppendOutputFileNotCreated(sDstFile)

      return bConverterIssue, bSuccess, CString.FormatResult(sMethod, bSuccess, sResult)

# eof class CDocument():

# --------------------------------------------------------------------------------------------------------------

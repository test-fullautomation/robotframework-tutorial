#  Copyright 2020-2022 Robert Bosch Car Multimedia GmbH
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
# **************************************************************************************************************
#
#  Copyright 2020-2022 Robert Bosch Car Multimedia GmbH
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
# CTutorial.py
#
# XC-CT/ECA3-Queckenstedt
#
# Initial version 02/2022
#
# --------------------------------------------------------------------------------------------------------------

import os, sys
import colorama as col
import pypandoc

from PythonExtensionsCollection.String.CString import CString
from PythonExtensionsCollection.File.CFile import CFile

col.init(autoreset=True)
COLBR = col.Style.BRIGHT + col.Fore.RED
COLBG = col.Style.BRIGHT + col.Fore.GREEN
COLBY = col.Style.BRIGHT + col.Fore.YELLOW
COLBW = col.Style.BRIGHT + col.Fore.WHITE

# --------------------------------------------------------------------------------------------------------------

class CTutorial():

   def __init__(self, oRepositoryConfig=None, oStatistics=None):

      sMethod = "CTutorial.__init__"

      if oRepositoryConfig is None:
         bSuccess = None
         sResult  = "oRepositoryConfig is None"
         raise Exception(CString.FormatResult(sMethod, bSuccess, sResult))

      self.__oRepositoryConfig = oRepositoryConfig

      if oStatistics is None:
         bSuccess = None
         sResult  = "oStatistics is None"
         raise Exception(CString.FormatResult(sMethod, bSuccess, sResult))

      self.__oStatistics = oStatistics

      self.__listSections = []

   def __del__(self):
      pass


   # --------------------------------------------------------------------------------------------------------------
   def GetSectionsList(self):

      sMethod = "GetSectionsList"

      tupleSubfoldersToExclude = (".git", "__setup")

      bSuccess     = None
      sResult      = None

      sRepositoryPath = self.__oRepositoryConfig.Get('sRepositoryPath')

      listItems = os.listdir(sRepositoryPath)
      for sItem in listItems:
         if sItem not in tupleSubfoldersToExclude:
            sItem = CString.NormalizePath(os.path.join(sRepositoryPath, sItem))
            if os.path.isdir(sItem):
               self.__listSections.append(sItem)
         # eof if sItem not in tupleSubfoldersToExclude:
      # eof for sItem in listItems:

      self.__listSections.sort()
      nNrOfSections = len(self.__listSections)

      bSuccess = True
      sResult  = f"Found {nNrOfSections} tutorial sections within '{sRepositoryPath}'"

      return self.__listSections, bSuccess, CString.FormatResult(sMethod, bSuccess, sResult)


   # --------------------------------------------------------------------------------------------------------------
   def Clean(self):

      sMethod = "Clean"

      bSuccess = None
      sResult  = None

      for sSection in self.__listSections:
         print(f"* cleaning tutorial section '{sSection}'")

         for sLocalRootPath, listFolderNames, listFileNames in os.walk(sSection):
            for sFileName in listFileNames:
               if sFileName.lower().endswith(".html"):
                  sDocument = CString.NormalizePath(os.path.join(sLocalRootPath, sFileName))
                  oDocument = CFile(sDocument)
                  bSuccess, sResult = oDocument.Delete()
                  print(f"  - deleting '{sFileName}'")
                  if bSuccess is not True:
                     return bSuccess, CString.FormatResult(sMethod, bSuccess, sResult)
               # eof if sFileName.lower().endswith(".html"):
            # eof for sFileName in listFileNames:
         # eof for sLocalRootPath, listFolderNames, listFileNames in os.walk(sSection):
         print()
      # eof for sSection in self.__listSections:

      bSuccess = True
      sResult  = "Tutorial cleaning done."

      return bSuccess, CString.FormatResult(sMethod, bSuccess, sResult)


   # --------------------------------------------------------------------------------------------------------------
   def ConvertReadme(self):
      """Converts the main repository README from 'rst' to 'md' format.
      """

      sMethod = "ConvertReadme"

      bSuccess = None
      sResult  = None

      sReadMe_rst = self.__oRepositoryConfig.Get("sReadMe_rst")
      if sReadMe_rst is None:
         bSuccess = None
         sResult  = "sReadMe_rst is None"
         return bSuccess, CString.FormatResult(sMethod, bSuccess, sResult)

      sReadMe_md = self.__oRepositoryConfig.Get("sReadMe_md")
      if sReadMe_md is None:
         bSuccess = None
         sResult  = "sReadMe_md is None"
         return bSuccess, CString.FormatResult(sMethod, bSuccess, sResult)

      if os.path.isfile(sReadMe_rst) is False:
         bSuccess = False
         sResult  = f"Missing README file '{sReadMe_rst}'"
         return bSuccess, CString.FormatResult(sMethod, bSuccess, sResult)

      sFileContent = pypandoc.convert_file(sReadMe_rst, 'md')
      hFile_md = open(sReadMe_md, "w", encoding="utf-8")
      listFileContent = sFileContent.splitlines()
      for sLine in listFileContent:
          hFile_md.write(sLine + "\n")
      hFile_md.close()

      bSuccess = True
      sResult  = f"File '{sReadMe_rst}'\nconverted to\n'{sReadMe_md}'"
      return bSuccess, CString.FormatResult(sMethod, bSuccess, sResult)

   # --------------------------------------------------------------------------------------------------------------
   def DumpStatistics(self, oLogfile=None):
      """
      """

      # !! statistics are dumped at end of computation; therefore no return value (doesn't matter) !!

      nRJust = 39

      print()
      print(120*"=")
      print()
      print(COLBY + "                                                FINAL STATISTICS")
      print()

      if oLogfile is not None:
         oLogfile.Append()
         oLogfile.Append(120*"=")
         oLogfile.Append()
         oLogfile.Append("                                                FINAL STATISTICS")
         oLogfile.Append()

      listOut = []
      listOut.append("Nr of tutorial sections".rjust(nRJust, ' ') + " : " + self.__oStatistics.GetCntSections(1))
      listOut.append("Nr of input files".rjust(nRJust, ' ') + " : " + self.__oStatistics.GetCntInputFiles(1))
      listOut.append("Nr of generated output files".rjust(nRJust, ' ') + " : " + self.__oStatistics.GetCntOutputFilesExisting(1))
      listOut.append("Nr of output files not generated".rjust(nRJust, ' ') + " : " + self.__oStatistics.GetCntOutputFilesNotExisting(1))
      listOut.append("Nr of converter returned a value != 0".rjust(nRJust, ' ') + " : " + self.__oStatistics.GetCntConverterReturnedNotZero(1))
      for sOut in listOut:
         print(COLBW + sOut)
      print()

      if oLogfile is not None:
         for sOut in listOut:
            oLogfile.Append(sOut)
         oLogfile.Append()

      nNrOfInternalErrors = self.__oStatistics.GetCntInternalErrors()
      if nNrOfInternalErrors > 0:
         # -- mostly implementation issues after code changes; should not happen at runtime in released versions
         sOut = f"                                            !!! INTERNAL ERRORS : {nNrOfInternalErrors} !!!"
         print(COLBR + sOut)
         print()
         if oLogfile is not None:
            oLogfile.Append(sOut)
            oLogfile.Append()

      listFilesForConverterReturnedNotZero = self.__oStatistics.GetFileListForConverterReturnedNotZero()
      if len(listFilesForConverterReturnedNotZero) > 0:
         sOut = "Files where the converter returned a value != 0:"

         ## maybe not relevant enough for console
         ## print(COLBW + sOut)
         ## print()
         ## for sFile in listFilesForConverterReturnedNotZero:
         ##    print(f"* '{sFile}'")
         ## print()

         if oLogfile is not None:
            oLogfile.Append(sOut)
            oLogfile.Append()
            for sFile in listFilesForConverterReturnedNotZero:
               oLogfile.Append(f"* '{sFile}'")
            oLogfile.Append()
      # eof if len(listFilesForConverterReturnedNotZero) > 0:

      listOutputFilesNotCreated = self.__oStatistics.GetListOfOutputFilesNotCreated()
      if len(listOutputFilesNotCreated) > 0:
         sOut = "Possible output files that have not been created:"

         ## maybe not relevant enough for console
         ## print(COLBW + sOut)
         ## print()
         ## for sFile in listOutputFilesNotCreated:
         ##    print(f"* '{sFile}'")
         ## print()

         if oLogfile is not None:
            oLogfile.Append(sOut)
            oLogfile.Append()
            for sFile in listOutputFilesNotCreated:
               oLogfile.Append(f"* '{sFile}'")
            oLogfile.Append()
      # eof if len(listOutputFilesNotCreated) > 0:

      sLogfile = self.__oRepositoryConfig.Get('sLogfile')
      sOut = f"Log file: '{sLogfile}'"
      print(sOut)
      print()
      if oLogfile is not None:
         oLogfile.Append(sOut)
         oLogfile.Append()

      print(120*"=")
      print()
      if oLogfile is not None:
         oLogfile.Append(120*"=")
         oLogfile.Append()

   # --------------------------------------------------------------------------------------------------------------

# eof class CTutorial():

# --------------------------------------------------------------------------------------------------------------

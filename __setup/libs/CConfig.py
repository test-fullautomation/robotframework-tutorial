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
# CConfig.py
#
# XC-CT/ECA3-Queckenstedt
#
# 20.09.2022
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

def printerror(sMsg):
   sys.stderr.write(COLBR + f"Error: {sMsg}!\n")

# --------------------------------------------------------------------------------------------------------------

class CConfig():

   def __init__(self, sThisScript, sThisScriptVersionNumber, sThisScriptVersionDate):

      sMethod = "CConfig.__init__"

      self.__dictConfig = {}

      # Repository folder is parent folder of gen_doc_tutorial script.
      # This is the reference for all other paths.
      sRepositoryPath    = CString.NormalizePath(os.path.dirname(os.path.dirname(sThisScript)))
      sThisScriptName    = os.path.basename(sThisScript)
      sThisScriptVersion = f"{sThisScriptVersionNumber} / {sThisScriptVersionDate}"
      sThisScriptInfo    = f"{sThisScriptName} v. {sThisScriptVersion}"
      self.__dictConfig['sRepositoryPath']    = sRepositoryPath
      self.__dictConfig['sThisScriptName']    = sThisScriptName
      self.__dictConfig['sThisScriptVersion'] = sThisScriptVersion
      self.__dictConfig['sThisScriptInfo']    = sThisScriptInfo

      sThisScriptPath = CString.NormalizePath(os.path.dirname(sThisScript))
      self.__dictConfig['sLogfile'] = f"{sThisScriptPath}/gen_doc_tutorial.log"

      # 1. basic setup stuff
      self.__dictConfig['sPackageName']                = "robotframework-tutorial"
      self.__dictConfig['sVersion']                    = "0.1.0"
      self.__dictConfig['sAuthor']                     = "AIO team"
      self.__dictConfig['sAuthorEMail']                = "AIO team"
      self.__dictConfig['sDescription']                = "This package provides a tutorial for the RobotFramework AIO"
      self.__dictConfig['sLongDescriptionContentType'] = "text/markdown"
      self.__dictConfig['sURL']                        = "https://github.com/test-fullautomation/robotframework-tutorial"
      self.__dictConfig['sProgrammingLanguage']        = "Programming Language :: Python :: 3"
      self.__dictConfig['sLicence']                    = "License :: OSI Approved :: Apache Software License"
      self.__dictConfig['sOperatingSystem']            = "Operating System :: OS Independent"
      self.__dictConfig['sPythonRequires']             = ">=3.0"
      self.__dictConfig['sDevelopmentStatus']          = "Development Status :: 4 - Beta"
      self.__dictConfig['sIntendedAudience']           = "Intended Audience :: Developers"
      self.__dictConfig['sTopic']                      = "Topic :: Software Development"
      self.__dictConfig['arInstallRequires']           = ['sphinx','pypandoc','colorama']

      # 2. certain folder and executables (things that requires computation)
      bSuccess, sResult = self.__InitConfig()
      if bSuccess is not True:
         raise Exception(CString.FormatResult(sMethod, bSuccess, sResult))
      # print(COLBG + sResult) # (not really useful)
      # print()


   def __del__(self):
      del self.__dictConfig


   def __InitConfig(self):

      sMethod = "__InitConfig"

      sPlatformSystem = platform.system()
      sOSName         = os.name
      sPython         = CString.NormalizePath(sys.executable)
      sPythonPath     = os.path.dirname(sPython)
      sPythonVersion  = sys.version

      sThisScriptInfo = self.__dictConfig['sThisScriptInfo']
      print()
      print(f"This is {sThisScriptInfo}")
      print()
      print(f"Running under {sPlatformSystem} ({sOSName})")

      self.__dictConfig['sPlatformSystem'] = sPlatformSystem
      self.__dictConfig['sOSName']         = sOSName
      self.__dictConfig['sPython']         = sPython
      self.__dictConfig['sPythonPath']     = sPythonPath
      self.__dictConfig['sPythonVersion']  = sPythonVersion

      self.__dictConfig['sPandoc'] = None
      try:
          self.__dictConfig['sPandoc'] = CString.NormalizePath(pypandoc.get_pandoc_path())
      except Exception as ex:
          bSuccess = False
          sResult  = str(ex)
          return bSuccess, CString.FormatResult(sMethod, bSuccess, sResult)

      sRST2HTML = None
      if sPlatformSystem == "Windows":
         sRST2HTML = CString.NormalizePath(f"{sPythonPath}/Scripts/rst2html.py")
      elif sPlatformSystem == "Linux":
         sRST2HTML = CString.NormalizePath(f"{sPythonPath}/rst2html.py")
      else:
         bSuccess = None
         sResult  = f"Platform system '{sPlatformSystem}' is not supported"
         raise Exception(CString.FormatResult(sMethod, bSuccess, sResult))

      if os.path.isfile(sRST2HTML) is False:
         bSuccess = False
         sResult  = "Missing file converter '" + str(sRST2HTML) + "'"
         return bSuccess, CString.FormatResult(sMethod, bSuccess, sResult)
      self.__dictConfig['sRST2HTML'] = sRST2HTML

      # - README
      self.__dictConfig['sReadMe_rst'] = self.__dictConfig['sRepositoryPath'] + "/README.rst"
      self.__dictConfig['sReadMe_md']  = self.__dictConfig['sRepositoryPath'] + "/README.md"

      self.PrintConfig()

      bSuccess = True
      sResult  = "Repository setup done"
      return bSuccess, sResult

   # eof def __InitConfig(self):


   def PrintConfig(self):
      # -- printing configuration to console
      nJust = 30
      print()
      for sKey in self.__dictConfig:
         print(sKey.rjust(nJust, ' ') + " : " + str(self.__dictConfig[sKey]))
      print()
   # eof def PrintConfig(self):


   def Get(self, sName=None):
      if ( (sName is None) or (sName not in self.__dictConfig) ):
         print()
         printerror("Error: Configuration parameter '" + str(sName) + "' not existing!")
         # from here it's standard output:
         print("Use instead one of:")
         self.PrintConfig()
         return None # returning 'None' in case of key is not existing !!!
      else:
         return self.__dictConfig[sName]
   # eof def Get(self, sName=None):

   def Set(self, sName=None, sValue=None):
      if ( (sName is not None) and (sName.strip() != "") ):
         self.__dictConfig[sName] = sValue

# eof class CConfig():

# --------------------------------------------------------------------------------------------------------------

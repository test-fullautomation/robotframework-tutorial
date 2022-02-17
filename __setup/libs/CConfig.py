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
# CConfig.py
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
      self.__dictConfig['sVersion']                    = "0.0.0"
      self.__dictConfig['sAuthor']                     = "AIO team"
      self.__dictConfig['sAuthorEMail']                = "AIO team"
      self.__dictConfig['sDescription']                = "This package provides a tutorial for the RobotFramework AIO"
      self.__dictConfig['sLongDescriptionContentType'] = "text/markdown"
      self.__dictConfig['sURL']                        = "https://github.com/test-fullautomation/TODO"
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

      sOSName         = os.name
      sPlatformSystem = platform.system()

      self.__dictConfig['sOSName']         = sOSName
      self.__dictConfig['sPlatformSystem'] = sPlatformSystem

      sThisScriptInfo = self.__dictConfig['sThisScriptInfo']
      print()
      print(f"This is {sThisScriptInfo}")
      print()
      print(f"Running under {sPlatformSystem} ({sOSName})")

      SPHINXBUILD       = None
      sPython           = None
      sLaTeXInterpreter = None
      sRST2HTML         = None
      sGENHTMLDOC       = None

      try:
          self.__dictConfig['sPythonVersion'] = sys.version
          self.__dictConfig['sPandoc']        = CString.NormalizePath(pypandoc.get_pandoc_path())
      except Exception as ex:
          bSuccess = False
          sResult  = str(ex)
          return bSuccess, CString.FormatResult(sMethod, bSuccess, sResult)

      if sPlatformSystem == "Windows":
         # -- environment check
         sRobotPythonPath_EnvVar = "%RobotPythonPath%"
         sRobotPythonPath = os.path.expandvars(sRobotPythonPath_EnvVar)
         if sRobotPythonPath_EnvVar == sRobotPythonPath:
            # environment variable not resolved => not existing
            bSuccess = False
            sResult = f"""Missing Windows environment variable %RobotPythonPath%!
This application requires a Windows environment variable %RobotPythonPath%, pointing to a Python installation (version required: {self.__dictConfig['sPythonRequires']}) that shall be updated.
Please create and try again"""
            return bSuccess, CString.FormatResult(sMethod, bSuccess, sResult)

         SPHINXBUILD       = CString.NormalizePath("%RobotPythonPath%/Scripts/sphinx-build.exe")
         sPython           = CString.NormalizePath("%RobotPythonPath%/python.exe")
         sLaTeXInterpreter = CString.NormalizePath("%ROBOTLATEXPATH%/miktex/bin/x64/pdflatex.exe")
         sRST2HTML         = CString.NormalizePath("%RobotPythonPath%/Scripts/rst2html.py")
         sGENHTMLDOC       = CString.NormalizePath("%RobotDevEclipse%/tools/robot-genhtmldoc.py")

      elif sPlatformSystem == "Linux":
         # -- environment check
         sRobotPythonPath_EnvVar = "${RobotPythonPath}"
         sRobotPythonPath = os.path.expandvars(sRobotPythonPath_EnvVar)
         if sRobotPythonPath_EnvVar == sRobotPythonPath:
            # environment variable not resolved => not existing
            bSuccess = False
            sResult = f"""Missing Linux environment variable ${RobotPythonPath}!
This application requires a Linux environment variable ${RobotPythonPath}, pointing to a Python installation (version required: {self.__dictConfig['sPythonRequires']}) that shall be updated.
Please create and try again"""
            return bSuccess, CString.FormatResult(sMethod, bSuccess, sResult)
         SPHINXBUILD       = CString.NormalizePath("${RobotPythonPath}/sphinx-build")
         sPython           = CString.NormalizePath("${RobotPythonPath}/python3.9")
         sLaTeXInterpreter = CString.NormalizePath("${ROBOTLATEXPATH}/miktex/bin/x64/pdflatex")
         sRST2HTML         = CString.NormalizePath("${RobotPythonPath}/Scripts/rst2html.py")
         sGENHTMLDOC       = CString.NormalizePath("${RobotDevEclipse}/tools/robot-genhtmldoc.py")

      else:
         bSuccess = False
         sResult  = "Operating system " + str(sPlatformSystem) + " (" + str(sOSName) + ") not supported"
         return bSuccess, CString.FormatResult(sMethod, bSuccess, sResult)

      if os.path.isfile(SPHINXBUILD) is False:     # !! not yet used - but in fututure !!
         bSuccess = False
         sResult  = "Missing Sphinx '" + str(SPHINXBUILD) + "'"
         return bSuccess, CString.FormatResult(sMethod, bSuccess, sResult)

      if os.path.isfile(sPython) is False:
         bSuccess = False
         sResult  = "Missing Python '" + str(sPython) + "'"
         return bSuccess, CString.FormatResult(sMethod, bSuccess, sResult)

      if os.path.isfile(sLaTeXInterpreter) is False:
         sLaTeXInterpreter = None # PDF generation is an option

      if os.path.isfile(sRST2HTML) is False:
         bSuccess = False
         sResult  = "Missing file converter '" + str(sRST2HTML) + "'"
         return bSuccess, CString.FormatResult(sMethod, bSuccess, sResult)

      if os.path.isfile(sGENHTMLDOC) is False:
         bSuccess = False
         sResult  = "Missing file converter '" + str(sGENHTMLDOC) + "'"
         return bSuccess, CString.FormatResult(sMethod, bSuccess, sResult)

      self.__dictConfig['SPHINXBUILD']       = SPHINXBUILD
      self.__dictConfig['sPython']           = sPython
      self.__dictConfig['sLaTeXInterpreter'] = sLaTeXInterpreter
      self.__dictConfig['sRST2HTML']         = sRST2HTML
      self.__dictConfig['sGENHTMLDOC']       = sGENHTMLDOC

      # - README
      self.__dictConfig['sReadMe_rst'] = self.__dictConfig['sRepositoryPath'] + "/README.rst"
      self.__dictConfig['sReadMe_md']  = self.__dictConfig['sRepositoryPath'] + "/README.md"

      self.PrintConfig()

      bSuccess = True
      sResult  = "Repository setup done"
      return bSuccess, CString.FormatResult(sMethod, bSuccess, sResult)

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

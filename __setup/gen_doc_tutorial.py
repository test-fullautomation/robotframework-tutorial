# **************************************************************************************************************
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
# gen_doc_tutorial.py
#
# XC-CT/ECA3-Queckenstedt
#
# Builds the documentation of all tutorial files.
#
# More details in: __setup\tutorial_docu_concept.txt
#
# --------------------------------------------------------------------------------------------------------------
#
sThisScriptVersionNumber = "0.4.1"
sThisScriptVersionDate   = "16.02.2022"
#
# --------------------------------------------------------------------------------------------------------------
#TM***

import os, sys, time, platform, shlex, subprocess

import colorama as col

from PythonExtensionsCollection.String.CString import CString
from PythonExtensionsCollection.File.CFile import CFile

from libs.CConfig import *
from libs.CTutorial import *
from libs.CSection import *
from libs.CDocument import *
from libs.CStatistics import *

col.init(autoreset=True)

COLBR = col.Style.BRIGHT + col.Fore.RED
COLBY = col.Style.BRIGHT + col.Fore.YELLOW
COLBG = col.Style.BRIGHT + col.Fore.GREEN

SUCCESS                 = 0
WARNING_CONVERTER_ISSUE = 1
ERROR_CCONFIG           = 2
ERROR_CTUTORIAL         = 3
ERROR_README            = 4
ERROR_SECTIONSLIST      = 5
ERROR_CLEAN             = 6
ERROR_CSECTION          = 7
ERROR_DOCUMENTSLIST     = 8
ERROR_CDOCUMENT         = 9
ERROR_CONVERT           = 10

# --------------------------------------------------------------------------------------------------------------

def printerror(sMsg):
   sys.stderr.write(COLBR + f"{sMsg}!\n")

# --------------------------------------------------------------------------------------------------------------
#TM***

# -- setting up the repository configuration (relative to the path of this script)
oRepositoryConfig = None
try:
   oRepositoryConfig = CConfig(__file__, sThisScriptVersionNumber, sThisScriptVersionDate)
except Exception as ex:
   print()
   printerror(str(ex))
   print()
   sys.exit(ERROR_CCONFIG)

# -- opening the log file
sLogfile = oRepositoryConfig.Get("sLogfile")
oLogfile = CFile(sLogfile)
oLogfile.Write(oRepositoryConfig.Get("sThisScriptInfo") + " - started at " + time.strftime('%d.%m.%Y - %H:%M:%S'), 1)

# -- setting up the statistics
oStatistics = CStatistics()

# -- setting up the tutorial main class
oTutorial = None
try:
   oTutorial = CTutorial(oRepositoryConfig, oStatistics)
except Exception as ex:
   sResult = str(ex)
   print()
   printerror(sResult)
   print()
   oLogfile.Append(sResult)
   del oLogfile
   sys.exit(ERROR_CTUTORIAL)

# -- converting the repository README from rst to md format
bSuccess, sResult = oTutorial.ConvertReadme()
oLogfile.Append(sResult)
if bSuccess is not True:
   print()
   printerror(sResult)
   print()
   oStatistics.IncCntInternalErrors()
   oTutorial.DumpStatistics(oLogfile)
   del oLogfile
   sys.exit(ERROR_README)
else:
   print(COLBY + sResult)
print()

# -- computing the list of sections within the tutorial main folder
listSections, bSuccess, sResult = oTutorial.GetSectionsList()
oLogfile.Append(sResult)
if bSuccess is not True:
   print()
   printerror(sResult)
   print()
   oStatistics.IncCntInternalErrors()
   oTutorial.DumpStatistics(oLogfile)
   del oLogfile
   sys.exit(ERROR_SECTIONSLIST)
else:
   print(sResult)
print()

# -- removing previous results (= generated HTML files, for every section separately)
bSuccess, sResult = oTutorial.Clean()
oLogfile.Append(sResult)
if bSuccess is not True:
   print()
   printerror(sResult)
   print()
   oStatistics.IncCntInternalErrors()
   oTutorial.DumpStatistics(oLogfile)
   del oLogfile
   sys.exit(ERROR_CLEAN)
else:
   print(sResult)
print()

# -- for every tutorial section generate the documentation (in HTML format, out of robot, resource, rst and py files)
for sSectionRootPath in listSections:
   oStatistics.IncCntSections()
   oSection = None
   try:
      oSection = CSection(sSectionRootPath, oRepositoryConfig, oStatistics)
   except Exception as ex:
      sResult = str(ex)
      print()
      printerror(sResult)
      print()
      oLogfile.Append(sResult)
      oStatistics.IncCntInternalErrors()
      oTutorial.DumpStatistics(oLogfile)
      del oLogfile
      sys.exit(ERROR_CSECTION)

   listDocuments, bSuccess, sResult = oSection.GetDocumentsList()
   oLogfile.Append(sResult)
   if bSuccess is not True:
      print()
      printerror(sResult)
      print()
      oStatistics.IncCntInternalErrors()
      oTutorial.DumpStatistics(oLogfile)
      del oLogfile
      sys.exit(ERROR_DOCUMENTSLIST)
   else:
      print(sResult)
   print()

   for sDocument in listDocuments:
      try:
         oDocument = CDocument(sDocument, oRepositoryConfig, oStatistics)
      except Exception as ex:
         sResult = str(ex)
         print()
         printerror(sResult)
         print()
         oLogfile.Append(sResult)
         oStatistics.IncCntInternalErrors()
         oTutorial.DumpStatistics(oLogfile)
         del oLogfile
         sys.exit(ERROR_CDOCUMENT)

      bConverterIssue, bSuccess, sResult = oDocument.Convert()
      oLogfile.Append(sResult)
      if bSuccess is not True:
         print()
         printerror(sResult)
         print()
         oStatistics.IncCntInternalErrors()
         oTutorial.DumpStatistics(oLogfile)
         del oLogfile
         sys.exit(ERROR_CONVERT)
      else:
         if bConverterIssue is True:
            print(COLBY + sResult)
         else:
            print(sResult)
      print()
   # eof for sDocument in listDocuments:

# eof for sSectionRootPath in listSections:
   
# --------------------------------------------------------------------------------------------------------------

# -- final statistics

oTutorial.DumpStatistics(oLogfile)

# --------------------------------------------------------------------------------------------------------------

sResult = "Tutorial documentation rendering done"
print(COLBG + sResult)
print()
oLogfile.Append(sResult)

del oLogfile

if oStatistics.GetCntConverterReturnedNotZero() == 0:
   sys.exit(SUCCESS)
else:
   sys.exit(WARNING_CONVERTER_ISSUE)


# --------------------------------------------------------------------------------------------------------------


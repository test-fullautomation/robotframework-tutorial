@echo off
"%RobotPythonPath%/python.exe" ./gen_doc_tutorial.py
echo gen_doc_tutorial.py returned : %ERRORLEVEL%

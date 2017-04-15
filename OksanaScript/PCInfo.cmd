@ECHO OFF


SETLOCAL ENABLEEXTENSIONS

SET me=%~n0
SET parent=%~dp0

SET fl=%1

IF [%FL%] EQU [] (
SET fl=1
) 

SYSTEMINFO 1>%fl%

WMIC path Win32_VideoController 1>%fl%
@ECHO OFF

SETLOCAL ENABLEEXTENSIONS ENABLEDELAYEDEXPANSION

SET flPath=%1
SET fl=
SET flF=

IF "%flPath%" NEQ "" (
SET flF=1^>%flPath%
SET fl=1^>^>%flPath%
)

echo CPU information: %flF%
wmic cpu get Caption,MaxClockSpeed /format:list | findstr /r /v "^$" %fl%
echo. %fl%

echo OS information: %fl%
wmic os get Caption,CSDVersion /format:list | findstr /r /v "^$" %fl%
echo. %fl%

echo Video controller information: %fl%
WMIC path Win32_VideoController get Caption,DriverVersion /format:list | findstr /r /v "^$" %fl%
echo. %fl%


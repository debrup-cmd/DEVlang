@echo off
title DebLang v1.0
cd /d "%~dp0"
echo.
echo ================================================
echo                 DEBLANG v1.0
echo          My Own Flavour of Python
echo               Powered by DebVM
echo ================================================
echo.
where py >nul 2>nul
if %errorlevel%==0 (
    py -m deblang
    goto :end
)
where python >nul 2>nul
if %errorlevel%==0 (
    python -m deblang
    goto :end
)
echo Python was not found on this computer.
echo.
echo Please install Python 3.9 or newer from:
echo https://www.python.org/downloads/
echo IMPORTANT: Tick "Add Python to PATH" during installation.
echo Then close this window and double-click START_DEBLANG.bat again.
echo.
pause
:end

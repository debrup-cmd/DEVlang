@echo off
title Run DebLang Example
cd /d "%~dp0"
echo Running the DebLang conditions example...
where py >nul 2>nul
if %errorlevel%==0 (
    py -m deblang examples\conditions.deb
    goto :end
)
python -m deblang examples\conditions.deb
:end
echo.
pause

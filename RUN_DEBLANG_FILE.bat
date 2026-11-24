@echo off
cd /d "%~dp0"
if "%~1"=="" (
    echo Usage: Drag a .deb file onto this batch file.
    echo Or run: RUN_DEBLANG_FILE.bat examples\hello.deb
    pause
    exit /b 1
)
where py >nul 2>nul
if %errorlevel%==0 (
    py -m deblang "%~1"
    goto :end
)
python -m deblang "%~1"
:end
echo.
pause

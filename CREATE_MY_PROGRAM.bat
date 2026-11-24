@echo off
title Create a DebLang Program
cd /d "%~dp0"
if not exist "my_first_program.deb" (
    >"my_first_program.deb" echo # My first DebLang program
    >>"my_first_program.deb" echo naam = pucho("What is your name? ")
    >>"my_first_program.deb" echo bolo("Namaste", naam)
)
echo.
echo Created my_first_program.deb in the DebLang folder.
echo Open it with Notepad or VS Code, edit it, save it,
echo then drag the file onto RUN_DEBLANG_FILE.bat.
echo.
pause

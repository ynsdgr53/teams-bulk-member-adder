@echo off
chcp 65001 >nul
title Build Teams Bulk Member Adder
echo ========================================================
echo   Building Teams Bulk Member Adder Standalone EXE
echo ========================================================
echo.

py -m pip install -r requirements.txt pyinstaller
if %ERRORLEVEL% NEQ 0 (
    echo [ERROR] Failed to install requirements.
    pause
    exit /b %ERRORLEVEL%
)

echo.
echo Building single-file executable with PyInstaller...
py -m PyInstaller --onefile --noconsole --name "Teams_Bulk_Member_Adder" --collect-all customtkinter src\main.py

if %ERRORLEVEL% EQU 0 (
    copy /y "dist\Teams_Bulk_Member_Adder.exe" ".\Teams_Bulk_Member_Adder.exe"
    rmdir /s /q build dist 2>nul
    del /q Teams_Bulk_Member_Adder.spec 2>nul
    echo.
    echo ========================================================
    echo   [SUCCESS] Standalone EXE created: Teams_Bulk_Member_Adder.exe
    echo ========================================================
) else (
    echo.
    echo [ERROR] Build failed!
)
pause

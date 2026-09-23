@echo off
chcp 65001 >nul
title Teams Bulk Member Adder
py src\main.py
if %ERRORLEVEL% NEQ 0 (
    echo.
    echo Make sure Python and dependencies are installed:
    echo py -m pip install -r requirements.txt
    pause
)

@echo off
cls

sphinx-apidoc -o . ..
echo.
.\make.bat %1

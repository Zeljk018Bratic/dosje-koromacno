@echo off
title Provjera linkova - Dosje Koromacno
color 0A
echo ===================================================
echo   PROVJERA LINKOVA U HTML DATOTEKAMA
echo ===================================================
echo.
cd /d "C:\Users\zeljk\dosje-koromacno"
powershell -ExecutionPolicy Bypass -File ".\alati\provjeri_linkove.ps1"
echo.
echo ===================================================
echo Provjera zavrsena. Pritisni bilo koju tipku za izlaz...
pause > nul

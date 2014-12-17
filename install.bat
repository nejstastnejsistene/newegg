@echo off
set pythonw=C:\Python27\pythonw.exe
schtasks /create /sc minute /mo 1 /tn "Newegg Stock Checker Script" /tr "%pythonw% \"%cd%\newegg.pyw\""
pause
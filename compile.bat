@echo off
RD /S /Q compile 2>nul
title Compiler
cls
md compile
copy /Y main.py ".\compile\main.py">nul
copy /Y icon.png ".\compile\icon.png">nul
copy /Y nofile.png ".\compile\nofile.png">nul
cd compile
%appdata%\python\python310\Scripts\pyinstaller --noconfirm --onedir --windowed --clean --log-level "WARN" "main.py">nul
rd /S /Q build
del /Q main.spec
xcopy ".\dist\main\*" ".\" /E >nul
rd /S /Q dist
ren main.exe SMRP.exe
md Files
copy ..\icon.png .\ >nul
copy ..\Files\ .\Files\>nul
del /Q main.py
echo.
echo Done
pause>nul
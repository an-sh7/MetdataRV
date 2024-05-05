@echo off

rem Get the directory path of the batch script
set script_dir=%~dp0

rem Run the exiftool.py Python script located in the same directory as this batch file
python "%script_dir%\exiftool.py"

@echo off

rem Get the directory path of the batch script
set script_dir=%~dp0

:loop

rem Run the exiftool.py Python script located in the same directory as this batch file
python "%script_dir%\exiftool.py"

rem Prompt the user to press "Q" to quit or any other key to continue
set /p choice=Press Q to quit, or any other key to continue:
if /I "%choice%"=="q" goto end

goto loop

:end

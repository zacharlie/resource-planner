@echo off
cd %~dp0
call .\venv\Scripts\activate
call %~dp0zero.bat
call %~dp0mm.bat
call %~dp0migrate.bat
call %~dp0serve.bat

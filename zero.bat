@echo off
cd %~dp0
call .\venv\Scripts\activate
python manage.py migrate activity zero
python manage.py migrate event zero
python manage.py migrate resource zero

del /s /q .\rp\activity\migrations\*.py
echo.> .\rp\activity\migrations\__init__.py
del /s /q .\rp\event\migrations\*.py
echo.> .\rp\event\migrations\__init__.py
del /s /q .\rp\resource\migrations\*.py
echo.> .\rp\resource\migrations\__init__.py

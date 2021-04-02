@echo off

cd src
FOR %%x in (%*) DO python manage.py startapp %%x
cd ..

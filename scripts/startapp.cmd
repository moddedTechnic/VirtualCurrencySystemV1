@echo off

FOR %%x in (%*) DO (
    python src\manage.py startapp %%x
)

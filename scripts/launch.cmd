@echo off
cls

IF "%1" == "" (
    SET host="80"
) ELSE (
    SET host="%~1"
)

IF "%2" NEQ "" SET host="%host%:%~2"

python src\manage.py runserver %host%

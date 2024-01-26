@ECHO off

start /min python manage.py runserver
timeout 3
start /min npm run project
@ECHO off

start /min python manage.py runserver
timeout 5
start /min npm run project
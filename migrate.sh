#/bin/bash

python cah/manage.py makemigrations && 
python cah/manage.py migrate

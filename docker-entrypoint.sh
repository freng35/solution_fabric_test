#!/bin/bash

cd fabric_test || exit

while ! curl http://fabric_db:5432/ 2>&1 | grep '52'
do
  echo "ждем"
  sleep 1
done
echo "бд поднялось"

python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py runserver 0.0.0.0:8000
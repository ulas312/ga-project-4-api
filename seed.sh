#!/bin/bash

echo "dropping database django-sneakers"
dropdb django-sneakers

echo "creating database django-sneakers"
createdb django-sneakers

python3 manage.py makemigrations

python3 manage.py migrate

echo "inserting users"
python3 manage.py loaddata jwt_auth/seeds.json

echo "inserting brands"
python3 manage.py loaddata brands/seeds.json

echo "inserting sneakerModels"
python3 manage.py loaddata sneakerModels/seeds.json

echo "inserting comments"
python3 manage.py loaddata comments/seeds.json
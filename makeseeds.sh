#!/bin/bash

echo "creating brands/seeds.json"
python3 manage.py dumpdata brands --output brands/seeds.json --indent=2;

echo "creating sneakerModels/seeds.json"
python3 manage.py dumpdata sneakerModels --output sneakerModels/seeds.json --indent=2;

echo "creating comments/seeds.json"
python3 manage.py dumpdata comments --output comments/seeds.json --indent=2;

echo "creating jwt_auth/seeds.json"
python3 manage.py dumpdata jwt_auth --output jwt_auth/seeds.json --indent=2;


#!/bin/bash

export HOST=${LEAKY_HOST:="0.0.0.0"}
export LEAKY_DOMAIN_NAME=${LEAKY_DOMAIN_NAME:="leaky.com"}
export DJANGO_SETTINGS_MODULE=${DJANGO_SETTINGS_MODULE:="leaky.settings"}
export LEAKY_DEBUG=${LEAKY_DEBUG:="1"}
export LEAKY_SYSTEM_EMAIL=${LEAKY_SYSTEM_EMAIL:="root@leaky.com"}
export LEAKY_ADMIN_EMAIL=${LEAKY_ADMIN_EMAIL:="admin@leaky.com"}
export LEAKY_ADMIN_PASSWORD=${LEAKY_ADMIN_PASSWORD:="password"}
export LEAKY_DATABASE_NAME=${LEAKY_DATABASE_NAME:="postgres"}
export LEAKY_DATABASE_USER=${LEAKY_DATABASE_USER:="postgres"}
export LEAKY_DATABASE_PASSWORD=${LEAKY_DATABASE_PASSWORD:="postgres"}
export LEAKY_DATABASE_HOST=${LEAKY_DATABASE_HOST:="localhost"}
export LEAKY_DATABASE_PORT=${LEAKY_DATABASE_PORT:="5432"}
export LEAKY_DEFAULT_FROM_EMAIL=${LEAKY_DEFAULT_FROM_EMAIL:="root@leaky.com"}
export LEAKY_STATIC_ROOT=${LEAKY_STATIC_ROOT:="/srv/leaky-app/static/"}
export LEAKY_MEDIA_ROOT=${LEAKY_MEDIA_ROOT:="/srv/leaky-app/media/"}
export LEAKY_PORT=${LEAKY_PORT:="8000"}

# remove this before running
docker stop $(docker ps -a -q)
docker rm -v $(docker ps -a -q)
xfce4-terminal -T leaky-postgres -e "docker run -it --rm=true --name leaky-postgres -p 5432:5432 -e POSTGRES_PASSWORD=postgres postgres"

# we don't need migrations until we have the first stable release
rm -rf ./customers/migrations
rm -rf ./warehouses/migrations

# creating a tmp virtualenv for testing
virtualenv --clear /tmp/leaky_venv -p python3.6
. /tmp/leaky_venv/bin/activate
pip install -r ./requirements.txt
pip install --no-deps -r ./no-deps-requirements.txt

RC=1
while [ $RC -eq 1 ]
do
  echo 'Testing database connection...'
  python check_db.py
  RC=$?
done

# Perform the initial schema migrations
python manage.py makemigrations  --noinput

# generate migrations for apps
python manage.py makemigrations customers --noinput
python manage.py makemigrations warehouses --noinput

# generate empty migrations for apps
#python manage.py makemigrations --empty customers --noinput

# applying migrations
python manage.py migrate_schemas
python manage.py migrate_schemas --shared

# create new apps
#python manage.py startapp <app_name>

python init_db.py

# Start the server
python3 -u manage.py runserver ${HOST}:8000

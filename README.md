# TransporterBackend
# http://ctvehicular.pythonanywhere.com/

CTVehicular:
Version:
Python: 3.8
Django: 2.2.7
MySql: 5.7.27
  name: CTVehicular$DBCTVehicular

Nombre Proyecto
Transporter
 |_ appVehicular

Details:
  MySql
    drop database ctvehicular$dbctvehicular;
    create database ctvehicular$dbctvehicular;
    use ctvehicular$dbctvehicular;
    create user CTVehicular identified by "idsCT2020";
    grant all on ctvehicular$dbctvehicular.* to CTVehicular;
    flush privileges;
  Steps

    python manage.py makemigrations appVehicular
    python manage.py migrate

    python manage.py makemigrations
    python manage.py migrate --run-syncdb
    python manage.py migrate

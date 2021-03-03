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


Manual

  Facebook
https://www.facebook.com/v8.0/dialog/oauth?client_id=1034969293634110&redirect_uri=http://localhost:8000/&state={state-param}

  Google
https://accounts.google.com/o/oauth2/v2/auth?
 scope=https://www.googleapis.com/auth/userinfo.profile&
 access_type=offline&
 include_granted_scopes=true&
 response_type=code&
 redirect_uri=http://localhost:8000/&
 client_id=767125300767-fbti9tafnkvdvk5t2m4poe7sv79a6h0f.apps.googleusercontent.com


Copiar code de url redirigida y hacer post a http://localhost:8000/api/login/social/token/
con form  provider 'facebook' y code 'lo de arriba'
con form  provider 'google-oauth2' y code 'lo de arriba'

recibe token de aplicacion de una red social

token--> Authorization : Token <token>
  
pip install django-filter
pip install firebase-admin

python manage.py loaddata fixtures/*.json

Delete the sqlite database file (often db.sqlite3) in your django project folder (or wherever you placed it)
Delete everything except __init__.py file from migration folder in all django apps
Make changes in your models (models.py).
Run the command python manage.py makemigrations or python3 manage.py makemigrations
Then run the command python manage.py migrate.
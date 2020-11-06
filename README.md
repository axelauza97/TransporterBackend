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

Primero login
http://localhost:8000/api/auth/login/facebook
http://localhost:8000/api/auth/login/google-oauth2/
se crea registro en python social auth

Luego cargar el token
Con los datos de user social auths 
(POST) http://localhost:8000/api/auth/convert-token?grant_type=convert_token&backend=facebook&token=EAAOtTJEZAuj4BAFZB8CpOpWtghjSwcHiDphv6Lo7ZCLkL3pAqKL2iaEYuzk1GsGNV7qPakc4ELLm1rGIM7SZAjRzlMvwmvgG63CgZC9ZA4r4POMOYZAD7xtzaYYR4CvHnvvmoel92iTsVNHWqDez8ZB1bx7gfvKHEN9loXTueDFtqCWvDOPUcdO9&client_id=HcfRA5CdaIWRvB86nkGhKNCnbM7t9b7NhQXGcIXA&client_secret=YcMq0S6fVpDFP7ZzxjyN0EZghuFQfg2tZQT7aIG5OmDGY1vB6CcnYwEmfmnBuIv3gehtfYsYfcMCpFKcKaxQBwLA852E1sg1DR4YxYqFZJdmM0Py8X6f9UJMkpqcdY2M
token=access_token user social auth 


En el BODY enviar access_token=<token> del anterior comando


consultar  rest-auth  y usar ese token
sin social poner Authorization : Token <token>
  
Install modules and run server:
   pip install --upgrade pip
   pip install django-oauth2-provider
   pip install django-oauth-toolkit djangorestframework
   pip install social-auth-app-django
   pip install django-rest-framework-social-oauth2
   pip install django-cors-headers
   python manage.py runserver

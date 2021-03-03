import firebase_admin
from firebase_admin import credentials
from firebase_admin import auth
from firebase_admin import exceptions
import sys
import os
from .models import *
#from pyrebase import pyrebase

from django.contrib.staticfiles.storage import staticfiles_storage

cred = credentials.Certificate(staticfiles_storage.path('vehicular-287023-firebase-adminsdk-wdn25-afc249ecfb.json'))
default_app = firebase_admin.initialize_app(cred)

def crearUsuarioFirebase(email,f_name,lname):
    uid = None
    try:
        nombre = f_name +' '+ lname
        user = auth.create_user(
        email=email,
        email_verified=False,
        display_name=nombre,
        disabled=False,)
        uid = user.uid
        return uid
    except Exception:
            eliminarUsuarioFirebase(uid)
            return None
def linkpaswordreset(email):
    link = auth.generate_password_reset_link(email)
    return link

def eliminarUsuarioFirebase(uid_user):
    try:
        auth.delete_user(uid_user)
        return True
    except Exception:
        return False

def verificarToken(id_token):
    decoded_token = None
    try:
        decoded_token = auth.verify_id_token(id_token)
    except Exception:
        return None
    if not id_token or not decoded_token:
        return None
    try:
        uid = decoded_token.get("uid")
        return uid
    except Exception:
        return None

def verificarEmail(email):
    try:
        user = auth.get_user_by_email(email)
        return True
    except exceptions. NotFoundError:
        return False

def habilitarUsuario(uid_user):
    try:
        update_user(uid_user, disabled=False)
        return True
    except exceptions. NotFoundError:
        return False

def inhabilitarUsuario(uid_user):
    try:
        update_user(uid_user, disabled=True)
        return True
    except exceptions. NotFoundError:
        return False



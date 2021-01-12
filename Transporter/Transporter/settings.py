"""
Django settings for Transporter project.

Generated by 'django-admin startproject' using Django 2.2.7.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os
import pytz

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: don't run with debug turned on in production!
SECRET_KEY = 's)%xi3rob-o7!(rjtq1vc4t8&_a94!ca5+jo&xr^ggu7b5nw73'
DEBUG = True

#ALLOWED_HOSTS = ['CTVehicular.pythonanywhere.com']
ALLOWED_HOSTS = ['*'] #acepte todos los dominios

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework.authtoken',
    'appVehicular',
    'fcm_django',
    'oauth2_provider',
    'social_django',
    'rest_framework_social_oauth2',
    'rest_social_auth',
    'corsheaders',
    #'rest_framework_swagger',
]

AUTH_USER_MODEL = 'appVehicular.User'

#capa encima de backend de conexión , recursos disponibles externos
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'social_django.middleware.SocialAuthExceptionMiddleware',
]

ROOT_URLCONF = 'Transporter.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect',
            ],
        },
    },
]


WSGI_APPLICATION = 'Transporter.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases
'''
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'CTVehicular$DBCTVehicular',
        'USER': 'CTVehicular',
        'PASSWORD': 'idsCT2020',
        'HOST': 'localhost',
        'PORT': '3306',

    }

}
'''
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

LOCAL_TZ = pytz.timezone('America/Guayaquil')

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'

# default static files settings for PythonAnywhere.
# see https://help.pythonanywhere.com/pages/DjangoStaticFiles for more info
#MEDIA_ROOT = '/home/CTVehicular/Transporter/media'
#MEDIA_URL = '/media/'
#STATIC_ROOT = '/home/CTVehicular/Transporter/static'
#STATIC_URL = '/static/'
CORS_ALLOW_ALL_ORIGINS = True  # permite que cualquier domini entre; en produccion usar whitelist

FCM_DJANGO_SETTINGS = {
         # default: _('FCM Django')
        "APP_VERBOSE_NAME": "Vehicular",
         # Your firebase API KEY
        "FCM_SERVER_KEY": "AAAAkjaU_KQ:APA91bHkHveYfsBPbzBGoa-53cDYSzgG-Z5Rcq7HLrklDg4KpYGRXOjhS7XfJhqEAESAwQ2hsptAAMtKqeKFte0QLpkwe8pbZ2UNkJTLokWaNIPfmBKxB4PYl5ScsUSq3-P-zWPI-XCs",

         # true if you want to have only one active device per registered user at a time
         # default: False
        "ONE_DEVICE_PER_USER": True,
         # devices to which notifications cannot be sent,
         # are deleted upon receiving error response from FCM
         # default: False
        "DELETE_INACTIVE_DEVICES": False,
}

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
        'oauth2_provider.contrib.rest_framework.OAuth2Authentication',  # django-oauth-toolkit >= 1.0.0
        'rest_framework_social_oauth2.authentication.SocialAuthentication',
    ),
}

#REST_FRAMEWORK = { 'DEFAULT_SCHEMA_CLASS': 'rest_framework.schemas.coreapi.AutoSchema' }


AUTHENTICATION_BACKENDS = (
    # Facebook
    'social_core.backends.facebook.FacebookAppOAuth2',
    'social_core.backends.facebook.FacebookOAuth2',

    # Google OAuth2
    'social_core.backends.google.GoogleOAuth2',
    'social_core.backends.google.GoogleOAuth',
    'rest_framework_social_oauth2.backends.DjangoOAuth2',

    'django.contrib.auth.backends.ModelBackend',    
)

LOGOUT_REDIRECT_URL='http://localhost:8000/'
REST_SOCIAL_DOMAIN_FROM_ORIGIN=False



# Google configuration

# Define SOCIAL_AUTH_GOOGLE_OAUTH2_SCOPE to get extra permissions from Google.
# Facebook configuration
#SOCIAL_AUTH_LOGIN_REDIRECT_URL = '/api/tokenFB/'

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '767125300767-fbti9tafnkvdvk5t2m4poe7sv79a6h0f.apps.googleusercontent.com'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = 'sGCg0nRdlo3lXf4AiVR6zvih'
SOCIAL_AUTH_GOOGLE_OAUTH2_SCOPE = [
    'https://www.googleapis.com/auth/userinfo.email',
    'https://www.googleapis.com/auth/userinfo.profile',
] 

# Define SOCIAL_AUTH_FACEBOOK_SCOPE to get extra permissions from Facebook.
# Email is not sent by default, to get it, you must request the email permission.
SOCIAL_AUTH_FACEBOOK_KEY = '1034969293634110'
SOCIAL_AUTH_FACEBOOK_SECRET = '9ac01bac616f497016a5e67c659d3402'
SOCIAL_AUTH_FACEBOOK_SCOPE = ['email']
SOCIAL_AUTH_FACEBOOK_PROFILE_EXTRA_PARAMS = {
    'fields': 'id, name, email'
}

#SOCIAL_AUTH_FIELDS_STORED_IN_SESSION = ['key']


# Uploaded files
MEDIA_ROOT = os.path.join(BASE_DIR, 'static')
MEDIA_URL = '/media/'

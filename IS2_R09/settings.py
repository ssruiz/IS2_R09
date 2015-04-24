# -*- encoding: utf-8 -*-
"""
Django settings for IS2_R09 project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
#from django.conf.global_settings import MEDIA_ROOT, MEDIA_URL,\
 #   DATE_INPUT_FORMATS
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '@868wy4_1qa^7pgw38efx075awj0&fv$&=#1oh_$@n_rr441f('

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django_admin_bootstrapped',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'IS2_R09.apps.Usuario',
    'IS2_R09.apps.Proyecto',
    'IS2_R09.apps.Flujo',
    'IS2_R09.apps.US',
    'IS2_R09.apps.Sprint',
    
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # 'django.contrib.staticfiles',
)

ROOT_URLCONF = 'IS2_R09.urls'

WSGI_APPLICATION = 'IS2_R09.wsgi.application'


#identificar, extender o definir perfil para usuarios 
AUTH_PROFILE_MODULE = 'Usuario.usuario'
#DJANGO_GROUP_MODEL = 'Roles.roles'

TEMPLATE_DIRS = {
              "/home/samuel/workspace/IS2_R09/templates",
              }

#Base de datos postgresql

DATABASES = {
'default': {
'ENGINE': 'django.db.backends.postgresql_psycopg2',
'NAME': 'IS2_R09',
'USER': 'samuel',
'PASSWORD': 'passwd',
'HOST': 'localhost',
'PORT': '5432',

}
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'es-paraguay'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

client_encoding= 'UTF8'
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/
#STATIC_ROOT = ' '
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    "/home/rafael/workspace/IS2_R09/IS2_R09/media",
)

URL_LOGIN = '/login'
MEDIA_ROOT = '/home/samuel/workspace/IS2_R09/IS2_R09/media'
MEDIA_URL = '/media/'

# Configuracion de mail
EMAIL_USE_TLS = True 
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'is2.pagiles@gmail.com'
EMAIL_HOST_PASSWORD = 'is_2_r09'
EMAIL_PORT = 587

# Formato para fechas
DATE_INPUT_FORMATS = (
    '%Y-%m-%d', '%m/%d/%Y', '%m/%d/%y', # '2006-10-25', '10/25/2006', '10/25/06'
    '%b %d %Y', '%b %d, %Y',            # 'Oct 25 2006', 'Oct 25, 2006'
    '%d %b %Y', '%d %b, %Y',            # '25 Oct 2006', '25 Oct, 2006'
    '%B %d %Y', '%B %d, %Y',            # 'October 25 2006', 'October 25, 2006'
    '%d %B %Y', '%d %B, %Y',            # '25 October 2006', '25 October, 2006'
)

PATH = '/home/samuel/workspace/IS2_R09'
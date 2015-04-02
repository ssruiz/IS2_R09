"""
Django settings for IS2_R09 project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
from django.conf.global_settings import MEDIA_ROOT, MEDIA_URL
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
    'IS2_R09.apps.Usuario'
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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/
#STATIC_ROOT = ' '
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    "/home/samuel/workspace/IS2_R09/IS2_R09/media",
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

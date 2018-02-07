import os

from .settings import *

import dj_database_url

SECRET_KEY = os.environ['DJANGO_SECRET_KEY']
DATABASES['default'] = dj_database_url.config()

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

ALLOWED_HOSTS = ['grorg.herokuapp.com']  # Change this to ['yourapp.herokuapp.com']

STATIC_ROOT = 'staticfiles'

DEBUG = False

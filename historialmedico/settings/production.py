
import os
import dj_database_url
from django.conf import settings

SECRET_KEY = os.environ['SECRET_KEY']
DEBUG = False
DATABASES = settings.DATABASES

db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

ALLOWED_HOSTS = ['*']

STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'

EMAIL_HOST_USER = os.environ['EMAIL']
EMAIL_HOST_PASSWORD = os.environ['PASSWORD']
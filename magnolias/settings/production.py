from .base import *
DEBUG = True

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'd1rut6pj6huh5',
        'USER': 'spnaavijdvmlto',
        'PASSWORD': '93ea0913adfc3dba5f01206209b15e5d3348c679e9ebc6a6912db5198d1417a8',
        'HOST': 'ec2-52-70-15-120.compute-1.amazonaws.com',
        'PORT': '5432',
    }
}


STATICFILES_DIRS =(BASE_DIR, 'static')

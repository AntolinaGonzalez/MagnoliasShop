from .base import *
DEBUG = True

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'd8s8avl18jnbdj',
        'USER': 'dphiusaqouxcxx',
        'PASSWORD': '95f3228271639c8802ab9804ebc0c81d6a787ac5786df8673d4ba74a52a7af64',
        'HOST': 'ec2-34-192-173-173.compute-1.amazonaws.com',
        'PORT': 5432,
    }
}


STATICFILES_DIRS =(BASE_DIR, 'static')

MEDIA_URL = '/img/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'img')


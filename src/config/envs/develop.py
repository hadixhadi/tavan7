import os.path
from .settings import *
from environs import Env
env=Env()
env.read_env()
#structure settings
SECRET_KEY =env.str("SECRET_KEY")
DEBUG = env.bool("DEBUG",default=False)
ALLOWED_HOSTS = ['app']
#database settings
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': env.str("DB_NAME"),
        'USER': env.str("DB_USER"),
        'PASSWORD': env.str("DB_PASSWORD"),
        'HOST': env.str("DB_HOST"),
        'PORT': env.int("DB_PORT"),
    }
}


#static files siettings
STATIC_ROOT=os.path.join(BASE_DIR,'static')
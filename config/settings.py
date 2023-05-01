import os
import dj_database_url

from typing import Union
from pathlib import Path
from dotenv import load_dotenv

from django.core.exceptions import ImproperlyConfigured
from django.core.management.utils import get_random_secret_key


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
load = load_dotenv(os.path.join(BASE_DIR, '.env'))

def get_env_variable(var_name: str, default: Union[str, None] = None) -> str:
    try:
        return os.environ[var_name] if os.environ[var_name] else default
    except KeyError:
        if default is not None:
            return default
        error_msg = f"Set the {var_name} environment variable"
        raise ImproperlyConfigured(error_msg)

# Variable environment local or production
ENV = get_env_variable('ENV', 'development')


# SECURITY WARNING: keep the secret key used in production secret!
DEFAULT_SECRET_KEY = get_random_secret_key() + get_random_secret_key() + get_random_secret_key()
SECRET_KEY = get_env_variable('SECRET_KEY', DEFAULT_SECRET_KEY)

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = ENV != 'production'

ALLOWED_HOSTS = get_env_variable('ALLOWED_HOSTS', "127.0.0.1 localhost").split(" ")

# Application definition
DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
]

THIRD_PARTY_APPS = [
    'cloudinary',
    'cloudinary_storage',
    'import_export',
]

LOCAL_APPS = [
    'apps.home',
    'apps.users',
    'apps.profiles',
    'apps.post',
    'apps.comments',
    'apps.friends',
    'apps.notifications',
    'apps.chat',
]

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    "whitenoise.middleware.WhiteNoiseMiddleware",
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'middlewares.ajaxMiddleware.AjaxMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES_DIRS = [
    os.path.join(BASE_DIR, 'templates'),
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': TEMPLATES_DIRS,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'


DEFAULT_DATABASE_URL = "sqlite:////{0}".format(os.path.join(BASE_DIR, 'db.sqlite3'))

if ENV == 'production':
    DATABASE_URL = get_env_variable('DATABASE_URL')

DATABASES = {
    'default': dj_database_url.config(default=DEFAULT_DATABASE_URL)
}

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'fr-fr'

TIME_ZONE = 'Europe/Paris'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images) and media
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

MEDIA_URL = '/mediafiles/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'mediafiles')

STORAGES = {
    "default": {
        "BACKEND": "cloudinary_storage.storage.MediaCloudinaryStorage",
        # "BACKEND": "cloudinary_storage.storage.MediaCloudinaryStorage" if ENV == "production" else "django.core.files.storage.FileSystemStorage",
    },
    "staticfiles": {
        "BACKEND": "django.contrib.staticfiles.storage.StaticFilesStorage",
    },
}

FIXTURE_DIRS = [
    os.path.join(BASE_DIR, "fixtures"),
]


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_USER_MODEL = 'users.CustomUser'

# Config Send Email
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = get_env_variable('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = get_env_variable('EMAIL_HOST_PASSWORD')
EMAIL_PORT= 587
EMAIL_USE_TLS = True


# config cloudinary for production
# if ENV == 'production':
CLOUDINARY_STORAGE = {
    'CLOUD_NAME': get_env_variable('CLOUDINARY_CLOUD_NAME'),
    'API_KEY': get_env_variable('CLOUDINARY_API_KEY'),
    'API_SECRET': get_env_variable('CLOUDINARY_API_SECRET')
}


ADMIN_FIRST_NAME = get_env_variable('ADMIN_FIRST_NAME', 'Admin')
ADMIN_LAST_NAME = get_env_variable('ADMIN_LAST_NAME', 'AD')
ADMIN_EMAIL = get_env_variable('ADMIN_EMAIL', 'admin@gmail.com')
ADMIN_PASSWORD = get_env_variable('ADMIN_PASSWORD', 'admin')

# uid acces Interface Administrateur 
UID_ADMIN = get_env_variable('UID_ADMIN', '2de70bac-86a5-4fb5-a3b4-9b375ef0342b03f63189-3f5b-4a07-b8d2-8402b9af726f')


# # Django Debug Toolbar
# if ENV == 'development':
#     INSTALLED_APPS += [
#         'debug_toolbar',
#         'django_extensions',
#         'rest_framework',
#     ]
#     MIDDLEWARE = ['debug_toolbar.middleware.DebugToolbarMiddleware'] + list(MIDDLEWARE)
#     INTERNAL_IPS = ['127.0.0.1']

#     import mimetypes
#     mimetypes.add_type("application/javascript", ".js", True)

#     DEBUG_TOOLBAR_PATCH_SETTINGS = False

#     def show_toolbar(request):
#         return True
        
#     DEBUG_TOOLBAR_CONFIG = {
#         'INTERCEPT_REDIRECTS': False,
#         "SHOW_TOOLBAR_CALLBACK": show_toolbar,
#         'INSERT_BEFORE': '</head>',
#         'INTERCEPT_REDIRECTS': False,
#         'RENDER_PANELS': True,
#     }


# Config logs
from config.loggers import *
# import logging
# import logging.config
# from django.utils.log import DEFAULT_LOGGING

# logger = logging.getLogger(__name__)
# LOG_LEVEL = "INFO"
# DIR_LOGS = "logs/logs.production.log" if ENV == 'production' else "logs/logs.development.log"

# if os.path.isfile(DIR_LOGS):
#     logging.config.dictConfig(
#         {
#             "version": 1,
#             "disable_existing_loggers": False,
#             "formatters": {
#                 "console": {
#                     "format": "%(asctime)s %(name)-12s %(levelname)-8s %(message)s",
#                 },
#                 "file": {"format": "%(asctime)s %(name)-12s %(levelname)-8s %(message)s"},
#                 "django.server": DEFAULT_LOGGING["formatters"]["django.server"],
#             },
#             "handlers": {
#                 "console": {
#                     "class": "logging.StreamHandler",
#                     "formatter": "console",
#                 },
#                 "file": {
#                     "level": "INFO",
#                     "class": "logging.FileHandler",
#                     "formatter": "file",
#                     "filename": DIR_LOGS,
#                 },
#                 "django.server": DEFAULT_LOGGING["handlers"]["django.server"],
#             },
#             "loggers": {
#                 "": {"level": "INFO", "handlers": ["console", "file"], "propagate": False},
#                 "apps": {"level": "INFO", "handlers": ["console"], "propagate": False},
#                 "django.server": DEFAULT_LOGGING["loggers"]["django.server"],
#             },
#         }
#     )
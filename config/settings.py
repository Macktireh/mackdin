import os
import django_heroku
import dj_database_url
import cloudinary
import cloudinary.uploader
import cloudinary.api

from pathlib import Path
from dotenv import load_dotenv

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
load = load_dotenv(os.path.join(BASE_DIR, '.env'))

# Variable environment local or production
ENV = os.environ.get('ENV', 'development')


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY', 'sfdhvsnosgtrtvyt54g19hty1hd')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False if ENV == 'production' else True

ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS').split(" ") if os.environ.get('ALLOWED_HOSTS', []) != [] else ["127.0.0.1", "localhost"]

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
    'import_export'
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
    'django.contrib.sessions.middleware.SessionMiddleware',
    # 'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
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



# config database production settings
if ENV == 'production':
    DATABASES = {
        'default': dj_database_url.config()
    }
    
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
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


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_USER_MODEL = 'users.CustomUser'

# Config Send Email
EMAIL_BACKEND = os.environ.get('EMAIL_BACKEND')
EMAIL_HOST = os.environ.get('EMAIL_HOST')
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')
EMAIL_PORT= os.environ.get('EMAIL_PORT')
EMAIL_USE_TLS = os.environ.get('EMAIL_USE_TLS')


# Configure Django App for Heroku.
django_heroku.settings(locals(), test_runner=False)


# config cloudinary for production
cloudinary.config( 
    cloud_name = os.environ.get('CLOUD_NAME'), 
    api_key = os.environ.get('API_KEY'), 
    api_secret = os.environ.get('API_SECRET'),
)

# uid acces Interface Administrateur 
UID_ADMIN = os.environ.get('UID_ADMIN', 'admin-123')


# Django Debug Toolbar
if ENV == 'development':
    INSTALLED_APPS += [
        'debug_toolbar',
        'django_extensions',
        'rest_framework',
    ]
    MIDDLEWARE = ['debug_toolbar.middleware.DebugToolbarMiddleware'] + list(MIDDLEWARE)
    INTERNAL_IPS = ['127.0.0.1']

    import mimetypes
    mimetypes.add_type("application/javascript", ".js", True)

    DEBUG_TOOLBAR_PATCH_SETTINGS = False

    def show_toolbar(request):
        return True
        
    DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS': False,
    "SHOW_TOOLBAR_CALLBACK": show_toolbar,
    'INSERT_BEFORE': '</head>',
    'INTERCEPT_REDIRECTS': False,
    'RENDER_PANELS': True,
}


# Config logs
import logging
import logging.config
from django.utils.log import DEFAULT_LOGGING

logger = logging.getLogger(__name__)
LOG_LEVEL = "INFO"
DIR_LOGS = "logs/logs.production.log" if ENV == 'production' else "logs/logs.development.log"

if os.path.isfile(DIR_LOGS):
    logging.config.dictConfig(
        {
            "version": 1,
            "disable_existing_loggers": False,
            "formatters": {
                "console": {
                    "format": "%(asctime)s %(name)-12s %(levelname)-8s %(message)s",
                },
                "file": {"format": "%(asctime)s %(name)-12s %(levelname)-8s %(message)s"},
                "django.server": DEFAULT_LOGGING["formatters"]["django.server"],
            },
            "handlers": {
                "console": {
                    "class": "logging.StreamHandler",
                    "formatter": "console",
                },
                "file": {
                    "level": "INFO",
                    "class": "logging.FileHandler",
                    "formatter": "file",
                    "filename": DIR_LOGS,
                },
                "django.server": DEFAULT_LOGGING["handlers"]["django.server"],
            },
            "loggers": {
                "": {"level": "INFO", "handlers": ["console", "file"], "propagate": False},
                "apps": {"level": "INFO", "handlers": ["console"], "propagate": False},
                "django.server": DEFAULT_LOGGING["loggers"]["django.server"],
            },
        }
    )
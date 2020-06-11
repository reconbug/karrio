"""
Django settings for purpleserver project.

Generated by 'django-admin startproject' using Django 3.0.4.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os
import importlib
from django.urls import reverse_lazy
from django.templatetags.static import static
from django.utils.functional import lazy
from django.core.management.utils import get_random_secret_key

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY', get_random_secret_key())

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = bool(os.environ.get('DEBUG_MODE', True))

SECURE_DOMAIN = os.environ.get('SECURE', False)

ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', '*').split(',')

CORS_ORIGIN_ALLOW_ALL = True

if SECURE_DOMAIN:
    global SECURE_SSL_REDIRECT
    global SECURE_PROXY_SSL_HEADER

    SECURE_SSL_REDIRECT = True
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')


static_lazy = lazy(static, str)

# Application definition

PURPLSHIP_CONF = [app for app in [
    {'app': 'purpleserver.core', 'urls': 'purpleserver.core.urls'},
    {'app': 'purpleserver.proxy', 'urls': 'purpleserver.proxy.urls'},
    {'app': 'purpleserver.manager', 'urls': 'purpleserver.manager.urls'},
] if importlib.util.find_spec(app['app']) is not None]

PURPLSHIP_APPS = [cfg['app'] for cfg in PURPLSHIP_CONF]
PURPLSHIP_URLS = [cfg['urls'] for cfg in PURPLSHIP_CONF]

INSTALLED_APPS = [
    *PURPLSHIP_APPS,

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'rest_framework',
    'rest_framework.authtoken',

    'oauth2_provider',
    'drf_yasg',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'purpleserver.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'purpleserver', 'templates')],
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

WSGI_APPLICATION = 'purpleserver.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.{}'.format(os.getenv('DATABASE_ENGINE', 'sqlite3')),
        'NAME': os.getenv('DATABASE_NAME', 'db.sqlite3'),
        'USER': os.getenv('DATABASE_USERNAME'),
        'PASSWORD': os.getenv('DATABASE_PASSWORD'),
        'HOST': os.getenv('DATABASE_HOST'),
        'PORT': os.getenv('DATABASE_PORT'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

STATIC_URL = '/static/'

STATICFILES_DIRS = [os.path.join(BASE_DIR, 'purpleserver', 'static')]


# drf-yasg

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.TokenAuthentication',
        'oauth2_provider.contrib.rest_framework.OAuth2Authentication',
    ),
    'DEFAULT_THROTTLE_CLASSES': (
        'rest_framework.throttling.AnonRateThrottle',
        'rest_framework.throttling.UserRateThrottle'
    ),
    'DEFAULT_THROTTLE_RATES': {
        'anon': '40/minute',
        'user': '60/minute'
    },

    'DEFAULT_RENDERER_CLASSES': (
        'djangorestframework_camel_case.render.CamelCaseJSONRenderer',
        'djangorestframework_camel_case.render.CamelCaseBrowsableAPIRenderer',
    ),

    'DEFAULT_PARSER_CLASSES': (
        'djangorestframework_camel_case.parser.CamelCaseFormParser',
        'djangorestframework_camel_case.parser.CamelCaseMultiPartParser',
        'djangorestframework_camel_case.parser.CamelCaseJSONParser',
    ),
}

OAUTH2_CLIENT_ID = os.environ.get('OAUTH2_CLIENT_ID', get_random_secret_key())
OAUTH2_CLIENT_SECRET = os.environ.get('OAUTH2_CLIENT_SECRET', get_random_secret_key())
OAUTH2_APP_NAME = 'PurplShip OAuth2 provider'

OAUTH2_REDIRECT_URL = static_lazy('drf-yasg/swagger-ui-dist/oauth2-redirect.html')
OAUTH2_AUTHORIZE_URL = reverse_lazy('oauth2_provider:authorize')
OAUTH2_TOKEN_URL = reverse_lazy('oauth2_provider:token')

SWAGGER_SETTINGS = {
    'USE_SESSION_AUTH': False,
    'LOGIN_URL': reverse_lazy('admin:login'),
    'LOGOUT_URL': '/admin/logout',

    'DEFAULT_INFO': 'purpleserver.urls.swagger_info',

    'SECURITY_DEFINITIONS': {
        'Bearer': {
            'type': 'apiKey',
            'name': 'Authorization',
            'in': 'header'
        },
        'OAuth2 password': {
            'flow': 'password',
            'scopes': {
                'read': 'Read everything.',
                'write': 'Write everything,',
            },
            'tokenUrl': OAUTH2_TOKEN_URL,
            'type': 'oauth2',
        },
    },
    'OAUTH2_REDIRECT_URL': OAUTH2_REDIRECT_URL,
    'OAUTH2_CONFIG': {
        'clientId': OAUTH2_CLIENT_ID,
        'clientSecret': OAUTH2_CLIENT_SECRET,
        'appName': OAUTH2_APP_NAME,
    },
}

REDOC_SETTINGS = {
   'LAZY_RENDERING': False,
}

LOG_LEVEL = ('DEBUG' if DEBUG else os.getenv('LOG_LEVEL', 'INFO'))

# Logging configuration
LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'verbose': {
            'format': '{levelname} {asctime} {module} {process:d} {thread:d} {message}',
            'style': '{',
        },
        'simple': {
            'format': '{levelname} {message}',
            'style': '{',
        },
    },
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': os.path.join(os.getenv('LOG_PATH', ''), 'debug.log'),
        },
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'simple',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file', 'console'],
            'level': 'WARNING',
            'propagate': False,
        },
        'purplship': {
            'handlers': ['file', 'console'],
            'level': LOG_LEVEL,
            'propagate': False,
        },
        'purpleserver': {
            'handlers': ['file', 'console'],
            'level': LOG_LEVEL,
            'propagate': False,
        },
    },
}

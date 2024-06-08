import os
from pathlib import Path

from decouple import Config

config = Config('.env')

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

SECRET_KEY = config('SECRET_KEY', default='django-insecure-(^je%$!$p)$7u4(#lo1g@bzgyyd!_0j!o&9r!^!k8d4#bhqxwo',
                    cast=str)

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG', default=False, cast=bool)

ALLOWED_HOSTS = config('ALLOWED_HOSTS', default='', cast=str).split(' ')

# Get CSRF_TRUSTED_ORIGINS from environment variable, default to empty string
CSRF_TRUSTED_ORIGINS = config('CSRF_TRUSTED_ORIGINS', default=None, cast=str)

# Get CORS_ALLOW_ALL_ORIGINS from environment variable, default to empty string
CORS_ALLOWED_ORIGINS = config('CORS_ALLOWED_ORIGINS', default=None, cast=str)

if CSRF_TRUSTED_ORIGINS == '*':
    CSRF_TRUSTED_ORIGINS = ['http://*', 'https://*']
else:
    CSRF_TRUSTED_ORIGINS = CSRF_TRUSTED_ORIGINS.split(' ')

CORS_ALLOW_ALL_ORIGINS = False
if CORS_ALLOWED_ORIGINS == '*':
    CORS_ALLOW_ALL_ORIGINS = True
    CORS_ALLOWED_ORIGINS = ['http://*', 'https://*']
else:
    CORS_ALLOWED_ORIGINS = CORS_ALLOWED_ORIGINS.split(' ')

URL_PREFIX = config('URL_PREFIX', default='', cast=str)
if URL_PREFIX:
    URL_PREFIX = f'{URL_PREFIX}/'

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'corsheaders',
    'apps.users',
    'apps.authors',
    'apps.books',
    'apps.data_export'
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

ROOT_URLCONF = 'books_api_service.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'books_api_service.wsgi.application'

# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'HOST': config('POSTGRES_HOST', default='books-db', cast=str),
        'PORT': config('POSTGRES_PORT', default='5432', cast=str),
        'NAME': config('POSTGRES_DB', default='notes_db', cast=str),
        'USER': config('POSTGRES_USER', default='books_admin', cast=str),
        'PASSWORD': config('POSTGRES_PASSWORD', default='9874593784530', cast=str),
    }
}

# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
}

# REDIS
REDIS_HOST = config('REDIS_HOST', default='books-redis', cast=str)
REDIS_PORT = config('REDIS_PORT', default='6379', cast=str)
REDIS_DEFAULT_DB = config('REDIS_DEFAULT_DB', default='0', cast=str)

# Celery settings
CELERY_BROKER_URL = f'redis://{REDIS_HOST}:{REDIS_PORT}/{REDIS_DEFAULT_DB}'
CELERY_RESULT_BACKEND = f'redis://{REDIS_HOST}:{REDIS_PORT}/{REDIS_DEFAULT_DB}'
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TIMEZONE = 'UTC'

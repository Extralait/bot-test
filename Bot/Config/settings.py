import os
from datetime import timedelta

import dotenv
import logging.config
from pathlib import Path

# import django
# django.setup()

# Настройка окружения
BASE_DIR = Path(__file__).resolve().parent.parent

dotenv_file = os.path.join(BASE_DIR.parent, ".env.back")

if os.path.isfile(dotenv_file):
    dotenv.load_dotenv(dotenv_file)

# Базовые настройки приложения
SECRET_KEY = os.getenv('SECRET_KEY')

DEBUG = os.getenv('DEBUG')

PRODUCTION = os.getenv('PRODUCTION')

ROOT_URLCONF = 'Config.urls'

# ALLOWED_HOSTS = ["159.89.37.210", "host.docker.internal", "127.0.0.1", "localhost", "back", "web"]
ALLOWED_HOSTS = ['*']

LOGGING_CONFIG = None

LOGLEVEL = os.getenv('DJANGO_LOGLEVEL').upper()

logging.config.dictConfig({
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'console': {
            'format': '%(asctime)s %(levelname)s [%(name)s:%(lineno)s] %(module)s %(process)d %(thread)d %(message)s',
        },
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'console',
        },
    },
    'loggers': {
        '': {
            'level': LOGLEVEL,
            'handlers': ['console', ],
        },
    },
})

# Настройки языка и времени
LANGUAGE_CODE = os.getenv('LANGUAGE_CODE')

TIME_ZONE = os.getenv('TIME_ZONE')

USE_I18N = os.getenv('USE_I18N')

USE_L10N = os.getenv('USE_L10N')

USE_TZ = os.getenv('USE_TZ')

# Базовые настройки базы данных
DB_USER = os.getenv('DB_USER')

DB_USER_PASSWORD = os.getenv('DB_USER_PASSWORD')

DB_HOST = os.getenv('DB_HOST')

DB_NAME = os.getenv('DB_NAME')

DB_PORT = os.getenv('DB_PORT')

CONN_MAX_AGE = None

# Базовые настройки Celery
RABBITMQ_DEFAULT_USER = os.getenv('RABBITMQ_DEFAULT_USER')

RABBITMQ_DEFAULT_PASS = os.getenv('RABBITMQ_DEFAULT_PASS')

CELERY_BROKER_URL = f'pyamqp://{RABBITMQ_DEFAULT_USER}:{RABBITMQ_DEFAULT_PASS}@rabbit:5672/'

CELERY_ACCEPT_CONTENT = os.getenv('CELERY_ACCEPT_CONTENT').split(' ')

CELERY_TASK_SERIALIZER = os.getenv('CELERY_TASK_SERIALIZER')

CELERY_RESULT_SERIALIZER = os.getenv('CELERY_RESULT_SERIALIZER')

CELERYD_PREFETCH_MULTIPLIER = os.getenv('CELERYD_PREFETCH_MULTIPLIER')

CELERY_TIMEZONE = os.getenv('CELERY_TIMEZONE')

CELERY_CACHE_BACKEND = os.getenv('CELERY_CACHE_BACKEND')

CELERY_RESULT_BACKEND = os.getenv('CELERY_RESULT_BACKEND')

CELERY_CREATE_MISSING_QUEUES = os.getenv('CELERY_CREATE_MISSING_QUEUES')

CELERYD_MAX_TASKS_PER_CHILD = os.getenv('CELERYD_MAX_TASKS_PER_CHILD')

CELERY_BROKER_CONNECTION_RETRY = os.getenv('CELERY_BROKER_CONNECTION_RETRY')

CELERY_DISABLE_RATE_LIMITS = os.getenv('CELERY_DISABLE_RATE_LIMITS')

CELERY_BROKER_CONNECTION_MAX_RETRIES = os.getenv('CELERY_BROKER_CONNECTION_MAX_RETRIES')

# Настройки telegram bot
TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')

WEBHOOK_HOST = os.getenv('WEBHOOK_HOST')

WEBHOOK_PORT = os.getenv('WEBHOOK_PORT')

WEBHOOK_LISTEN = os.getenv('WEBHOOK_LISTEN')

WEBHOOK_SSL_CERT = os.getenv('WEBHOOK_SSL_CERT')

WEBHOOK_SSL_PRIV = os.getenv('WEBHOOK_SSL_PRIV')

# Настройки аккаунта админитратора
ADMINS = [
    {
        # 'ADMIN_NAME': os.getenv('ADMIN_NAME'),
        'ADMIN_EMAIL': os.getenv('ADMIN_EMAIL'),
        'ADMIN_PASSWORD': os.getenv('ADMIN_PASSWORD'),
    }
]

# Установленные приложения
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'rest_framework',
    'users',
    'users_messages',
    'telegram',
    'whitenoise.runserver_nostatic',
    'django.contrib.staticfiles',
    'django_celery_beat',
    'django_celery_results',
    'corsheaders',
]

# Промежуточные слои
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
]

# Настройки шаблонизатора
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates']
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                # 'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

TEMPLATE_LOADERS = [
    # Loads templates from DIRS setting:
    'django.template.loaders.filesystem.Loader',

    # Loads templates from your installed apps:
    'django.template.loaders.app_directories.Loader',
]

# Настройка запуска приложения
ASGI_APPLICATION = 'Config.asgi.application'

# Настройка базы данных
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': DB_NAME,
        'USER': DB_USER,
        'PASSWORD': DB_USER_PASSWORD,
        'HOST': DB_HOST,
        'PORT': DB_PORT,
    }
}

# Настройка медиафайлов и статики
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

STATIC_URL = '/static/'

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(os.path.dirname(BASE_DIR), "media")

# Переопределение стандартного пользователя
AUTH_USER_MODEL = 'users.User'

# Настройки CORS заголовков
CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = True

# Директория файлов заполнения базы данных из JSON
FIXTURE_DIRS = [
    '/fixtures/'
]


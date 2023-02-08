"""
Django settings for Core project.

Generated by 'django-admin startproject' using Django 3.2.16.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""
import os
from pathlib import Path

from celery.schedules import crontab
import Tasks.tasks


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

##################################################################################################
#                                 Docker Secret Key Setting                                      #
##################################################################################################

#SECRET_KEY = os.environ.get("SECRET_KEY")


##################################################################################################
#                                 Venv Secret Key setting                                        #
##################################################################################################

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-okc1n%x5k8_=a_dag$75a55g_#rpg&**^76x5mu@fp^xsxxqs&'


##################################################################################################
#                                 Docker Debug Setting                                           #
###################################################################################################

#DEBUG = int(os.environ.get("DEBUG", default=0))


##################################################################################################
#                                 Venv Debug Setting                                             #
##################################################################################################

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True


##################################################################################################
#                                 Docker Allowed Host setting                                    #
##################################################################################################

#ALLOWED_HOSTS = os.environ.get("DJANGO_ALLOWED_HOSTS").split(" ")


##################################################################################################
#                                 Venv Allowed Host setting                                      #
##################################################################################################

# 'DJANGO_ALLOWED_HOSTS' should be a single string of hosts with a space between each.
# For example: 'DJANGO_ALLOWED_HOSTS=localhost 127.0.0.1 [::1]'

ALLOWED_HOSTS = ['127.0.0.1', 'localhost']


##################################################################################################
#                                       Installed Apps                                           #
##################################################################################################

# Application definition

INSTALLED_APPS = [
    # Core Applications
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # 3rd party Packages
    'import_export',          ### adds import/export capability in admin
    'django_celery_results',  ### adds celery tasks to django admin

    # My applications
    'Registration',
    'UI',
    'Data',
    'Devices',
    'Profiles',
    'Security',
    'Tasks',
    'Test',
    'Web',
]


##################################################################################################
#                                       Middleware                                               #
##################################################################################################

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


##################################################################################################
#                                       Root URLConf                                             #
##################################################################################################

ROOT_URLCONF = 'Core.urls'


##################################################################################################
#                                          Templates                                             #
##################################################################################################

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]


##################################################################################################
#                                         Webserver                                              #
##################################################################################################

WSGI_APPLICATION = 'Core.wsgi.application'


##################################################################################################
#                                    Database Configurations                                     #
##################################################################################################

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


##################################################################################################
#                                   Password Configurations                                      #
##################################################################################################

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


##################################################################################################
#                              Internationalization Configuration                                #
##################################################################################################

# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


##################################################################################################
#                                     Static Configurations                                      #
##################################################################################################

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/' # only for production use
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
STATICFILES_DIRS = (os.path.join('static'), ) #


##################################################################################################
#                                       Media Configuration                                      #
##################################################################################################

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')

X_FRAME_OPTIONS = 'SAMEORIGIN'  ## Set this to ensure that Rich Field Text Editor for django_summernote runs. Otherwise it will show a blank space where its editor is supposed to appear.


##################################################################################################
#                                       Redis Configuration                                      #
##################################################################################################

REDISBOARD_DETAIL_FILTERS = ['uptime.*', 'db.*', '.*']
REDISBOARD_ITEMS_PER_PAGE = 100
REDISBOARD_SOCKET_TIMEOUT = None
REDISBOARD_SOCKET_CONNECT_TIMEOUT = None
REDISBOARD_SOCKET_KEEPALIVE = None
REDISBOARD_SOCKET_KEEPALIVE_OPTIONS = None


##################################################################################################
#                                       Celery Configuration                                     #
##################################################################################################

BROKER_URL = 'redis://localhost:6379'
#CELERY_RESULT_BACKEND = 'redis://localhost:6379'  ### Original setting
CELERY_RESULT_BACKEND = 'django-db'   ### Test Configuration for adding celery tasks to django admin
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TIMEZONE = 'UTC'
CELERY_BROKER_URL = 'redis://redis:6379'
CELERY_RESULT_EXTENDED = True # https://docs.celeryq.dev/en/stable/userguide/configuration.html#result-extended


CELERY_BEAT_SCHEDULE = {
    "sample_task": {
        "task": "Tasks.tasks.sample_task",
        "schedule": crontab(minute="*/1"),
    },
    "send_email_report": {
        "task": "Tasks.tasks.send_email_report",
        "schedule": crontab(hour="*/1"),
    },
    "testapicalls": {
        "task": "Tasks.tasks.testapicalls",
        "schedule": crontab(minute="*/1"),
    },
    "testapicalls2": {
        "task": "Tasks.tasks.testapicalls2",
        "schedule": crontab(minute="*/1"),
    },
}


##################################################################################################
#                                 Backend Email Configuration                                    #
##################################################################################################

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
DEFAULT_FROM_EMAIL = "noreply@email.com"
ADMINS = [("testuser", "test.user@email.com"), ]


##################################################################################################
#                                 Emporium Security Configuration                                #
##################################################################################################

# Emporium Source for Emporium Settings Files for the more advanced settings.py options reference: https://github.com/doismellburning/emporium/blob/master/emporium/emporium/settings.py

    # Security Settings Configuration for both Development & Production

# REFERRER_POLICY = "strict-origin-when-cross-origin"
#
# CSP_DEFAULT_SRC = ("'self'", "'unsafe-inline'", "https:")  # TODO Fix these!
#
#
# if not DEBUG:
#     CSRF_COOKIE_SECURE = True
#     SECURE_BROWSER_XSS_FILTER = True
#     SECURE_CONTENT_TYPE_NOSNIFF = True
#     SECURE_HSTS_INCLUDE_SUBDOMAINS = True
#     SECURE_HSTS_PRELOAD = True
#     SECURE_HSTS_SECONDS = 2592000
#     SECURE_SSL_REDIRECT = True
#     SESSION_COOKIE_SECURE = True
#     X_FRAME_OPTIONS = "DENY"

### Setting for Auth imported from Profiles API
# AUTH_USER_MODEL = 'profiles_api.UserProfile'


##################################################################################################
#                                Misc Performance Configurations                                 #
##################################################################################################

DATA_UPLOAD_MAX_NUMBER_FIELDS = 10240  ## higher than the count of fields desired to be uploaded

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


####################################   End of Configuration   ####################################
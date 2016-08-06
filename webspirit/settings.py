# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import os
import sys
import dj_database_url

from spirit.settings import *

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "hf0x^6q!)z%%blce^ru%h&e8=9amit=yil1wx%sz&b9$1cw_0("

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# This will be the default in next version
ST_RATELIMIT_CACHE = 'st_rate_limit'


# Extend the Spirit installed apps.
# Check out the spirit.settings.py so you do not end up with duplicated apps.
INSTALLED_APPS.extend([
	# 'my_app1',
	# 'my_app2',
])

# same here, check out the spirit.settings.py
MIDDLEWARE_CLASSES.extend([
	# 'my_middleware1',
	# 'my_middleware2',
])

# same here
TEMPLATES[0]['OPTIONS']['context_processors'].extend([
	# 'my_template_proc1',
	# 'my_template_proc2',
])

# same here (we update the Spirit caches)
CACHES.update({
	'st_rate_limit': {
		'BACKEND': CACHES['default']['BACKEND'],
		'LOCATION': 'spirit_rl_cache',
		'TIMEOUT': None
	}
})

ST_COMMENT_MAX_LEN = 3000
# Application definition

"""
INSTALLED_APPS = (
	'django.contrib.admin',
	'django.contrib.auth',
	'django.contrib.contenttypes',
	'django.contrib.sessions',
	'django.contrib.messages',
	'django.contrib.staticfiles',
	'spirit',
)

MIDDLEWARE_CLASSES = (
	'django.contrib.sessions.middleware.SessionMiddleware',
	'django.middleware.common.CommonMiddleware',
	'django.middleware.csrf.CsrfViewMiddleware',
	'django.contrib.auth.middleware.AuthenticationMiddleware',
	'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
	'django.contrib.messages.middleware.MessageMiddleware',
	'django.middleware.clickjacking.XFrameOptionsMiddleware',
	'django.middleware.security.SecurityMiddleware',
)
"""
ROOT_URLCONF = 'webspirit.urls'

"""
TEMPLATES = (
	{
		'BACKEND': 'django.template.backends.django.DjangoTemplates',
		'DIRS': [os.path.join(BASE_DIR, 'templates')],
		'APP_DIRS': True,
		'OPTIONS': {
			'context_processors': [
				'django.template.context_processors.debug',
				'django.template.context_processors.request',
				'django.contrib.auth.context_processors.auth',
				'django.contrib.messages.context_processors.messages',
			],
			'debug': DEBUG,
		},
	},
)"""

WSGI_APPLICATION = 'webspirit.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases


DATABASES = {
	'default': {
		'ENGINE': 'django.db.backends.sqlite3',
		'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
	}
}
"""
DATABASES = {
	'default': {
		'ENGINE': 'django.db.backends.postgresql_psycopg2',
		'NAME': 'd1oitk3ih8b8ps',
		'USER': 'huukhwhjqfimaf',
		'PASSWORD': '0_wUgKoN2zfJreReGY0frXpDwX',
		'HOST': 'ec2-54-243-249-154.compute-1.amazonaws.com',
		'PORT': '5432',
	}
}
"""

AUTH_PASSWORD_VALIDATORS = (
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
)

# Internationalization
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'es'
TIME_ZONE = 'America/Lima'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Update database configuration with $DATABASE_URL.
db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)



# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Allow all host headers
ALLOWED_HOSTS = ['*']

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'

# Extra places for collectstatic to find static files.
STATICFILES_DIRS = [
	os.path.join(BASE_DIR, 'static'),
]

# Simplified static file serving.
# https://warehouse.python.org/project/whitenoise/
STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'



MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')



# Send an email to the site admins
# on error when DEBUG=False,
# log to console on error always.
"""LOGGING = {
	'version': 1,
	'disable_existing_loggers': False,
	'filters': {
		'require_debug_false': {
			'()': 'django.utils.log.RequireDebugFalse'
		}
	},
	'handlers': {
		'mail_admins': {
			'class': 'django.utils.log.AdminEmailHandler',
			'filters': ['require_debug_false'],
		},
		'console': {
			'class': 'logging.StreamHandler',
		},
		'file': {
			'class': 'logging.FileHandler',
			'filename': os.path.join(BASE_DIR, 'django.log'),
		},
	},
	'loggers': {
		'': {
			'handlers': ['console', 'mail_admins'],
			'level': 'ERROR',
			'propagate': False,
		},
		'django': {
			'handlers': ['console', 'mail_admins'],
			'level': 'ERROR',
			'propagate': False,
		},
	}
}
"""
"""
# https://docs.djangoproject.com/en/dev/ref/settings/#admins
ADMINS = (('John', 'john@example.com'), )

# You can change this to something like 'MyForum <noreply@example.com>'
DEFAULT_FROM_EMAIL = 'webmaster@localhost'  # Django default
SERVER_EMAIL = DEFAULT_FROM_EMAIL  # For error notifications

# https://docs.djangoproject.com/en/dev/ref/settings/#databases
"""


CACHES.update({
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    },
    'st_rate_limit': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': 'spirit_rl_cache',
        'TIMEOUT': None
    }
})

PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.MD5PasswordHasher',
]

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

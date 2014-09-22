"""
Django settings for a2c project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True


# SECURITY WARNING: keep the secret key used in production secret!
if not DEBUG:
    SECRET_KEY = os.environ['SECRET_KEY']



TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []



ADMINS = (
    # ('Your Name', 'your_email@domain.com'),
)

MANAGERS = ADMINS


# Application definition

INSTALLED_APPS = (
    'a2c',
    'django.contrib.admin',
    'django.contrib.auth',
    #'django.contrib.sites',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'creditcard',
    'accounts',
    'apps',
    'feincms',
    'feincms.module.blog',
    'feincms.module.page',
    'feincms.module.medialibrary',  

    'mptt',
    'registration',
    'south',
    'easy_thumbnails',
    'plans',
    'localflavor',
    #'getpaid',

)

if DEBUG:
    INSTALLED_APPS+=('debug_toolbar',)
    
ACCOUNT_ACTIVATION_DAYS = 7 # One-week activation window; you may, of course, use a different value.

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.request',
    'django.core.context_processors.static',
    'plans.context_processors.account_status',

    'feincms.context_processors.add_page_if_missing',
)


MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)



TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

ROOT_URLCONF = 'a2c.urls'

WSGI_APPLICATION = 'a2c.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': '',
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')
MEDIA_URL = '/media/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static/')
STATIC_URL = '/static/'


# Easy Thumbnails

SOUTH_MIGRATION_MODULES = {
    'easy_thumbnails': 'easy_thumbnails.south_migrations',
}


# Django Plan

CURRENCY = 'USD'

DEFAULT_FROM_EMAIL='example@example.com' # need to be changed before production

INVOICE_COUNTER_RESET = 'yearly'

INVOICE_NUMBER_FROMAT = "{{ invoice.number }}/{{ invoice.issued|date='m/FV/Y' }}"

INVOICE_TEMPLATE = 'plans/invoices/PL_EN.html'

PLAN_EXPIRATION_REMIND = [1, 3 , 7]

from decimal import Decimal
TAX = Decimal(8.75) #for 8.75% VAT

ISSUER_DATA = {
    "issuer_name": "App2China",
    "issuer_street": "Django street, 34",
    "issuer_zipcode": "123-3444",
    "issuer_city": "Djangoko",
    "issuer_country": "Djangoland",
    "issuer_tax_number": "1222233334444555",
}


TAXATION_POLICY='plans.taxation.EUTaxationPolicy'



try:
    from local_settings import *
except ImportError:
    pass
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
DEBUG = False


# SECURITY WARNING: keep the secret key used in production secret!
if not DEBUG:
    SECRET_KEY = os.environ['SECRET_KEY']



TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = []



ADMINS = (
    ('app2china', 'app2china@gmail.com'),
)

MANAGERS = ADMINS


# Application definition

INSTALLED_APPS = (
    'a2c',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.sites',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    #'creditcard',
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
    #'debug_toolbar',
    'storages',
    'paypal.standard.ipn',
    #'paypal.standard.pdt',
    #'paypal_express_checkout',
)

SITE_ID=1

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
    'accounts.context_processors.contact_status',
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

CACHES={
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    }
}
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

LOGIN_REDIRECT_URL='/accounts/info/'

# Easy Thumbnails

SOUTH_MIGRATION_MODULES = {
    'easy_thumbnails': 'easy_thumbnails.south_migrations',
}


# Django Plan

CURRENCY = 'USD'

TAX_COUNTRY = 'USA'

DEFAULT_FROM_EMAIL='app2china@gmail.com' # need to be changed before production

#INVOICE_COUNTER_RESET = 'annually'

PLAN_DEFAULT_GRACE_PERIOD = 90

INVOICE_NUMBER_FROMAT = "{{ invoice.number }}/{{ invoice.issued|date='m/FV/Y' }}"

TAXATION_POLICY='accounts.USA.USATaxationPolicy'

INVOICE_TEMPLATE = 'plans/invoices/PL_EN.html'

PLAN_EXPIRATION_REMIND = [1, 3 , 7]

from decimal import Decimal
TAX = Decimal(0.00) #for 8.75% VAT

ISSUER_DATA = {
    "issuer_name": "App2China",
    "issuer_street": " ",
    "issuer_zipcode": " ",
    "issuer_city": " ",
    "issuer_country": " ",
    "issuer_tax_number": " ",
}


PLAN_VALIDATORS = {
    'MAX_APP_COUNT': 'apps.validators.max_apps_validator',
    'MAX_APPUPDATE_COUNT': 'apps.validators.max_appupdates_validator',
}

PLAN_CHANGE_POLICY = 'accounts.plan_change.StandardPlanChangePolicy'


# Amazon S3

if not DEBUG:
    
    DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
    
    AWS_ACCESS_KEY_ID=os.environ['AWS_ACCESS_KEY_ID']
    
    AWS_SECRET_ACCESS_KEY=os.environ['AWS_SECRET_ACCESS_KEY']
    
    AWS_STORAGE_BUCKET_NAME='app2china'
    
    #STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
    AWS_QUERYSTRING_AUTH = False
    
    AWS_HEADERS = {
    'Expires': 'Thu, 15 Apr 2010 20:00:00 GMT',
    'Cache-Control': 'max-age=86400',
    }
    

# # Django paypal express checkout

# HOSTNAME = 'http://a2c-c9-johnlizenith.c9.io'  # without trailing slash

# SALE_DESCRIPTION = 'Your payment to App2China'

if DEBUG:
    PAYPAL_RECEIVER_EMAIL = 'john.li-facilitator_api1.zen-tec.us'
    # PAYPAL_PWD = 'HS97YCWJTFLZX4N8'
    PAYPAL_IDENTITY_TOKEN = 'AFcWxV21C7fd0v3bYYYRCpSSRl31AvwB3D9piSVkDQrMvBpz09iPKC2-'



# Django Paypal

if not DEBUG:
    PAYPAL_IDENTITY_TOKEN=os.environ['PAYPAL_IDENTITY_TOKEN']
    PAYPAL_TEST = False
    PAYPAL_RECEIVER_EMAIL = os.environ['PAYPAL_RECEIVER_EMAIL']

# Sendgrid

if not DEBUG:
    EMAIL_HOST = 'smtp.sendgrid.net'
    EMAIL_HOST_USER = os.environ['SENDGRID_USERNAME']
    EMAIL_HOST_PASSWORD = os.environ['SENDGRID_PASSWORD']
    EMAIL_PORT = 587
    EMAIL_USE_TLS = True
    

# Heroku settings
if not DEBUG:
    # Parse database configuration from $DATABASE_URL
    import dj_database_url
    DATABASES['default'] =  dj_database_url.config()

    # Honor the 'X-Forwarded-Proto' header for request.is_secure()
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

    # Allow all host headers
    ALLOWED_HOSTS = ['*']
    
    import os
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    STATIC_ROOT = 'staticfiles'
    STATIC_URL = '/static/'

    STATICFILES_DIRS = (
        os.path.join(BASE_DIR, 'static'),
    )



try:
    from local_settings import *
except ImportError:
    pass
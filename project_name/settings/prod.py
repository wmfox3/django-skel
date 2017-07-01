"""Production settings and globals."""


from os import environ

from memcacheify import memcacheify
from postgresify import postgresify
#from S3 import CallingFormat

from common import *

from decouple import config, Csv

########## EMAIL CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-backend
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-host
EMAIL_HOST = environ.get('EMAIL_HOST', 'smtp.gmail.com')

# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-host-password
EMAIL_HOST_PASSWORD = environ.get('EMAIL_HOST_PASSWORD', '')

# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-host-user
EMAIL_HOST_USER = environ.get('EMAIL_HOST_USER', 'your_email@example.com')

# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-port
EMAIL_PORT = environ.get('EMAIL_PORT', 587)

# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-subject-prefix
EMAIL_SUBJECT_PREFIX = '[%s] ' % SITE_NAME

# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-use-tls
EMAIL_USE_TLS = True

# See: https://docs.djangoproject.com/en/dev/ref/settings/#server-email
SERVER_EMAIL = EMAIL_HOST_USER
########## END EMAIL CONFIGURATION


########## DATABASE CONFIGURATION
DATABASES = postgresify()
########## END DATABASE CONFIGURATION


########## CACHE CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#caches
CACHES = memcacheify()
########## END CACHE CONFIGURATION


########## CELERY CONFIGURATION
# See: http://docs.celeryproject.org/en/latest/configuration.html#broker-transport
BROKER_TRANSPORT = 'amqplib'

# Set this number to the amount of allowed concurrent connections on your AMQP
# provider, divided by the amount of active workers you have.
#
# For example, if you have the 'Little Lemur' CloudAMQP plan (their free tier),
# they allow 3 concurrent connections. So if you run a single worker, you'd
# want this number to be 3. If you had 3 workers running, you'd lower this
# number to 1, since 3 workers each maintaining one open connection = 3
# connections total.
#
# See: http://docs.celeryproject.org/en/latest/configuration.html#broker-pool-limit
BROKER_POOL_LIMIT = 3

# See: http://docs.celeryproject.org/en/latest/configuration.html#broker-connection-max-retries
BROKER_CONNECTION_MAX_RETRIES = 0

# See: http://docs.celeryproject.org/en/latest/configuration.html#broker-url
BROKER_URL = environ.get('RABBITMQ_URL') or environ.get('CLOUDAMQP_URL')

# See: http://docs.celeryproject.org/en/latest/configuration.html#celery-result-backend
CELERY_RESULT_BACKEND = 'amqp'
########## END CELERY CONFIGURATION


########## STORAGE CONFIGURATION
# See: http://django-storages.readthedocs.org/en/latest/index.html
INSTALLED_APPS += (
    'storages',
)

# See: http://django-storages.readthedocs.org/en/latest/backends/amazon-S3.html#settings
#STATICFILES_STORAGE = DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
STATICFILES_STORAGE = 'misc.custom_storages.StaticCachedS3BotoStorage'
DEFAULT_FILE_STORAGE = 'misc.custom_storages.MediaS3BotoStorage'

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# See: http://django-storages.readthedocs.org/en/latest/backends/amazon-S3.html#settings
#AWS_CALLING_FORMAT = CallingFormat.SUBDOMAIN

# See: http://django-storages.readthedocs.org/en/latest/backends/amazon-S3.html#settings
#AWS_ACCESS_KEY_ID = environ.get('AWS_ACCESS_KEY_ID', '')
AWS_ACCESS_KEY_ID = config('AWS_ACCESS_KEY_ID')
#AWS_SECRET_ACCESS_KEY = environ.get('AWS_SECRET_ACCESS_KEY', '')
AWS_SECRET_ACCESS_KEY = config('AWS_SECRET_ACCESS_KEY')
#AWS_STORAGE_BUCKET_NAME = environ.get('AWS_STORAGE_BUCKET_NAME', '')
AWS_STORAGE_BUCKET_NAME = config('AWS_STORAGE_BUCKET_NAME')

AWS_S3_CUSTOM_DOMAIN = '{0}.s3.amazonaws.com'.format(AWS_STORAGE_BUCKET_NAME)

AWS_AUTO_CREATE_BUCKET = True
AWS_QUERYSTRING_AUTH = False

# AWS cache settings, don't change unless you know what you're doing:
AWS_EXPIRY = 60 * 60 * 24 * 7
AWS_HEADERS = {
    'Cache-Control': 'max-age=%d, s-maxage=%d, must-revalidate' % (AWS_EXPIRY,
        AWS_EXPIRY)
}

# See: https://docs.djangoproject.com/en/dev/ref/settings/#static-url
#STATIC_URL = 'https://s3.amazonaws.com/%s/' % AWS_STORAGE_BUCKET_NAME
STATIC_URL = 'https://{0}/static/'.format(AWS_S3_CUSTOM_DOMAIN)
MEDIA_URL = 'https://{0}/media/'.format(AWS_S3_CUSTOM_DOMAIN)

########## END STORAGE CONFIGURATION


########## COMPRESSION CONFIGURATION
# See: http://django_compressor.readthedocs.org/en/latest/settings/#django.conf.settings.COMPRESS_OFFLINE
COMPRESS_OFFLINE = True

# See: http://django_compressor.readthedocs.org/en/latest/settings/#django.conf.settings.COMPRESS_STORAGE
COMPRESS_STORAGE = STATICFILES_STORAGE
COMPRESS_URL = STATIC_URL

# See: http://django_compressor.readthedocs.org/en/latest/settings/#django.conf.settings.COMPRESS_CSS_FILTERS
#COMPRESS_CSS_FILTERS += [
#    'compressor.filters.cssmin.CSSMinFilter',
#]

# See: http://django_compressor.readthedocs.org/en/latest/settings/#django.conf.settings.COMPRESS_JS_FILTERS
COMPRESS_JS_FILTERS += [
    'compressor.filters.jsmin.JSMinFilter',
]
########## END COMPRESSION CONFIGURATION

########## BOWER CONFIGURATION
# perhaps the heroku bower path needs to be different from the dev path
BOWER_PATH = '/app/node_modules/.bin/bower'
########## END BOWER CONFIGURATION

########## SECRET CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#secret-key
SECRET_KEY = environ.get('SECRET_KEY', SECRET_KEY)
########## END SECRET CONFIGURATION

########## ALLOWED HOSTS CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#allowed-hosts
ALLOWED_HOSTS = ['.herokuapp.com']
#ALLOWED_HOSTS = config('ALLOWED_HOSTS', cast=Csv())
########## END ALLOWED HOST CONFIGURATION

import dj_database_url
DATABASES['default'] =  dj_database_url.config()
DATABASES['default']['ENGINE'] = 'django.contrib.gis.db.backends.postgis'

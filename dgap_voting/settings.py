
"""
Django settings for dgap_voting project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

TEMPLATE_DIRS = ()
TEMPLATE_DIRS += (os.path.join(BASE_DIR, 'templates'),)

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'gp9e%(8c5)^-738+ha==f1-&3j8@3@xpruk)1cxvfsg@%35f8@'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = ["canetoad.mooo.com"]


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'registration',
    'bootstrap3',
    'polls',
    'django_user_agents',
    'django_bleach',
    'social.apps.django_app.default',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.tz',
    'django.contrib.messages.context_processors.messages',
    'social.apps.django_app.context_processors.backends',
    'social.apps.django_app.context_processors.login_redirect',
)

AUTHENTICATION_BACKENDS = (
    'social.backends.google.GoogleOAuth2',
    'django.contrib.auth.backends.ModelBackend',
)

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:11211',
    }
}

#BOOTSTRAP3 = {
#    'include_jquery': True,  
#}

SENDFILE_BACKEND = 'sendfile.backends.development'

SITE_ID = 1

ACCOUNT_ACTIVATION_DAYS = 7

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django_user_agents.middleware.UserAgentMiddleware',
    #'social.apps.django_app.middleware.SocialAuthExceptionMiddleware',
    'polls.psa.SocialAuthExceptionMiddlewareExtended',
)

ROOT_URLCONF = 'dgap_voting.urls'

WSGI_APPLICATION = 'dgap_voting.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

# SECURITY WARNING: don't run with this passwords in production!

DATABASE_ROUTERS = ['polls.routers.ModelDatabaseRouter']

DATABASES = {
    'default': {
        'ENGINE':'django.db.backends.postgresql_psycopg2',
        'NAME': 'dgap_voting_db',
        'USER': 'postgres',
        'PASSWORD': 'postgres2014', 
        'HOST': '127.0.0.1',
        'PORT': '5432',
    },
    'legacy_users': {
        'ENGINE': 'mysql.connector.django',
        'NAME': 'wow',
        'USER': 'root',
        'PASSWORD': 'gsogso;;;',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}


# Bleach default settings
BLEACH_ALLOWED_TAGS = ['b', 'i', 'u', 's', 'a', 'p', 'div', 'ul', 'li', 'img', 'h1', 'h2', 'h3']

BLEACH_ALLOWED_ATTRIBUTES = ['href', 'title', 'style', 'src', 'align']

# Which CSS properties are allowed in 'style' attributes (assuming style is
# an allowed attribute)
BLEACH_ALLOWED_STYLES = ['font-size', 'color', 'height', 'width']

# Strip unknown tags if True, replace with HTML escaped characters if False
BLEACH_STRIP_TAGS = False

# To strip HTML comments, or not to strip?
BLEACH_STRIP_COMMENTS = False


# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'Europe/Moscow'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

MEDIA_ROOT = (os.path.join(BASE_DIR, 'media'))
SENDFILE_ROOT = MEDIA_ROOT
STATIC_ROOT = (os.path.join(BASE_DIR, 'static'))
STATIC_URL = '/static/'
LOGIN_REDIRECT_URL = '/'

SOCIAL_AUTH_GOOGLE_OAUTH2_WHITELISTED_DOMAINS = ['phystech.edu']

SOCIAL_AUTH_LOGIN_ERROR_URL = 'polls:done'

SOCIAL_AUTH_PIPELINE = (
    'social.pipeline.social_auth.social_details',
    'social.pipeline.social_auth.social_uid',
    'social.pipeline.social_auth.auth_allowed',
    'social.pipeline.social_auth.social_user',
    'social.pipeline.user.get_username',
    'social.pipeline.user.create_user',
    'social.pipeline.social_auth.associate_user',
    'social.pipeline.social_auth.load_extra_data',
    'social.pipeline.user.user_details',
    'polls.psa.cut_firstname',  # cut firstname from mixed name from phystech.edu
)


from dgap_voting.local_settings import *

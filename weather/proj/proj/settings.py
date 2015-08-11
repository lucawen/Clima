"""
Django settings for proj project.

Generated by 'django-admin startproject' using Django 1.8.3.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

print BASE_DIR

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'y@bzrocszm8#r_cyt@gsof+#29kcufqv6@z#l*7z@_e!5m8boj'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'grappelli',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'normais',
    'automaticas',
    'django_extensions',
    
    
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

ROOT_URLCONF = 'proj.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR+'/templates/'], 
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.core.context_processors.request',
            ],
        },
    },
]

WSGI_APPLICATION = 'proj.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2', 
        'NAME': 'FireMonitor',                      
        'USER': 'postgres',
        'PASSWORD': 'wilci5w7',
        'HOST': '10.3.0.29',                   
        'PORT': '5432',                     
    }
}


STATICFILES_DIRS = (
    BASE_DIR+ "/normal/static/plugins/",
    BASE_DIR+ "/normal/static/css/",
    BASE_DIR+ "/normal/static/js/",
    BASE_DIR+ "/normal/static/img/",
    BASE_DIR+ "/normal/static/js//typeahead/",
    BASE_DIR+ "/normal/static/fonts/",
    BASE_DIR+ "/normal/static/plugins/bootstrap/",
    BASE_DIR+ "/normal/static/plugins/bootstrapvalidator/",
    BASE_DIR+ "/normal/static/plugins/d3/",
    BASE_DIR+ "/normal/static/plugins/fatatables/",
    BASE_DIR+ "/normal/static/plugins/fancybox/",
    BASE_DIR+ "/normal/static/plugins/fineuploader/",
    BASE_DIR+ "/normal/static/plugins/flot/",
    BASE_DIR+ "/normal/static/plugins/fullcalendar/",
    BASE_DIR+ "/normal/static/plugins/jquery/",
    BASE_DIR+ "/normal/static/plugins/jQuery-Knob/",
    BASE_DIR+ "/normal/static/plugins/jquery-ui/",
    BASE_DIR+ "/normal/static/plugins/jquery-ui-timepicker-addon/",
    BASE_DIR+ "/normal/static/plugins/justified-gallery/",
    BASE_DIR+ "/normal/static/plugins/moment/",
    BASE_DIR+ "/normal/static/plugins/morris/",
    BASE_DIR+ "/normal/static/plugins/raphael/",
    BASE_DIR+ "/normal/static/plugins/select2/",
    BASE_DIR+ "/normal/static/plugins/sparkline/",
    BASE_DIR+ "/normal/static/plugins/tinymce/",
    BASE_DIR+ "/normal/static/plugins/xcharts/"
)


LANGUAGE_CODE = 'pt-br'
ugettext = lambda s: s
LANGUAGES = (
    ('en', ugettext('English')),
    ('pt', ugettext('Portugues')),
)

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


GRAPPELLI_ADMIN_TITLE= u'FIRE-MONITOR -  Terravision'

STATIC_URL = '/static/'

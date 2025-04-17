
from pathlib import Path
import os
from decouple import config


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

#DEFINITION DU CHEMIN D'ACCES AUX FICHIERS DE NOTRE PROJET. ON CREE LE DOSSIER TEMPLATES
TEMPLATES_DIR=os.path.join(BASE_DIR,('templates'))


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-1vq*7@n01p*^oro(0#wv82qk(2h9^4$4kos0n=8-)#*^a7*+^k'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'sigim.apps.SigimConfig',
    'rest_framework',
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

ROOT_URLCONF = 'gvictoire.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATES_DIR],
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

WSGI_APPLICATION = 'gvictoire.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


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


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/
#DENITION DU CHEMIN D'ACCES AUX FICHIERS STATICS: On cree le dossier des medias dans le projet
#STATIC_URL = '/static/'
##STATIC_URL = "static/"
##STATICFILES_DIRS=["static"]
##MEDIA_URL="images/"
##MEDIA_ROOT=os.path.join(BASE_DIR,"images/")
#MEDIA_ROOT=BASE_DIR,'images/'

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')  # pour collectstatic (prod)
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]  # pour dev


# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


#Envoi de mail. A supprimer en cas de deploiement de l'application
#EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
"""
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'kobenanwykys@gmail.com'
EMAIL_HOST_PASSWORD ='Microsoft1995@#'
EMAIL_PORT ='587'
EMAIL_USE_TLS = True
"""
EMAIL_BACKEND='django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST= config('EMAIL_HOST')
EMAIL_PORT = config('EMAIL_PORT')
EMAIL_HOST_USER = config('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')
EMAIL_USE_TLS = config('EMAIL_USE_TLS')

ANYMAIL = {
    "SENDINBLUE_API_KEY": "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",
}


#REST_FRAMEWORK POUR LA CREATION DES API
REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ]
}
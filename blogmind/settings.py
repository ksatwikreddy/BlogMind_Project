# blogmind/settings.py (NEW FILE)
"""
Django settings for blogmind project.
"""

from pathlib import Path
import os # Keep this if you used os.path.join elsewhere

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-some-random-key' # Use your actual secret key here


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1', 'localhost'] # Add this back!


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'core', # Re-add your custom app
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

# 🌟 CRITICAL LINE 1: MUST be correct
ROOT_URLCONF = 'blogmind.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

# 🌟 CRITICAL LINE 2: MUST be correct
WSGI_APPLICATION = 'blogmind.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# ... (omitted for brevity)


# Internationalization
# ... (omitted for brevity)


# blogmind/settings.py

# ... (usually located near STATIC_URL)

# 🌟 CRITICAL FIX: The absolute path to the directory where collectstatic will gather files.
# This creates a folder named 'staticfiles' in your project's root directory.
# blogmind/settings.py

# Replace the previous STATIC_URL = 'static/' with this:
# 🌟 CRITICAL FIX: The base URL must include the repository name.
STATIC_URL = '/BlogMind_Project/staticfiles/'

# NOTE: The destination folder is STATIC_ROOT = BASE_DIR / 'staticfiles'


# ... (omitted for brevity)
ROOT_URLCONF = 'blogmind.urls'
WSGI_APPLICATION = 'blogmind.wsgi.application'

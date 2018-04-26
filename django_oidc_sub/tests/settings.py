"""Settings for tests."""
from __future__ import unicode_literals

SECRET_KEY = 'Black hole sucks!'

INSTALLED_APPS = [
    'django.contrib.contenttypes',
    'django.contrib.auth',
    'django_oidc_sub',
    'mozilla_django_oidc',
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    }
}

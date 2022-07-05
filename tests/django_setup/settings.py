import os
import sys

ROOT_PATH = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, ROOT_PATH + "/tests/django_setup")

SECRET_KEY = 1

INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'graphene_django',
    'tests.django_setup',
]

DATABASES = {
    "default": {"ENGINE": "django.db.backends.sqlite3", "NAME": "test.sqlite"}
}

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
    }
]

GRAPHENE = {"SCHEMA": "tests.django_setup.schema.schema"}
USE_TZ = True
ROOT_URLCONF = "tests.django_setup.urls"

import sys
import os

ROOT_PATH = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, ROOT_PATH + "/tests/django_setup")

SECRET_KEY = 1

INSTALLED_APPS = [
    "graphene_django",
    "tests.django_setup",
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

ROOT_URLCONF = "graphene_django.tests.urls"

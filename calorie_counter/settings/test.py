from .base import *

LOGGING = {}
CELERY_ENABLED = False

SECRET_KEY="django-insecure-+01rjt^m#w9_jxu!s6##q3j6fch*i5_h#_x4rn0q!zni&3qmls"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": "my_database",
        "TEST": {
            "NAME": "mytestdatabase",
        },
    }
}
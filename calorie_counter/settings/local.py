from .base import *

SECRET_KEY="django-insecure-+01rjt^m#w9_jxu!s6##q3j6fch*i5_h#_x4rn0q!zni&3qmls"

DEBUG = True

DATABASES = {
    "default": {
        "ENGINE": os.environ.get("DB_ENGINE", "django.db.backends.sqlite3"),
        "NAME": os.environ.get("DB_NAME", "mydatabase"),
        "USER": os.environ.get("DB_USER", ""),
        "PASSWORD": os.environ.get("DB_PASSWORD", ""),
        "HOST": os.environ.get("DB_HOST", ""),
        "PORT": os.environ.get("DB_PORT", ""),
    }
}

# Celery
CELERY_ENABLED = False

# DJANGO DEBUG TOOLBAR
# INSTALLED_APPS.append("debug_toolbar")
# MIDDLEWARE.insert(0, "debug_toolbar.middleware.DebugToolbarMiddleware")
# INTERNAL_IPS = ["127.0.0.1"]

# HTTPS
# The cookie will be marked as “secure”, 
# which means browsers may ensure that the cookie is only sent under an HTTPS connection.
SESSION_COOKIE_SECURE = False

# All SSL redirects will be directed to this host rather than the originally-requested host 
SECURE_SSL_HOST = ""
SECURE_SSL_REDIRECT = False

# LOGS
LOGGING = {
    "version": 1,
    "disable_existing_loggers": True,
    "loggers": {
        "django": {
            "handlers": ["file_info", "file_warning", "file_error"],
            "level": "INFO",
        },
    },
    "handlers": {
        "console": {
            "level": "INFO",
            "class": "logging.StreamHandler",
            "formatter": "simple_format",
        },
        "file_info": {
            "level": "DEBUG",
            "class": "logging.FileHandler",
            "filename": "./logs/info.log",
            "formatter": "simple_format",
        },
        "file_warning": {
            "level": "WARNING",
            "class": "logging.FileHandler",
            "filename": "./logs/warning.log",
            "formatter": "warning_format",
        },
        "file_error": {
            "level": "ERROR",
            "class": "logging.FileHandler",
            "filename": "./logs/error.log",
            "formatter": "error_format",
        },
    },
    "formatters": {
        "simple_format": {
            "format": "{levelname:8s} {asctime}: {message} - {filename}: {lineno}",
            "style": "{",
            "datefmt": "%d-%m-%Y %H:%M:%S",
        },
        "warning_format": {
            "format": "{levelname:8s} {asctime}: {message} - {filename}: {lineno}",
            "style": "{",
            "datefmt": "%d-%m-%Y %H:%M:%S",
        },
        "error_format": {
            "format": "{levelname:8s}: {asctime} {filename} {message} - {pathname}: {lineno}",
            "style": "{",
            "datefmt": "%d-%m-%Y %H:%M:%S",
        },
    }
}

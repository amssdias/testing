def task_celery(func, *args, **kwargs):
    from django.conf import settings

    if settings.CELERY_ENABLED:
        func.delay(*args, **kwargs)
    else:
        func(*args, **kwargs)
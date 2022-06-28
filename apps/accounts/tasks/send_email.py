from celery import shared_task

from apps.accounts.utils import send_email


@shared_task
def send_email_async(*args, **kwargs):
    """
    Send activation link to user
    """

    try:
        send_email(*args, **kwargs)
    except Exception as e:
        return e
    return True

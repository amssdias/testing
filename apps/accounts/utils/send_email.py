import logging

from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode

from apps.accounts.models.user import User
from apps.accounts.utils import generate_token

logger = logging.getLogger("django")


def send_email(user_id, domain):
    email_subject = "Activate your account"
    email_template_name = "accounts/email/activate_account.html"

    user = User.objects.get(id=user_id)
    logger.info("Generating template with token.")
    message = render_to_string(
        email_template_name,
        {
            "user": user,
            "domain": domain,
            "uid": urlsafe_base64_encode(force_bytes(user.pk)),
            "token": generate_token.make_token(user),
        },
    )

    email = EmailMessage(
        subject=email_subject,
        body=message,
        to=[user.email],
    )

    try:
        logger.info(f"Sent email to user: {user_id}")
        email.send()
    except Exception as e:
        logging.warning(f"Couldn't send email to activate account.")
        raise Exception(e)

    return True

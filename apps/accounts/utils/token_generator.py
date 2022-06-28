from django.contrib.auth.tokens import PasswordResetTokenGenerator


class TokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp):
        """
        Change this hash, so we can check a token for activating email
        """
        return f"{user.pk}{timestamp}{user.is_active}"


generate_token = TokenGenerator()

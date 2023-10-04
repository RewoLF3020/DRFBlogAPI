from templated_mail.mail import BaseEmailMessage
from django.contrib.auth.tokens import default_token_generator
from djoser import utils
from djoser.conf import settings
import os


class ActivationEmail(BaseEmailMessage):
    template_name = "email/activation.html"

    def get_context_data(self):
        # ActivationEmail can be deleted
        context = super().get_context_data()
        # ...

        return context


class PasswordResetEmail(BaseEmailMessage):
    template_name = "email/password_reset.html"

    def get_context_data(self):
        # ActivationEmail can be deleted
        context = super().get_context_data()
        # ...

        return context

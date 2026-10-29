from django.core.mail import send_mail, EmailMessage
from .email_builder import EmailBuilder


class EmailService:

    @staticmethod
    def send(details):
        email_message = EmailMessage(
            subject=details.subject, body=details.text,
            from_email=details.frm, to=details.to
        )

        email_message.content_subtype = 'plain'

        email_message.send()
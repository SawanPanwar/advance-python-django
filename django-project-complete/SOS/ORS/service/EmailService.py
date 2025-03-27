from django.core.mail import send_mail, EmailMessage
from .EmailBuilder import EmailBuilder


class EmailService:

    @staticmethod
    def send(msg, sendingMail, user):
        if (sendingMail == 'changePassword'):
            text = EmailBuilder.change_password(user)
            email = EmailMessage(msg.subject, text, msg.frm, msg.to)
            email.content_subtype = 'html'
            try:
                res = email.send()
            except Exception as e:
                res = e
            return res
        elif (sendingMail == 'signUp'):
            text = EmailBuilder.sign_up(user)
            email = EmailMessage(msg.subject, text, msg.frm, msg.to)
            email.content_subtype = 'html'

            try:
                res = email.send()
            except Exception as e:
                res = e
            return res
        elif (sendingMail == 'forgotPassword'):
            text = EmailBuilder.forgot_password(user)
            email = EmailMessage(msg.subject, text, msg.frm, msg.to)
            email.content_subtype = 'html'

            try:
                res = email.send()
            except Exception as e:
                res = e
            return res
        else:
            return None

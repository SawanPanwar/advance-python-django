
from django.conf import settings

class EmailMessege:

    def __init__(self):
        self.frm = settings.EMAIL_HOST_USER
        self.to = []
        self.cc = []
        self.bcc = []
        self.subject = ""
        self.text = ""
        self.type = "html"
        self.attachment = []

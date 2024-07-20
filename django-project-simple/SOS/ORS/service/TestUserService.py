import os
import sys
import django
import datetime
from UserService import UserService

sys.path.append("D:/Rays/Python Workspace/django-project-simple/SOS")
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'SOS.settings')
django.setup()


def testadd():
    params = {
        'firstName': 'Sneha',
        'lastName': 'Kushwah',
        'loginId': '105Sneha',
        'password': 'abc',
        'dob': datetime.date(2003, 12, 27),
        'address': 'Indore'
    }
    service = UserService()
    service.add(params)


testadd()

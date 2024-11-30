from django.test import TestCase
from .models import User


class TestUserModel(TestCase):

    obj = User(
        firstName="Shyammm",
        lastName="Sharma",
        loginid="shyam@gmail.com",
        password="1234",
        dob="2024-01-01",
        address="indore"
    )

    obj.save()
    print("Data Saved")  # py manage.py test
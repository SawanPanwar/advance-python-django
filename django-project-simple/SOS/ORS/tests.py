from django.test import TestCase
from .models import User


class TestUserModel(TestCase):

    def test_add(self):
        obj = User(
            firstName="Shyammm",
            lastName="Sharma",
            loginId="shyam@gmail.com",
            password="1234",
            dob="2024-01-01",
            address="indore"
        )
        obj.save()
        print("User Added")  # python manage.py test ORS.tests.TestUserModel.test_add

    def test_update(self):
        obj = User.objects.create(
            firstName="Shyammm",
            lastName="Sharma",
            loginId="shyam@gmail.com",
            password="1234",
            dob="2024-01-01",
            address="indore"
        )
        obj.firstName = 'abc'
        obj.save()
        print("User Updated")  # python manage.py test ORS.tests.TestUserModel.test_update

    def test_delete(self):
        obj = User.objects.create(
            firstName="Shyammm",
            lastName="Sharma",
            loginId="shyam@gmail.com",
            password="1234",
            dob="2024-01-01",
            address="indore"
        )
        obj_id = obj.id
        obj.delete()
        # Check that the user no longer exists
        user_exists = User.objects.filter(id=obj_id).exists()
        assert not user_exists, "User was not deleted"
        print("User Deleted")

    def test_read(self):
        obj = User.objects.create(
            firstName="Shyammm",
            lastName="Sharma",
            loginId="shyam@gmail.com",
            password="1234",
            dob="2024-01-01",
            address="indore"
        )
        all_users = User.objects.all()
        assert len(all_users) > 0, "No users found"
        print(f"Users Read: {len(all_users)} found")

    def test_get(self):
        obj = User.objects.create(
            firstName="Shyammm",
            lastName="Sharma",
            loginId="shyam@gmail.com",
            password="1234",
            dob="2024-01-01",
            address="indore"
        )
        user = User.objects.get(id=obj.id)
        assert user.firstName == "Shyammm", "Get returned wrong user"
        print("User Get by ID successful")

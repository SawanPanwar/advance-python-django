import os
import sys
import django

BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.dirname(
            os.path.abspath(__file__)
        )
    )
)

sys.path.insert(0, BASE_DIR)

os.environ.setdefault(
    'DJANGO_SETTINGS_MODULE',
    'sos.settings'
)

django.setup()

from ors.models import User
from ors.service.user_service import UserService

import datetime


def test_save():
    user = User()

    user.id = 0
    user.first_name = 'Harshad'
    user.last_name = 'Kushwah'
    user.login_id = 'harsh@gmail.com'
    user.password = '123'
    user.dob = datetime.date(2003, 12, 27)
    user.address = 'Indore'

    service = UserService()
    service.save(user)

    print("User Saved")
    print("ID =", user.id)


def test_update():
    service = UserService()

    user = User()

    user.id = 21
    user.first_name = 'Harshad'
    user.last_name = 'Niboriya'
    user.login_id = 'abc@gmail.com'
    user.password = '123'
    user.dob = datetime.date(2003, 12, 27)
    user.address = 'Indore'

    service.save(user)

    print("User Updated")


def test_delete():
    service = UserService()

    service.delete(21)

    print("User Deleted")


def test_get():
    service = UserService()

    user = service.get(21)

    if user is not None:

        print("ID =", user.id)
        print("First Name =", user.first_name)
        print("Last Name =", user.last_name)
        print("Login ID =", user.login_id)
        print("Password =", user.password)
        print("DOB =", user.dob)
        print("Address =", user.address)

    else:
        print("User Not Found")


def test_find_by_login():
    service = UserService()

    users = service.find_by_login('abc@gmail.com')

    for user in users:
        print("ID =", user.id)
        print("First Name =", user.first_name)
        print("Last Name =", user.last_name)
        print("Login ID =", user.login_id)
        print("Password =", user.password)
        print("DOB =", user.dob)
        print("Address =", user.address)


def test_authenticate():
    service = UserService()

    user = service.authenticate('abc@gmail.com', '1234')

    if user is not None:

        print("ID =", user.id)
        print("First Name =", user.first_name)
        print("Last Name =", user.last_name)
        print("Login ID =", user.login_id)
        print("Password =", user.password)
        print("DOB =", user.dob)
        print("Address =", user.address)

    else:

        print("Invalid Login ID or Password")


def test_search():
    params = {}

    # params['first_name'] = 'S'
    params['page_no'] = 2
    params['page_size'] = 5

    service = UserService()

    result = service.search(params)

    for user in result:
        print(
            user.id,
            user.first_name,
            user.last_name,
            user.login_id,
            user.dob,
            user.address
        )

    print("Has Next =", params.get('has_next'))
    print("Has Previous =", params.get('has_previous'))
    print("Index =", params.get('index'))


# test_save()
# test_update()
# test_delete()
# test_get()
# test_find_by_login()
# test_authenticate()
test_search()

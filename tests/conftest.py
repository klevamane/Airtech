import pytest
from user.models import User
from .mock_data.users import valid_user_one
from django.contrib.auth.hashers import pbkdf2, make_password

# @pytest.fixture(scope='function')
# def saved_valid_user_one(transactional_db):
#
#     user = User(**valid_user_one)
#     user.save()
#     return user


@pytest.fixture(scope='module')
def new_user1():
    hased_password = make_password('password123')
    params = {
        'firstname': 'test',
        'lastname': 'user1',
        'email': 'testuser@test.com',
        'date_of_birth': '1995-01-01',
        # 'password': 'pbkdf2_sha256$150000$ah3ccoAH5eS5$fv/61uyxCYq6Pv5GGVB6gQs0s7NBw8tcbzHSLZoFr78=',
        'password': hased_password,
        'is_active': True,
        'is_admin': False,
    }
    user = User(**params)
    return user


@pytest.fixture(scope='module')
def new_user2():
    hased_password = make_password('password123')
    params = {
        'firstname': 'test',
        'lastname': 'user2',
        'email': 'testuser2@test.com',
        'date_of_birth': '1995-01-01',
        # 'password': 'pbkdf2_sha256$150000$ah3ccoAH5eS5$fv/61uyxCYq6Pv5GGVB6gQs0s7NBw8tcbzHSLZoFr78=',
        'password': hased_password,
        'image': 'https://res.cloudinary.com/health-id/image/upload/v1554552278/Profile_Picture_Placeholder.png',
        'is_active': True,
        'is_admin': False,
    }
    user = User(**params)
    return user


@pytest.fixture(scope='module')
def admin_user():
    hased_password = make_password('password123')
    params = {
        'firstname': 'admin',
        'lastname': 'user',
        'email': 'admin@test.com',
        'date_of_birth': '1995-01-01',
        # 'password': 'pbkdf2_sha256$150000$ah3ccoAH5eS5$fv/61uyxCYq6Pv5GGVB6gQs0s7NBw8tcbzHSLZoFr78=',
        'password': hased_password,
        'is_active': True,
        'is_admin': True,
    }
    user = User(**params)
    return user

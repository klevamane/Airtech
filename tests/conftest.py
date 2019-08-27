import pytest
from user.models import User
from flights.models import Flight, Airport
from tickets.models import Tickets
from django.contrib.auth.hashers import pbkdf2, make_password
import datetime

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


@pytest.fixture(scope='module')
def airport1():
    params = {
    'name': 'airportone',
    'code': 'APO',
    'city': 'portharcourt',
    'country': 'Nigeria',
    }
    airport = Airport(**params)
    return airport


@pytest.fixture(scope='module')
def airport2():
    params = {
    'name': 'airportwo',
    'code': 'LOS',
    'city': 'lag',
    'country': 'Nigeria',
    }
    airport = Airport(**params)
    return airport


@pytest.fixture(scope='module')
def flightone():
    params = {
    'name': 'flightone',
    'code':'FLIONE',
    'source' : None,
    'destination' : None,
    'takeoff_time' : datetime.datetime.now(),
    'arrival_time' : datetime.datetime.now() + datetime.timedelta(hours=1),
    'gate': 1,
    'is_active': True,
    'seats': 70,
    'status': 'active',

    }
    flight = Flight(**params)
    return flight


@pytest.fixture(scope='module')
def ticket():
    params = {
        'flight_id': None,
        'customer': None,
        'payment_status': 'reserved'
    }
    ticket = Tickets(**params)
    return ticket


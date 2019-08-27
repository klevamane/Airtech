import pytest
from rest_framework.test import APIClient
from django.urls import resolve, reverse

from flights.models import Airport
import datetime
from helpers.constants import CHARSET
# Create your tests here.


USER_URL = '/v1/api/users/{}/'


@pytest.mark.django_db
class TestFlight:

    def test_flight_detail(self, admin_user, airport1, airport2, flightone):
        admin_user.save ()
        airport1.save()
        airport2.save()
        flightone.source = airport1
        flightone.destination = airport2
        flightone.save()

        login_data = {
            "email": "admin@test.com",
            "password": "password123"
        }
        client = APIClient ()

        path = reverse ('token_obtain_pair')
        resp = client.post(path, login_data)
        token = resp.data

        client.credentials(HTTP_AUTHORIZATION='Bearer ' + token['access'])
        response = client.get('/v1/api/flights/detail/{}/'.format(flightone.id))
        assert response.status_code == 200
        response_list = client.get ('/v1/api/flights/all/')
        assert response_list.status_code ==200

    def test_get_airport_list(self, admin_user, airport1, airport2):
        admin_user.save ()
        airport1.save()
        airport2.save()

        login_data = {
            "email": "admin@test.com",
            "password": "password123"
        }
        client = APIClient ()

        path = reverse ('token_obtain_pair')
        path2 = reverse('add_airport')
        resp = client.post(path, login_data)
        token = resp.data

        client.credentials(HTTP_AUTHORIZATION='Bearer ' + token['access'])
        response = client.get(path2)
        assert response.status_code == 200
        # assert

    def test_add_airport_fails(self, admin_user, airport1, airport2):
        admin_user.save ()


        login_data = {
            "email": "admin@test.com",
            "password": "password123"
        }

        params = {
            'name': 'testair',
            'code': '233',
            'city': 'lag',
            'country': 'Nigeria',
        }
        client = APIClient ()

        path = reverse ('token_obtain_pair')
        path2 = reverse('add_airport')
        resp = client.post(path, login_data)
        token = resp.data

        client.credentials(HTTP_AUTHORIZATION='Bearer ' + token['access'])
        response = client.post(path2, params)

        assert response.data['code'][0] == 'airport code should contain only letters'
        assert response.status_code == 400
        params['code'] = 'LO'
        response2 = client.post (path2, params)
        assert response2.data['code'][0] == 'The airport code must be of 3 characters'

    def test_adding_flight(self, admin_user, airport1, airport2, flightone):
        admin_user.save ()
        airport1.save()
        airport2.save()
        flightone.source = airport1
        flightone.destination = airport2
        new_flight = flightone
        new_flight.seats = 'ad'
        new_flight.status = 'wrong'

        login_data = {
            "email": "admin@test.com",
            "password": "password123"
        }
        params = {
            'name': 'flightest',
            'code': 'FLITES',
            'source': airport1.id,
            'destination': airport2.id,
            'takeoff_time': datetime.datetime.now (),
            'arrival_time': datetime.datetime.now () + datetime.timedelta (hours=1),
            'gate': 1,
            'is_active': True,
            'seats': 25,
            'status': 'active',

        }
        client = APIClient ()

        path = reverse ('token_obtain_pair')
        path2 = reverse('add_flight')

        resp = client.post(path, login_data)
        token = resp.data

        client.credentials(HTTP_AUTHORIZATION='Bearer ' + token['access'])
        response = client.post(path2, params)
        assert response.data['seats'][0] == 'Total flight seats must not be less than 50'
        assert response.status_code == 400
        params['seats'] = 300
        params['status'] = 'invalid'
        response2 = client.post (path2, params)
        assert response2.data['seats'][0] == 'Total flight seats must not be more than 200'
        assert response2.data['status'][0] == 'Wrong status'

        params['source'] = airport1.id
        params['seats'] = 150
        params['destination'] = airport1.id
        params['status'] = 'active'
        response3 = client.post (path2, params)
        assert response3.data['non_field_errors'][0] == 'The source and destination cannot be the same'
        time =  datetime.datetime.now ()
        params['source'] = airport1.id
        params['takeoff_time'] = time
        params['arrival_time'] = time
        params['destination'] = airport2.id
        response4 = client.post (path2, params)

        assert response4.data['non_field_errors'][0] == 'Departure and arrival time cannot be the same'
        params['takeoff_time'] = time + datetime.timedelta(days=1)
        params['arrival_time'] = time
        response5 = client.post (path2, params)
        assert response5.data['non_field_errors'][0] == 'Departure time cannot be greater than arrival time'

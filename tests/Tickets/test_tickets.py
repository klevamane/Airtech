import pytest
from rest_framework.test import APIClient
from django.urls import resolve, reverse

from tickets.models import Tickets
import datetime
# Create your tests here.


USER_URL = '/v1/api/users/{}/'


@pytest.mark.django_db
class TestFlight:

    def test_book_ticket(self, new_user1, airport1, airport2, flightone):
        new_user1.save ()
        airport1.save()
        airport2.save()
        flightone.source = airport1
        flightone.destination = airport2
        flightone.seats = 1
        flightone.save()

        login_data = {
            "email": "testuser@test.com",
            "password": "password123"
        }
        client = APIClient ()
        path = reverse ('token_obtain_pair')
        resp = client.post(path, login_data)
        token = resp.data
        client.credentials(HTTP_AUTHORIZATION='Bearer ' + token['access'])
        response = client.post('/v1/api/tickets/reservation/{}'.format(flightone.id))
        assert response.status_code == 201
        response2 = client.post ('/v1/api/tickets/reservation/{}'.format (flightone.id))
        assert response2.status_code == 400
        response3 = client.post ('/v1/api/tickets/reservation/{}'.format (500))
        assert response3.status_code == 400

@pytest.mark.django_db
class TestGetReservations:

    def test_get_reservation(self, new_user1, airport1, airport2, flightone, ticket):
        new_user1.save()
        airport1.save()
        airport2.save()
        flightone.source = airport1
        flightone.destination = airport2
        flightone.seats = 70
        flightone.save()
        ticket.customer = new_user1
        ticket.flight_id = flightone
        ticket.save()

        login_data = {
            "email": new_user1.email,
            "password": "password123"
        }
        client = APIClient ()
        path = reverse('token_obtain_pair')

        resp = client.post (path, login_data)
        token = resp.data
        client.credentials (HTTP_AUTHORIZATION='Bearer ' + token['access'])
        response = client.get('/v1/api/tickets/reservation/{}/all/'.format(new_user1.id))
        assert response.status_code == 200
        assert "id" in response.data[0]
        response2 = client.get ('/v1/api/tickets/reservation/{}/all/?date={}'.format (new_user1.id, "01-01-2019"))
        assert response2.data['message'] == 'Incorrect data format, should be YYYY-MM-DD'
        assert response2.status_code == 400

    def test_get_reservations_by_date_success(self, new_user1, airport1, airport2, flightone, ticket):
        new_user1.save()
        airport1.save()
        airport2.save()
        flightone.source = airport1
        flightone.destination = airport2
        flightone.seats = 70
        flightone.save()
        ticket.customer = new_user1
        ticket.flight_id = flightone
        ticket.save()

        login_data = {
            "email": new_user1.email,
            "password": "password123"
        }
        client = APIClient ()
        path = reverse('token_obtain_pair')

        resp = client.post (path, login_data)
        token = resp.data
        client.credentials (HTTP_AUTHORIZATION='Bearer ' + token['access'])
        response2 = client.get ('/v1/api/tickets/reservation/{}/all/?date={}'.format (new_user1.id, ticket.created_at))
        assert len(response2.data) > 0
        assert response2.status_code == 200


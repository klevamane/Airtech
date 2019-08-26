import pytest
from rest_framework.test import APIClient
from django.urls import resolve, reverse
import json
from helpers.constants import CHARSET
# Create your tests here.



USER_URL = '/v1/api/users/{}/'


class TestCaseSetup:
    def test_one_is_equal_to_one(self):
        assert 1 == 1

@pytest.mark.django_db
class TestUser:

    def test_user_signup_success(self):
        signup_data = {
            'firstname': 'maples',
            'lastname': 'lehft',
            'email': 'mapples@test.com',
            'password': 'password123',
            'date_of_birth': '1992-01-01',

        }
        path = reverse('list_user')
        client = APIClient()
        response = client.post(path, signup_data)
        assert response.status_code == 201

    def test_password_must_contain_digit_fails(self):
        signup_data = {
            'firstname': 'maples',
            'lastname': 'lehft',
            'email': 'mapples@test.com',
            'password': 'password',
            'date_of_birth': '1992-01-01',

        }
        path = reverse('list_user')
        client = APIClient()
        response = client.post(path, signup_data)

        # print("response ", dir(response.data))
        assert response.data['password'][0] == "The password must contain at least 1 digit, 0-9."
        assert response.status_code == 400

    def test_password_must_contain_be_min_6(self):
        signup_data = {
            'firstname': 'maples',
            'lastname': 'lehft',
            'email': 'mapples@test.com',
            'password': 'pass1',
            'date_of_birth': '1992-01-01',

        }
        path = reverse('list_user')
        client = APIClient()
        response = client.post(path, signup_data)

        # print("response ", dir(response.data))
        assert response.data['password'][0] == "The password must must be of at least 6 characters"
        assert response.status_code == 400

    def signup_invalid_data_fails(self):
        signup_data = {

        }
        path = reverse('list_user')
        client = APIClient()
        response = client.post(path, signup_data)
        print('**** response data ', response.data)
        # print("response ", dir(response.data))
        assert response.data['password'][0] == "This field is required."
        assert response.data['email'][0] == "This field is required."
        assert response.data['lastname'][0] == "This field is required."
        assert response.data['firstname'][0] == "This field is required."
        assert response.status_code == 400

    def test_get_list_of_users_success(self, new_user1, new_user2, admin_user):
        new_user1.save()
        new_user2.save()
        admin_user.save()
        login_data = {
            "email": "admin@test.com",
            "password": "password123"
        }
        client = APIClient()
        list_path = reverse ('list_user')
        path = reverse('token_obtain_pair')
        resp = client.post(path, login_data)
        token = resp.data

        client.credentials(HTTP_AUTHORIZATION='Bearer ' + token['access'])
        response = client.get(list_path)
        assert len(response.data) > 1
        assert response.status_code == 200

    def test_get_list_of_users_fails(self, new_user1, new_user2, admin_user):
        new_user2.save ()
        admin_user.save ()
        login_data = {
            "email": "testuser2@test.com",
            "password": "password123"
        }
        client = APIClient()
        list_path = reverse ('list_user')
        path = reverse ('token_obtain_pair')
        resp = client.post (path, login_data)
        token = resp.data
        client.credentials (HTTP_AUTHORIZATION='Bearer ' + token['access'])
        response = client.get(list_path)

        assert response.status_code == 403


@pytest.mark.django_db
class TestUserDetail:

    def test_retrieve_user_details_succeeds(self, new_user1):
        new_user1.save()
        login_data = {
            "email": "testuser@test.com",
            "password": "password123"
        }
        client = APIClient ()

        path = reverse ('token_obtain_pair')
        resp = client.post (path, login_data)
        token = resp.data
        client.credentials(HTTP_AUTHORIZATION='Bearer ' + token['access'])
        response = client.get(USER_URL.format(new_user1.id))
        assert response.data['data']['id'] == new_user1.id
        assert len(response.data) > 0
        assert response.status_code == 200

        update_data = {
            "firstname": "Trinity"
        }
        resp = client.patch('/v1/api/users/update/{}/'.format(new_user1.id), update_data)
        assert resp.status_code == 200

    def test_delete_user_passport(self, new_user2):
        new_user2.save ()
        login_data = {
            "email": "testuser2@test.com",
            "password": "password123"
        }
        client = APIClient()

        path = reverse('token_obtain_pair')
        resp = client.post(path, login_data)
        token = resp.data
        client.credentials (HTTP_AUTHORIZATION='Bearer ' + token['access'])
        response = client.delete('/v1/api/users/delete/{}/'.format(new_user2.id))
        assert response.status_code == 200

    def test_delete_another_user_passport_fails(self, new_user1, new_user2):
        new_user1.save()
        new_user2.save()
        login_data = {
            "email": "testuser2@test.com",
            "password": "password123"
        }
        client = APIClient()

        path = reverse('token_obtain_pair')
        resp = client.post(path, login_data)
        token = resp.data
        client.credentials (HTTP_AUTHORIZATION='Bearer ' + token['access'])
        response = client.delete('/v1/api/users/delete/{}/'.format(new_user1.id))
        resp = client.delete ('/v1/api/users/delete/{}/'.format (500))
        assert response.status_code == 403


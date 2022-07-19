import pytest
from accounts.models import Account
from django.contrib.auth.models import Group
from rest_framework.test import APIClient

BASE_API_ENDPOINT = "http://localhost:8000/"


@pytest.fixture
@pytest.mark.django_db
def new_client_api():
    api_client = APIClient()
    payload = {
        "email": "test@test.com",
        "mobile": "9129999999",
        "name": "test_name",
        "password": "test_pass",
    }
    return api_client.post(BASE_API_ENDPOINT + "api/clients/", payload)


@pytest.mark.django_db
def test_create_client_user(new_client_api):
    resp = new_client_api
    new_client_users = Account.objects.all()

    assert resp.status_code == 201
    assert new_client_users.count() == 1
    assert new_client_users[0].is_active == False
    assert new_client_users[0].role == Account.Role.CLIENT
    assert new_client_users[0].groups.first() == Group.objects.get(name="client")


@pytest.mark.django_db
def test_update_client_user(new_client_api):
    resp = new_client_api

    api_client = APIClient()
    payload = {
        "email": "test@test.com",
        "mobile": "91288888888",
        "name": "test_name2",
    }
    resp = api_client.put(BASE_API_ENDPOINT + "api/clients/1/", payload)

    assert resp.status_code == 200
    assert resp.data["name"] != "test_name"

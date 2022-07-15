from hashlib import new

import pytest
from accounts.models import Account
from rest_framework.test import APIClient

BASE_API_ENDPOINT = "http://localhost:8000/"


@pytest.mark.django_db
def test_create_client_api():
    api_client = APIClient()
    payload = {
        "email": "test@test.com",
        "mobile": "9120877283",
        "name": "test_name",
        "password": "test_pass",
    }
    resp = api_client.post(BASE_API_ENDPOINT + "api/clients/", payload)
    new_client_users = Account.objects.all()

    assert resp.status_code == 201
    assert new_client_users.count() == 1
    assert new_client_users[0].is_active == False
    assert new_client_users[0].role == Account.Role.CLIENT

import pytest
from model_bakery import baker

from .models import Account


@pytest.mark.django_db
def test_create_client():
    new_client_user = baker.make("accounts.Account")
    assert new_client_user.role == Account.Role.CLIENT
    assert new_client_user.is_active == False

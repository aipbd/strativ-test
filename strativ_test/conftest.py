import pytest
from django.contrib.auth.models import User
from factory import Faker
from factory.django import DjangoModelFactory
from rest_framework.test import APIClient


class UserFactory(DjangoModelFactory):
    username = Faker("first_name")

    class Meta:
        model = User


@pytest.fixture(autouse=True)
def enable_db_access(db):
    pass


@pytest.fixture
def client():
    return APIClient()


@pytest.fixture
def user():
    return UserFactory()


@pytest.fixture
def auth_client(user, client):
    client.force_authenticate(user)
    return client

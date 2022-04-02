import pytest

from rest_framework.test import APIClient
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


@pytest.fixture
def user_achille(django_user_model):
    achille = django_user_model.objects.create_user(
        email="adetroie@gmail.com",
        password="password123",
    )
    achille.save()

    return achille

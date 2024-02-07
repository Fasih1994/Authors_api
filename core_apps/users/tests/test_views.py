import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from core_apps.users.models import User
from core_apps.users.views import CustomUserDetailsView


@pytest.mark.django_db
def test_authetication_requirements(normal_user):
    client = APIClient()
    url = reverse("user_details")

    response = client.get(url)
    assert response.status_code == status.HTTP_401_UNAUTHORIZED

    client.force_authenticate(user=normal_user)
    response = client.get(url)
    assert response.status_code == status.HTTP_200_OK


@pytest.mark.django_db
def test_get_user_details(normal_user):
    client = APIClient()
    client.force_authenticate(user=normal_user)
    url = reverse("user_details")

    response = client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert response.data["email"] == normal_user.email
    assert response.data["first_name"] == normal_user.first_name
    assert response.data["last_name"] == normal_user.last_name


@pytest.mark.django_db
def test_update_details(normal_user):
    client = APIClient()
    client.force_authenticate(user=normal_user)
    url = reverse("user_details")

    update_data = {"first_name": "updated first name", "last_name": "updated last name"}

    response = client.patch(url, data=update_data)
    assert response.status_code == status.HTTP_200_OK
    assert response.data["first_name"] == update_data["first_name"]
    assert response.data["last_name"] == update_data["last_name"]

    updated_user = User.objects.get(pk=normal_user.pk)
    assert updated_user.first_name == update_data["first_name"]
    assert updated_user.last_name == update_data["last_name"]


def test_get_queryset_empty(normal_user):
    client = APIClient()
    client.force_authenticate()
    url = reverse("user_details")
    response = client.get(url)

    view = CustomUserDetailsView()
    view.request = response.wsgi_request

    queryset = view.get_queryset()

    assert queryset.count() == 0

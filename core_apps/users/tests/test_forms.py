import pytest
from core_apps.users.forms import UserCreationForm
from core_apps.users.tests.factories import UserFactory

@pytest.mark.django_db
def test_user_creation_form_valid_data():
    data = {
        'first_name': 'Jhon',
        'last_name': 'Doe',
        'email': 'jhon@doe.com',
        'password1': 'secur_it_123',
        'password2': 'secur_it_123'
    }

    form  = UserCreationForm(data)
    assert form.is_valid()

@pytest.mark.django_db
def test_user_creation_form_invalid_data():
    user = UserFactory()
    data = {
        'first_name': 'Jhon',
        'last_name': 'Doe',
        'email': user.email, # this email is alrady in use now
        'password1': 'secur_it_123',
        'password2': 'secur_it_123'
    }

    form  = UserCreationForm(data)
    assert not form.is_valid()
    assert 'email' in form.errors
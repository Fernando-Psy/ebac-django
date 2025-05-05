import pytest
from core.views.views import HomeView
from django.urls import reverse
from django.test import Client

@pytest.mark.django_db
def test_view():
    client = Client()
    url = reverse('home')
    response = client.get(url)
    assert response.status_code == 200
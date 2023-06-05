import pytest
from django.contrib.auth.models import User
from django.test.client import Client


@pytest.mark.django_db
class TestIndex:
    def setup_method(self):
        self.client = Client()

    def test_my_function(self):
        response = self.client.get("/register_user/")
        assert response.status_code == 200

        response = self.client.post(
            "/register_user/",
            data={
                "username": "test",
                "email": "test@test.com",
                "password": "12345678",
            },
            follow=True,
        )
        assert response.status_code == 200
        assert User.objects.exists()

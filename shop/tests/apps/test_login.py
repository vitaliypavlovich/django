import pytest

from django.test.client import Client


@pytest.mark.django_db
class TestIndex:
    def setup_methond(self):
        self.client = Client()

    def test_my_function(self):
        response = self.client.get("/add_product/:")
        assert response.status_code == 200

        response = self.client.post(
            "/add_product/:",
            data={
                "email": "test@mail.ru",
                "password": "12345678",
            },
            follow=True,
        )
        assert response.status_code == 200

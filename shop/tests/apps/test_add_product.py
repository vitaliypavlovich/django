import pytest

from django.test.client import Client

from products.models import Product


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
                "title": "test",
                "price": "1",
                "description": "test",
            },
            follow=True,
        )
        assert response.status_code == 200
        assert Product.objects.exists()

import pytest

from rest_framework.test import APIClient

from products.models import Product


@pytest.mark.django_db
class TestProductAddApi:
    def setup_method(self):
        self.client = APIClient()

    def test_my_function(self):
        response = self.client.get("/api/products/")
        assert response.status_code == 200

        response = self.client.post(
            "/api/products/",
            data={
                "title": "test",
                "color": "RED",
                "price": "12",
                "description": "12345678",
            },
            follow=True,
        )
        assert response.status_code == 201
        assert Product.objects.exists()

    def test_delete_product(self):
        product = Product.objects.create(
            title="test", color="RED", price="12", description="12345678"
        )

        response = self.client.get(f"/api/products/{product.id}/")
        assert response.status_code == 200
        assert response.json()["title"] == "test"

        # response = self.client.delete(f"/api/products/{product.id}/")
        # assert response.status_code == 204
        # assert not Product.objects.exists()

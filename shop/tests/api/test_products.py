# import pytest
# from rest_framework.test import APIClient
#
# from tests.factories import ProductFactory
#
#
# @pytest.mark.django_db
# class TestProductsApi:
#     def setup_method(self):
#         self.client = APIClient()
#
#     def test_index(self):
#         response = self.client.get("/api/products/")
#         assert response.status_code == 200
#         assert len(response.json()) == 0
#
#     def test_popular(self):
#         ProductFactory.create_batch(10)
#         response = self.client.get("/api/products/popular/")
#         assert response.status_code == 200
#         assert response.json().get("count") == 10

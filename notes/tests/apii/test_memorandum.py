import pytest
from rest_framework.test import APIClient


@pytest.mark.django_db
class TestMemorandumApi:
    def setup_method(self):
        self.client = APIClient()

    def test_index(self):
        response = self.client.get("/apii/memorandum/")
        assert response.status_code == 200
        assert len(response.json()) == 0
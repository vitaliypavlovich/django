import pytest

from rest_framework.test import APIClient

from memorandum.models import Note


@pytest.mark.django_db
class TestMemorandumAddApi:
    def setup_method(self):
        self.client = APIClient()

    def test_my_function(self):
        response = self.client.get("/apii/memorandum/")
        assert response.status_code == 200

        response = self.client.post("/apii/memorandum/", data={
            "title": "test",
            "text": "test",
        }, follow=True)
        assert response.status_code == 201
        assert Note.objects.exists()

    def test_delete_product(self):
        product = Note.objects.create(title='test', text='RED')

        response = self.client.get(f"/apii/memorandum/{note.id}/")
        assert response.status_code == 200
        assert response.json()['title'] == 'test'


        response = self.client.delete(f"/apii/memorandum/{note.id}/")
        assert response.status_code == 204
        assert not Note.objects.exists()
# import pytest
#
# from django.test.client import Client
#
# from profiles.models import Profile
#
#
# @pytest.mark.django_db
# class TestIndex:
#     def setup_methond(self):
#         self.client = Client()
#
#     def test_my_function(self):
#         response = self.client.get("/register_profile/:")
#         assert response.status_code == 200
#
#         response = self.client.post(
#             "/register_profile/:",
#             data={
#                 "first_name": "test",
#                 "last_name": "test",
#                 "age": "20",
#             },
#             follow=True,
#         )
#         assert response.status_code == 200
#         assert Profile.objects.exists()

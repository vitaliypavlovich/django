from django.urls import include, path
from rest_framework import routers
from apii.memorandum.views import NoteViewSet

app_name = "apii"

router = routers.DefaultRouter()
router.register(r"memorandum", NoteViewSet)


urlpatterns = [
    path("", include(router.urls)),
]
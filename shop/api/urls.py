from django.urls import include, path
from rest_framework import routers
from api.products.views import (
    ProductViewSet,
    TheMostExpensiveProductViewSet,
    TheMostPopularProductViewSet,
)
from api.users.login_views import LoginView
from api.users.views import RegisterView

app_name = "api"

router = routers.DefaultRouter()
router.register(r"products", ProductViewSet)


urlpatterns = [
    path(
        "products/expensive/",
        TheMostExpensiveProductViewSet.as_view(),
        name="products_expensive",
    ),
    path(
        "products/popular/",
        TheMostPopularProductViewSet.as_view(),
        name="products_popular",
    ),
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", LoginView.as_view(), name="login"),
    path("", include(router.urls)),
]

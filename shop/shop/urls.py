"""shop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from django.conf import settings

from products.views import index, add_product
from profiles.views import profiles, register_user, register_profile, login_view, logout_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('profiles/', profiles, name="profiles"),
    path('register_user/', register_user, name="register_user"),
    path('register_profile/', register_profile, name='register_profile'),
    path('add_product/', add_product, name='add_product'),
    path('', index, name="index"),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
]


if settings.DEBUG:
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    # Serve static and media files from development server
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


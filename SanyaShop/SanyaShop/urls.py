from django.urls import path, include
from rest_framework import routers
from users.views import login, logout
from shop_items.views import like
from shop_items.api import ShoppingItemView
from shop_items.models import ShoppingItem
from users.api import UserView

from django.contrib import admin
from django.urls import path
router = routers.DefaultRouter()


urlpatterns = [
    path("", include(router.urls)),
    path('admin/', admin.site.urls),
    path(
        "api-auth/",
        include("rest_framework.urls", namespace="rest_framework"),
    ),
    path("shopping/<str:_identificator>", ShoppingItemView.as_view()),
    path("shopping/", ShoppingItemView.as_view()),
    path("user/", UserView.as_view()),
    path("login/", login),
    path("like/", like),
    path("logout/", logout),
]

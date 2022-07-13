from django.urls import include, path
from rest_framework import routers

from . import api_views

router = routers.DefaultRouter()
router.register("accounts", api_views.ClientViewSet)

urlpatterns = [
    path("", include(router.urls)),
]

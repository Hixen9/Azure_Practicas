from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ImagenesViewSet

router = DefaultRouter()
router.register(r"productos",ImagenesViewSet,basename="productos")

urlpatterns = [
    path("api/",include(router.urls))
]
from django.urls import path, include
from .views import HellopAPI

urlpatterns = [
    path("hello/", HellopAPI)
]
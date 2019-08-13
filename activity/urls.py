from .views import *
from django.urls import re_path,include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'activities',ActivityViewSet)

urlpatterns = [
    re_path(r'^',include(router.urls))
]

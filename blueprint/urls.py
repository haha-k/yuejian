from .views import *
from django.conf.urls import re_path,include
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'picture',PictureViewSet)

urlpatterns = [
    re_path(r'^',include(router.urls))
    # re_path(r'^api-auth/',include('rest_framework.urls',namespace='rest_framework'))
]

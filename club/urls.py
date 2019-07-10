from .views import *
from django.urls import re_path,include
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'club',ClubViewSet)
router.register(r'attention',AttentionViewSet)
router.register(r'course',CourseViewSet)
router.register(r'coach',CoachViewSet)
router.register(r'train',TrainViewSet)
router.register(r'video',VideoViewSet)

urlpatterns = [
    re_path(r'^',include(router.urls))
    # re_path(r'^api-auth/',include('rest_framework.urls',namespace='rest_framework'))
]

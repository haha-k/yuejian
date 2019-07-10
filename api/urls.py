from django.urls import path,re_path,include
from club.views import *
from blueprint.views import *
from activity.views import *
from contest.views import *
# from *.views import *
from django.urls import re_path,include
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'clubs',ClubViewSet)
router.register(r'pictures',PictureViewSet)
router.register(r'attentions',AttentionViewSet)
router.register(r'courses',CourseViewSet)
router.register(r'coachs',CoachViewSet)
router.register(r'trains',TrainViewSet)
router.register(r'videos',VideoViewSet)
router.register(r'activities',ActivityViewSet)
router.register(r'contests',ContestViewSet)

all_api = [

    re_path(r'',include(router.urls))
]

api_v1 = [re_path(r'',include(all_api))]

api_versions = [re_path(r'v1/',include(api_v1))]

urlpatterns = [re_path(r'api/',include(api_versions))]
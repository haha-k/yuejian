from django.urls import path,re_path,include
from club.views import *
from blueprint.views import *
from activity.views import *
from contest.views import *
from account.views import *
from django.urls import re_path,include
from rest_framework.routers import DefaultRouter
# from rest_framework_jwt.views import obtain_jwt_token, verify_jwt_token
from .views import obtain_jwt_token
# from club.view import *

router = DefaultRouter()
router.register(r'clubs',ClubViewSet)
router.register(r'pictures',PictureViewSet)
router.register(r'attentions',AttentionViewSet)
router.register(r'courses',CourseViewSet)
router.register(r'coaches',CoachViewSet)
router.register(r'trains',TrainViewSet)
router.register(r'videos',VideoViewSet)
router.register(r'activities',ActivityViewSet)
router.register(r'application',ApplicationViewSet)
router.register(r'contests',ContestViewSet)
router.register(r'accounts',AccountViewSet)
router.register(r'users',UserViewSet)
router.register(r'participate',ApplyViewSet)
router.register(r'blueprints',BlueprintViewSet)
# router.register(r'participate',ViewSet)

# domains_router = routers.NestedSimpleRouter(router, r'attend', lookup='activities')
# domains_router.register(r'nameservers', NameserverViewSet)


all_api = [

    re_path(r'',include(router.urls)),
    # re_path(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
    re_path(r'^login/', obtain_jwt_token),
    # re_path(r'^login/', LoginView.as_view()),
]

api_v1 = [re_path(r'',include(all_api))]

api_versions = [re_path(r'v1/',include(api_v1))]

urlpatterns = [re_path(r'api/',include(api_versions))]
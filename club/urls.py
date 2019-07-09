from .views import *
from django.urls import re_path,include
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'club',ClubViewSet)


# club_list = ClubViewSet.as_view(
#     {
#         'get':'list'
#     }
# )

# club_detail = ClubViewSet.as_view({
#         'get':'retrieve'
# })

urlpatterns = [
    re_path(r'^',include(router.urls))
    # re_path(r'^api-auth/',include('rest_framework.urls',namespace='rest_framework'))
]

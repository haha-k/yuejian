from django.urls import path,re_path,include



all_api = [
    re_path(r'^$',)
]

api_v1 = [re_path(r'^$',include(all_api))]

api_versions = [re_path(r'^v1/',include(api_v1))]

urlpatterns = [re_path(r'^api/',include(api_versions))]
from django.urls import path,re_path
from account.views import RegisterUserView
from rest_framework_jwt.views import obtain_jwt_token

app_name='account'
urlpatterns =[
    path(r'users/',RegisterUserView.as_view()),
]
<<<<<<< HEAD
from django.urls import path,re_path
from account.views import RegisterUserView
from rest_framework_jwt.views import obtain_jwt_token

app_name='account'
urlpatterns =[
    path(r'users/',RegisterUserView.as_view()),
=======
from django.urls import path,re_path
from account.views import RegisterUserView
from rest_framework_jwt.views import obtain_jwt_token

app_name='account'
urlpatterns =[
    path(r'users/',RegisterUserView.as_view()),
>>>>>>> 7c30b391f56ff4a24fc6ee374b2540d9204ea724
]
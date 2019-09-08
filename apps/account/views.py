from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializer import *
from rest_framework.generics import CreateAPIView
from rest_framework import mixins, permissions, authentication
from rest_framework.mixins import *
from rest_framework.permissions import *
from rest_framework_jwt.serializers import jwt_encode_handler, jwt_payload_handler
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from api.permission import *
from django.contrib.auth import get_user_model
from rest_framework.decorators import *
from club.models import Club
from rest_framework.status import *

# User = get_user_model()

# class CustomBackend(ModelBackend):
#     """
#     自定义用户验证
#     """
#     def authentication(self, username=None,password=None,**kwargs):
#         pass



class AccountViewSet(ListModelMixin,RetrieveModelMixin,viewsets.GenericViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    authentication_classes = (JSONWebTokenAuthentication,)
    permission_classes = [IsAuthenticated,IsOwners]

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)



class RegisterUserView(CreateAPIView):
    serializer_class = RegisterUserSerializer


class UserViewSet(CreateModelMixin,RetrieveModelMixin,UpdateModelMixin,ListModelMixin,viewsets.GenericViewSet):
    serializer_class = RegisterUserSerializer
    queryset = Account.object.all()
    authentication_classes = (JSONWebTokenAuthentication,)

    def get_serializer_class(self):
        if self.action == "retrieve" :
            print("hhhh")
            return UserDetailSerializer
        elif self.action == "create":
            print("xxx")
            return RegisterUserSerializer
        # elif self.action == "update":
        #     print("update")
        #     return UserinfoSerializer

        return UserDetailSerializer

    def get_permissions(self):
        if self.action == 'retrieve':
            permission_classes = [IsAuthenticated]
        elif self.action=="create":
            print("create")
            # permission_classes = [IsAdminUser]
            permission_classes = []
        else:
            permission_classes = []
        return [permission() for permission in permission_classes]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = self.perform_create(serializer)
        re_dict = serializer.data
        payload = jwt_payload_handler(user)
        re_dict["token"] = jwt_encode_handler(payload)
        # re_dict["nickname"] = user.name if user.name else user.username
        headers = self.get_success_headers(serializer.data)
        print("__________________________________________")
        print(headers)
        return Response(re_dict, status=status.HTTP_201_CREATED, headers=headers)

    def get_object(self):
        return self.request.user

    def perform_create(self,serializer):
        return serializer.save()

    def update(self, request, *args, **kwargs):
        print("update----views")
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)

    def partial_update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)

    def perform_update(self,serializer):
        return serializer.save()

    @detail_route(methods=['get'],url_path='clubs', url_name='clubs',authentication_classes=(JSONWebTokenAuthentication,))
    def clubs(self, request, pk=None,*args, **kwargs):
        clubs = Club.objects.filter(club_administrator=pk).values()
        return Response(clubs,status=HTTP_200_OK)

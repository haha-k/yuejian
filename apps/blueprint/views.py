from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import *
from .serializer import *
from rest_framework.mixins import *
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.parsers import MultiPartParser, FileUploadParser
from rest_framework.viewsets import GenericViewSet
from rest_framework.permissions import *
from .permissions import *

# Create your views here.

class PictureViewSet(CreateModelMixin,RetrieveModelMixin,ListModelMixin,UpdateModelMixin,DestroyModelMixin,viewsets.GenericViewSet):
    authentication_classes = (JSONWebTokenAuthentication,)
    queryset = Picture.objects.all()
    serializer_class = PictureListSerializer

    parser_classer = (MultiPartParser,FileUploadParser,)

    def get_serializer_class(self):
        if self.action == "create":
            return PictureListSerializer
        elif self.action == "update":
            return PictureSerializer
        # elif self.action == "update":
        #     return PictureUpdateSerializer
        return PictureDetailSerializer

    def get_permissions(self):
        permission_classes = [IsAuthenticated,IsOwnerOrReadOnly]
        return [permission() for permission in permission_classes]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        # print(serializer.data)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def update(self, request, *args, **kwargs):
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

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        user = Account.objects.get(id = serializer.data['user'])
        # print(user.username)
        users = {
            'user_id':user.id,
            'username':user.username
        }
        # print(users)
        re_dict = serializer.data
        re_dict['user']=users
        # print(re_dict)
        return Response(re_dict)

    # def destroy(self, request, *args, **kwargs):
    #     instance = self.get_object()
    #     self.perform_destroy(instance)
    #     statusDict = {
    #         'deleted':1
    #     }
    #     return Response(statusDict,status=status.HTTP_204_NO_CONTENT)

    # def list(self, request, *args, **kwargs):
    #     queryset = self.filter_queryset(self.get_queryset())

    #     page = self.paginate_queryset(queryset)
    #     if page is not None:
    #         serializer = self.get_serializer(page, many=True)
    #         return self.get_paginated_response(serializer.data)

    #     serializer = self.get_serializer(queryset, many=True)
    #     return Response(serializer.data)


class BlueprintViewSet(viewsets.ModelViewSet):
    queryset = Blueprint.objects.all()
    serializer_class = BlueprintSerializer
    authentication_classes = (JSONWebTokenAuthentication,)

    def get_permissions(self):
        permission_classes = [IsAuthenticated,IsOwnerOrReadOnly]
        return [permission() for permission in permission_classes]

    def get_serializer_class(self):
        if self.action == "create":
            return BlueprintSerializer
        elif self.action == "update":
            return BlueprintSerializer
        return BlueprintSerializer
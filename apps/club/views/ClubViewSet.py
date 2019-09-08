from django.shortcuts import render
from rest_framework import viewsets
from club.models import *
# from club.serializers import *
from club.serializers import ClubSerializer,AttentionSerializer,ApplicationSerializer,AttentionListSerializer,VideoSerializer
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.permissions import *
from club.permissions import *
from rest_framework.mixins import *
from rest_framework.decorators import *
from rest_framework.status import *
from django.core import serializers
import json
import datetime

class ClubViewSet(viewsets.ModelViewSet):

    authentication_classes = (JSONWebTokenAuthentication,)
    queryset = Club.objects.all()
    serializer_class = ClubSerializer

    def get_serializer_class(self):
        if self.action == "create":
            return ClubSerializer
        return ClubSerializer

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



    @detail_route(methods=['put','delete','get'],url_path='application', url_name='application')
    def master(self, request, pk=None,*args, **kwargs):
        if request.method in ('PUT','DELETE'):
            club = Club.objects.get(club_id=pk)
            if not request.user.is_superuser:
                return Response({
                    "detail":"您没有权限访问"
                },status=HTTP_403_FORBIDDEN)
        if request.method == 'PUT':
            Club.objects.filter(club_id=pk).update(is_apply=1)
            return Response(status=HTTP_201_CREATED)
        elif request.method == 'DELETE':
            Club.objects.filter(club_id=pk).update(is_apply=0)
            return Response(status=HTTP_204_NO_CONTENT)
        elif request.method == 'GET':
            is_apply = Club.objects.get(club_id=pk).is_apply
            print(is_apply)
            return Response({
                'is_apply':is_apply
            },status=HTTP_200_OK)

    @detail_route(methods=['get'],url_path='videos', url_name='videos',serializer_class=(VideoSerializer,))
    def videos(self, request, pk=None,*args, **kwargs):
        videos = Video.objects.filter(club_id=pk).values()
        return Response(videos,status=HTTP_200_OK)
        # queryset = Video.objects.filter(club_id=pk).values()
        # page = self.paginate_queryset(queryset)
        # if page is not None:
        #     serializer = self.get_serializer(page, many=True)
        #     return self.get_paginated_response(serializer.data)

        # serializer = self.get_serializer(queryset, many=True)
        # return Response(serializer.data)

    @detail_route(methods=['get'],url_path='fans', url_name='fans')
    def fans(self, request, pk=None,*args, **kwargs):
        fans = Attention.objects.filter(club_id=pk).values()
        return Response(fans,status=HTTP_200_OK)

    @detail_route(methods=['get'],url_path='coaches', url_name='coaches')
    def coaches(self, request, pk=None,*args, **kwargs):
        coaches = Coach.objects.filter(club_id=pk).values()
        return Response(coaches,status=HTTP_200_OK)

    @detail_route(methods=['get'],url_path='courses', url_name='courses')
    def courses(self, request, pk=None,*args, **kwargs):
        courses = Course.objects.filter(club_id=pk).values()
        return Response(courses,status=HTTP_200_OK)

    @detail_route(methods=['get'],url_path='trains', url_name='trains')
    def trains(self, request, pk=None,*args, **kwargs):
        trains = Train.objects.filter(club_id=pk).values()
        return Response(trains,status=HTTP_200_OK)

    @detail_route(methods=['get'],url_path='masters', url_name='masters')
    def masters(self, request, pk=None,*args, **kwargs):
        masters = Coach.objects.filter(club_id=pk,coach_ismaster=1).values()
        return Response(masters,status=HTTP_200_OK)

    # @detail_route(methods=['get'],url_path='users', url_name='users')
    # def users(self, request, pk=None,*args, **kwargs):
    #     users = Club.objects.filter(club_administrator=pk).values()
    #     return Response(masters,status=HTTP_200_OK)

class AttentionViewSet(DestroyModelMixin,ListModelMixin,CreateModelMixin,RetrieveModelMixin,viewsets.GenericViewSet):
    authentication_classes = (JSONWebTokenAuthentication,)
    queryset = Attention.objects.all()
    serializer_class = AttentionSerializer

    def get_serializer_class(self):
        if self.action in ("create","update"):
            return AttentionSerializer
        return AttentionListSerializer

    def get_permissions(self):
        permission_classes = [IsAuthenticated,IsOwner]
        return [permission() for permission in permission_classes]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        club = serializer.data
        try:
            clubInfo = Club.objects.get(club_id=club['club'])
            print(clubInfo)
            clubInfo.fans+=1
            clubInfo.save()
        except Club.DoesNotExist:
            return Response(status.HTTP_500_INTERNAL_SERVER_ERROR)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        try:
            clubInfo = Club.objects.get(club_id=instance.club_id)
            if clubInfo.fans > 0:
                clubInfo.fans-=1
            clubInfo.save()
        except Club.DoesNotExist:
            return Response(status.HTTP_500_INTERNAL_SERVER_ERROR)
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

class ApplicationViewSet(UpdateModelMixin,viewsets.GenericViewSet):
    queryset = Club.objects.all()
    serializer_class =ApplicationSerializer

    def get_permissions(self):
        permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]

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


class DateEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(obj, date):
            return obj.strftime("%Y-%m-%d")
        else:
            return json.JSONEncoder.default(self, obj)
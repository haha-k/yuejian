from django.shortcuts import render
from rest_framework import viewsets
from club.models import Video
from club.serializers import VideoSerializer,VideoUpdateSerializer
from rest_framework.mixins import *
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.viewsets import GenericViewSet
from rest_framework.permissions import *
from club.permissions import *

class VideoViewSet(viewsets.ModelViewSet):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    authentication_classes = (JSONWebTokenAuthentication,)

    def get_permissions(self):
        permission_classes = [IsAuthenticated,IsClubAdmin]
        return [permission() for permission in permission_classes]

    def get_serializer_class(self):
        if self.action == "create":
            return VideoSerializer
        elif self.action == "update":
            return VideoUpdateSerializer
        return VideoSerializer
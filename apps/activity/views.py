from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializer import *
from rest_framework.mixins import *
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.viewsets import GenericViewSet
from rest_framework.permissions import *
# from club.permissions import *

class ActivityViewSet(viewsets.ModelViewSet):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer
    authentication_classes = (JSONWebTokenAuthentication,)

    def get_permissions(self):
        permission_classes = [IsAuthenticated,]
        return [permission() for permission in permission_classes]

    def get_serializer_class(self):
        if self.action == "create":
            return ActivitySerializer
        elif self.action == "update":
            return ActivitySerializer
        return ActivitySerializer

class ApplyViewSet(viewsets.ModelViewSet):
    queryset = Apply.objects.all()
    serializer_class = ApplySerializer
    authentication_classes = (JSONWebTokenAuthentication,)

    def get_permissions(self):
        permission_classes = [IsAuthenticated,]
        return [permission() for permission in permission_classes]

    def get_serializer_class(self):
        if self.action == "create":
            return ApplySerializer
        elif self.action == "update":
            return ApplySerializer
        return ApplySerializer


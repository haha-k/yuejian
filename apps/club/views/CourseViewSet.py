from django.shortcuts import render
from rest_framework import viewsets
from club.models import Course
from club.serializers import CourseSerializer,CourseUpdateSerializer
from rest_framework.mixins import *
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.viewsets import GenericViewSet
from rest_framework.permissions import *
from club.permissions import *

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    authentication_classes = (JSONWebTokenAuthentication,)

    def get_permissions(self):
        permission_classes = [IsAuthenticated,IsClubAdmin]
        return [permission() for permission in permission_classes]

    def get_serializer_class(self):
        if self.action == "create":
            return CourseSerializer
        elif self.action == "update":
            return CourseUpdateSerializer
        return CourseSerializer
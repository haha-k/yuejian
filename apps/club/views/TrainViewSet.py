from django.shortcuts import render
from rest_framework import viewsets
from club.models import Train
from club.serializers import TrainSerializer,TrainUpdateSerializer
from rest_framework.mixins import *
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.viewsets import GenericViewSet
from rest_framework.permissions import *
from club.permissions import *


class TrainViewSet(viewsets.ModelViewSet):
    queryset = Train.objects.all()
    serializer_class = TrainSerializer
    authentication_classes = (JSONWebTokenAuthentication,)

    def get_permissions(self):
        permission_classes = [IsAuthenticated,IsClubAdmin,IsClubCoach]
        return [permission() for permission in permission_classes]

    def get_serializer_class(self):
        if self.action == "create":
            return TrainSerializer
        elif self.action == "update":
            return TrainUpdateSerializer
        return TrainSerializer

    # @detail_route(methods=['post','delete','get'],url_path='participate', url_name='participate',)
    # def master(self, request, pk=None,*args, **kwargs):
    #     # if request.method in ('POST','DELETE'):
    #     #     club = Coach.objects.get(coach_id=pk).club
    #     #     clubAdmin =club.club_administrator
    #     #     if request.user != clubAdmin:
    #     #         return Response({
    #     #             "detail":"您没有权限访问"
    #     #         },status=HTTP_403_FORBIDDEN)
    #     if request.method == 'POST':
    #         Coach.objects.filter(coach_id=pk).update(coach_ismaster=1)
    #         return Response(status=HTTP_201_CREATED)
    #     elif request.method == 'DELETE':
    #         Coach.objects.filter(coach_id=pk).update(coach_ismaster=0)
    #         return Response(status=HTTP_204_NO_CONTENT)
    #     elif request.method == 'GET':
    #         is_master = Coach.objects.get(coach_id=pk).coach_ismaster
    #         print(is_master)
    #         return Response({
    #             'is_master':is_master
    #         },status=HTTP_200_OK)
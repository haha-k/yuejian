from django.shortcuts import render
from rest_framework import viewsets
from club.models import Club,Attention
from club.serializers import ClubSerializer,AttentionSerializer,ApplicationSerializer
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.permissions import *
from club.permissions import *
from rest_framework.mixins import *

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


class AttentionViewSet(DestroyModelMixin,ListModelMixin,CreateModelMixin,RetrieveModelMixin,viewsets.GenericViewSet):
    authentication_classes = (JSONWebTokenAuthentication,)
    queryset = Attention.objects.all()
    serializer_class = AttentionSerializer

    def get_serializer_class(self):
        if self.action == "create":
            return AttentionSerializer
        return AttentionSerializer

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
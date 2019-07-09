from django.shortcuts import render
from rest_framework import viewsets
from .models import Club
from .serializer import ClubSerializer


# Create your views here.
class ClubViewSet(viewsets.ModelViewSet):
    queryset = Club.objects.all()
    serializer_class = ClubSerializer


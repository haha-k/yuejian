from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializer import *


# Create your views here.
class ContestViewSet(viewsets.ModelViewSet):
    queryset = Contest.objects.all()
    serializer_class = ContestSerializer
from django.shortcuts import render
from rest_framework import viewsets
from .serializers import *


class RegisterView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

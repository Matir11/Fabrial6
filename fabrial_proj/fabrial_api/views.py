from django.shortcuts import render
from rest_framework import viewsets
from .models import Chore
from .serializers import ChoreSerializer, UserSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.contrib.auth.models import User
from rest_framework.authentication import TokenAuthentication
from rest_framework import permissions


class ChoreViewSet(viewsets.ModelViewSet):
    queryset=Chore.objects.all()
    serializer_class=ChoreSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes= (permissions.IsAuthenticated,)

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticated,) 

# Create your views here.

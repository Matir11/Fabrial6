# from django.shortcuts import render
# from rest_framework import viewsets
# from .models import Chore
# from .serializers import ChoreSerializer, UserSerializer
# from rest_framework.permissions import IsAuthenticated, AllowAny
# from django.contrib.auth.models import User
# from rest_framework.authentication import TokenAuthentication
# from rest_framework import permissions


# class ChoreViewSet(viewsets.ModelViewSet):
#     queryset=Chore.objects.all()
#     serializer_class=ChoreSerializer
#     authentication_classes = (TokenAuthentication,)
#     permission_classes= (permissions.IsAuthenticated,)

# class UserViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#     permission_classes = (permissions.IsAuthenticated,) 

# # Create your views here.
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import UserSerializer, GroupSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

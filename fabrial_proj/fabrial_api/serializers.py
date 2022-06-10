# from pkg_resources import require
# from rest_framework import serializers
# from .models import Chore
# from django.contrib.auth.models import User
# from rest_framework.authtoken.models import Token

# class ChoreSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Chore
#         fields = '__all__'

# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ('id','username', 'password')
#         extra_kwargs = {'password': {'required': True, 'write_only':True}}

#         def create(self, validated_data):
#             user = User.objects.create_user(**validated_data)
#             Token.objects.create(user=user)
#             return user

from django.contrib.auth.models import User, Group
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']
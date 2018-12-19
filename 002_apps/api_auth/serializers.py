from rest_framework import serializers
from djoser import serializers as dj_serializers
from django.contrib.auth import authenticate, get_user_model

User = get_user_model()


class UserProfileSerializer(dj_serializers.UserSerializer):


    class Meta:
        model = User
        fields = (
            'email',
            'username',
            'first_name',
            'last_name',
            'title',
            'sex',
            'image_url',
            'role',
            'country',
            'area',
            'region',
            'date_joined',
        )


class CurrentUserSerializer(UserProfileSerializer):
    pass

from django.db import models
from rest_framework import serializers
from rest_framework.serializers import (
    ModelSerializer,
    Serializer,
)

from account.models import (
    Profile,
)

from django.contrib.auth.models import User

from django.contrib.auth.password_validation import validate_password

class ProfileSerializer(ModelSerializer):
    class Meta:
        model = Profile
        fields = ('id', 'note', 'twitter')

class UserSerializer(ModelSerializer):
    profile = ProfileSerializer # nested serializer

    class Meta:
        model=User
        fields = ('id', 'first_name', 'last_name', 'profile')

class ChangePasswordSerializer(Serializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)

    def validate__new_password(self, value):
        validate_password(value)
        return 

class RegisterSerializer(ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta :
        model = User
        fields = ('id', 'username', 'password')

    def validate(self, attr):
        validate_password(attr["password"])
        return attr

    def create(self, validated_data):
        user = User.objects.create(
            username = validated_data["username"]
        )
        user.set_password(validated_data['password']) #user object is created here
        user.save() #user object saved
        return user
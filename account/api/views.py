from django.shortcuts import get_object_or_404
from rest_framework import permissions, serializers, status
from rest_framework.generics import(
    CreateAPIView,
    RetrieveUpdateAPIView,
    get_object_or_404,
)

from rest_framework.permissions import (
    IsAuthenticated
)
from rest_framework.response import Response
from rest_framework.settings import APISettings
from rest_framework.views import APIView
from account.api.permissions import NotAuthenticated

from account.api.serializers import(
    ChangePasswordSerializer,
    ProfileSerializer,
    UserSerializer,
    RegisterSerializer,
)

from django.contrib.auth.models import (
    User,
)

from .permissions import NotAuthenticated

from django.contrib.auth import update_session_auth_hash

class ProfileView(RetrieveUpdateAPIView):
    permissions_classes = IsAuthenticated
    serializer_classes = UserSerializer
    queryset = User.objects.all()

    # lookup_field : we need to define lookup_field when we used any kind of UpdateAPIView
    #               to be able to override this variable we are going to use get_object() method 
    def get_object(self):
        queryset = self.get_queryset()
        obj = get_object_or_404(queryset, id=self.request.user.id)
        return obj

    def perform_update(self, serializer) : # if there is an update operation, this method will run
        serializer.save(user = self.user)

    def update(self, instance, validate_data): # Update and save operations are not automatic in nested serializer
                                                # So, we need to override update handler method
        profile = validate_data.pop('profile')
        profile_serializer = ProfileSerializer(instance=instance.profile, data=profile)
        profile_serializer.is_valid(raise_exception=True) # a kind of security check
        profile_serializer.save()
        return super(UserSerializer, self).update(instance, validate_data)

class UpdatePassword(APIView):
    permission_classes = (IsAuthenticated, )

    def get_object(self, queryset=None): # Return the logged in user's information
        return self.request.user

    def put(self, request, *args, **kwargs):
        self.object = self.get_object()
        data = {
            "old_password" : request.data["old_password"],
            "new_password" : request.data["new_password"]
        }

        serializer = ChangePasswordSerializer(data = data)

        if serializer.is_valid():
            print(serializer)
            old_password = serializer.data.get("old_password")

            if not self.object.check_password(old_password):
                return Response({"old_password" : "wrong_password"}, status=status.HTTP_400_BAD_REQUEST)

            self.object.set_password(serializer.data.get("new_password "))
            self.object.save()

            update_session_auth_hash(request, self.object)
            return Response(status=status.HTTP_204_NO_CONTENT)
        
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

class CreateUserView(CreateAPIView):
    model = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [NotAuthenticated]
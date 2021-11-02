from django.db import models
from rest_framework import fields, serializers
from rest_framework.serializers import(
    ModelSerializer,
    ValidationError,
)

from favourite.models import Favourite

class FavouriteCreateListAPISerializer(ModelSerializer):
    class Meta:
        model = Favourite
        fields = "__all__"

    def validate(self, attrs):
        queryset = Favourite.objects.filter(post=attrs["post"], user = attrs["user"])
        
        if queryset.exists():
            raise ValidationError("Already added to favourites !")

        return attrs

class FavouriteAPISerializer(ModelSerializer):
    class Meta:
        model = Favourite
        fields = ('content',)
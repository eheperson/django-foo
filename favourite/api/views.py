
from rest_framework import serializers

from rest_framework.generics import(
    ListCreateAPIView, # ListCreateAPiView contains both mixins.ListModelMixin and mixins.CreateModelMixin
                       # so it allows us to list and create simultaneously
    RetrieveUpdateAPIView,
    RetrieveDestroyAPIView,
    RetrieveUpdateDestroyAPIView,

)

from rest_framework.permissions import(
    IsAuthenticated,
)

from .paginations import (
    FavouritePagination,
)

from .serializers import (
    FavouriteCreateListAPISerializer,
    FavouriteAPISerializer,

)

from favourite.models import Favourite

from .permissions import(
    IsOwner,
)

class FavouriteListCreateAPIView(ListCreateAPIView):
    # queryset = Favourite.objects.all()
    serializer_class = FavouriteCreateListAPISerializer
    pagination_class = FavouritePagination
    permission_class = [IsAuthenticated]

    def get_queryset(self):
        return  Favourite.objects.filter(user = self.request.user)

    def perform_create(self, serializer):
        serializer.save(user = self.request.user)

class FavouriteRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Favourite.objects.all()
    serializer_class = FavouriteAPISerializer
    lookup_field = 'pk'
    permission_classes = [IsOwner]

class FavouriteRetrieveDestroyAPIView(RetrieveDestroyAPIView):
    queryset = Favourite.objects.all()
    serializer_class = FavouriteAPISerializer
    lookup_field = 'pk'
    permission_classes = [IsOwner]

class FavouriteRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Favourite.objects.all()
    serializer_class = FavouriteAPISerializer
    lookup_field = 'pk'
    permission_classes = [IsOwner]
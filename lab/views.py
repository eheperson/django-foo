from django.shortcuts import render

from rest_framework.generics import (
    ListAPIView, 
    CreateAPIView,
    DestroyAPIView,
    UpdateAPIView,
    RetrieveAPIView
)

from .models import(
    Resistor,
    Capacitor,
    Inductor
)

from .serializers import(
    ResistorCreateSerializer,
    CapacitorCreateSerializer,
    InductorCreateSerializer,
    ResistorListSerializer,
    CapacitorListSerializer,
    InductorListSerializer,
)

from .paginations import(
    ComponentPagination,
)

# Create your views here.


class ResistorCreateView(CreateAPIView):
    queryset = Resistor.objects.all()
    serializer_class = ResistorCreateSerializer
    pagination_class = ComponentPagination

class CapacitorCreateView(CreateAPIView):
    queryset = Capacitor.objects.all()
    serializer_class = CapacitorCreateSerializer
    pagination_class = ComponentPagination

class InductorCreateView(CreateAPIView):
    queryset = Inductor.objects.all()
    serializer_class = InductorCreateSerializer
    pagination_class = ComponentPagination

class ResistorListView(
      ListAPIView,):
    serializer_class = ResistorListSerializer
    pagination_class = ComponentPagination

class CapacitorListView(
      ListAPIView,):
    serializer_class = CapacitorListSerializer
    pagination_class = ComponentPagination

class InductorListView(
      ListAPIView,):
    serializer_class = InductorListSerializer
    pagination_class = ComponentPagination
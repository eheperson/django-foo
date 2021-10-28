
from rest_framework import(
    ModelSerializer,
    SerializerMethodField,
)

from .models import (
    Resistor,
    Capacitor,
    Inductor,
)

class ResistorSerializer(ModelSerializer):
    class Meta:
        model = Resistor
        fields = ('name', 
                  'description', 
                  'manufactrer',
                  'resistance',
                  'unit',
        )

class CapacitorSerializer(ModelSerializer):
    class Meta:
        model = Capacitor
        fields = ('name', 
                  'description', 
                  'manufactrer',
                  'capacitance',
                  'unit',
        )

class InductorSerializer(ModelSerializer):
    class Meta:
        model = Inductor
        fields = ('name', 
                  'description', 
                  'manufactrer',
                  'inductance',
                  'unit',
        )


class ResistorCreateSerializer(ModelSerializer):
    class Meta:
        model = Resistor
        fields = '__all__'

class CapacitorCreateSerializer(ModelSerializer):
    class Meta:
        model = Capacitor
        fields = '__all__'

class InductorCreateSerializer(ModelSerializer):
    class Meta:
        model = Inductor
        fields = '__all__'

class ResistorListSerializer(ModelSerializer):
    class Meta:
        model = Resistor
        fields = '__all__'
        depth = 1

class CapacitorListSerializer(ModelSerializer):
    class Meta:
        model = Capacitor
        fields = '__all__'
        depth = 1

class InductorListSerializer(ModelSerializer):
    class Meta:
        model = Inductor
        fields = '__all__'
        depth = 1
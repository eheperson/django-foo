from django.db import models

# Create your models here.


class General(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=400) 
    manufacturer = models.CharField(max_length=100)
    created = models.DateTimeField(editable=False)

class Resistor(models.Model):
    general = models.ForeignKey(General, on_delete=models.CASCADE)
    resistance = models.FloatField()
    unit = models.CharField(max_length=10)

    def __str__(self):
        return self.resistance + self.unit +  self.general.name

class Capacitor(models.Model):
    general = models.ForeignKey(General, on_delete=models.CASCADE)
    capacitance = models.FloatField()
    unit = models.CharField(max_length=10)

    def __str__(self):
        return self.capacitance + self.unit +  self.general.name

class Inductor(models.Model):
    general = models.ForeignKey(General, on_delete=models.CASCADE)
    inductance = models.FloatField()
    unit = models.CharField(max_length=10)

    def __str__(self):
        return self.inductance + self.unit +  self.general.name
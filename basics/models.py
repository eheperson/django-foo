from django.db import models

# Create your models here.


class Dummy(models.Model):
    name = models.CharField(max_length=200)
    age = models.CharField(max_length=200)
    bullshit = models.CharField(max_length=200)
    published_date = models.DateTimeField('date published')
    
    def __str__(self):
        return self.name + " - " + self.bullshit
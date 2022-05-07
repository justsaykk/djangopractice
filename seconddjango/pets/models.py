from django.db import models

# Create your models here.
#The Model class we will inherit from
from django.db import models

#new model class
class Dog(models.Model):
    # define a string field of max 100 characters
    name = models.CharField(max_length=100)
    # define a age that is an integer
    age = models.IntegerField()
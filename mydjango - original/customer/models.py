from django.db import models
from django.db import models

# Create your models here.
class Customer(models.Model):
     name = models.CharField(max_length=150)
     number = models.IntegerField()
     detials = models.CharField(max_length=200)
     email = models.CharField(max_length=50)
     gender = models.CharField(max_length=1)

     def __str__(self) -> str:
          return self.name 
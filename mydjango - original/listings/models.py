from re import A
from turtle import title
from django.db import models

# Create your models here.
class Listing(models.Model):
    title = models.CharField(max_length=150)
    price =models.IntegerField()
    num_bedrooms= models.IntegerField()
    square_footage = models.IntegerField()
    address = models.CharField(max_length=100)


    def __str__(self) -> str:
        return self.title 


        
        
        
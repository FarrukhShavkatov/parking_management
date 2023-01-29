from django.contrib import admin
from django.db import models
from django.contrib.auth.models import User

# Register your models here.


class Car(models.Model):
    number = models.CharField(max_length=8)
    color = models.CharField(max_length=50)
    brand = models.CharField(max_length=100)
    
    
class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    phone =  models.CharField(max_length=13)

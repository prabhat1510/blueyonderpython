from django.db import models


# Create your models here.
class Data(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    
class Customer(models.Model):
        cname = models.CharField(max_length=100)
        #dob = models.DateField(auto_now_add=True)
        dob = models.DateTimeField()
        email = models.CharField(max_length=100)
        city = models.CharField(max_length=100)
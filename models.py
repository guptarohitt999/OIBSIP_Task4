from django.db import models

# Create your models here.

class Employee(models.Model):
    Name=models.CharField(max_length=100)
    Email=models.EmailField()
    Phone=models.CharField(max_length=100)
    Address=models.TextField()

class signup(models.Model):
    Name=models.CharField(max_length=100)
    Email=models.EmailField()
    Phone=models.CharField(max_length=100)
    Password=models.CharField(max_length=100)
    Gender = models.CharField(max_length=1)
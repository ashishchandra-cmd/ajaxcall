from django.db import models

# Create your models here.
class Registation(models.Model):
    Name=models.CharField(max_length=100)
    Phone=models.IntegerField()
    Email=models.EmailField()
    Password=models.CharField(max_length=50)
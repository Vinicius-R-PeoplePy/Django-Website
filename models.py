from django.db import models 

class User(models.Model):
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(unique=True)
    birthdate = models.DateField()
    password = models.CharField(max_length=100)


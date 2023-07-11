from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=64)
    email = models.CharField(max_length=64)
    address = models.CharField(max_length=124)
    message = models.TextField()
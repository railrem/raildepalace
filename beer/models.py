from django.db import models

# Create your models here.

class Beer(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    brand = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
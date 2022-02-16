from django.db import models

# Create your models here.

class Products(models.Model):
    name = models.CharField(max_length = 255)
    color = models.CharField(max_length = 255)
    weight = models.DecimalField(max_digits=8, decimal_places=2)
    price = models.DecimalField(max_digits=8, decimal_places=2)
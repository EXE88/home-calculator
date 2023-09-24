from django.db import models

class Material(models.Model):
    name = models.CharField(max_length=50)
    group = models.CharField(max_length=50)
    brand = models.CharField(max_length=50)
    unit = models.CharField(max_length=50)
    price = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    last_price = models.CharField(max_length=50)

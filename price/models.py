from django.db import models

class Material(models.Model):
    name = models.CharField()
    group = models.CharField()
    brand = models.CharField()
    unit = models.CharField()
    price = models.CharField()
    description = models.CharField()
    last_price = models.CharField()

from django.db import models

# Create your models here.

class Peak(models.Model):
    name = models.CharField(max_length=128)
    lat = models.FloatField()
    lon = models.FloatField()
    altitude = models.FloatField()

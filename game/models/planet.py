from django.db import models


class Planet(models.Model):
    name = models.CharField(max_length=80)
    diameter = models.IntegerField()
    min_temperature = models.FloatField()
    max_temperature = models.FloatField()
    fields = models.IntegerField()
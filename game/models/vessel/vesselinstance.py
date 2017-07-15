from django.db import models


class VesselInstance(models.Model):
    owner = models.ForeignKey('Player', null=True, blank=True)
    template = models.ForeignKey('VesselTemplate')
    current_hull_points = models.IntegerField()
    amount = models.IntegerField()

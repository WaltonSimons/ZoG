from django.db import models


class Vessel(models.Model):
    name = models.CharField(max_length=80)
    engine_slots = models.IntegerField()
    weapon_slots = models.IntegerField()
    utility_slots = models.IntegerField()

    def __str__(self):
        return self.name

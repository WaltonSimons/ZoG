from django.db import models


class Weapon(models.Model):
    name = models.CharField(max_length=80)
    hull_points = models.IntegerField()
    attack_power = models.IntegerField()
    required_technologies = models.ManyToManyField('TechnologyLevel')

    def __str__(self):
        return self.name

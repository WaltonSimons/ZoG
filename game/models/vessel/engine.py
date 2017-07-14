from django.db import models


class Engine(models.Model):
    name = models.CharField(max_length=80)
    hull_points = models.IntegerField()
    speed_points = models.IntegerField()
    required_technologies = models.ManyToManyField('TechnologyLevel')

    def __str__(self):
        return self.name

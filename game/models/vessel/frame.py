from django.db import models


class Frame(models.Model):
    name = models.CharField(max_length=80)
    hull_points = models.IntegerField()
    speed_modifier = models.FloatField()
    required_technologies = models.ManyToManyField('TechnologyLevel')

    def __str__(self):
        return self.name

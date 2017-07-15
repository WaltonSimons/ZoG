from django.db import models


class VesselTemplate(models.Model):
    name = models.CharField(max_length=80)
    owner = models.ForeignKey('Player', null=True, blank=True)
    frame = models.ForeignKey('Frame')
    engine_slots = models.IntegerField()
    weapon_slots = models.IntegerField()
    utility_slots = models.IntegerField()
    engines = models.ManyToManyField('Engine')
    weapons = models.ManyToManyField('Weapon')
    utilities = models.ManyToManyField('Utility')

    def __str__(self):
        return self.name

    def get_maximum_hull_points(self):
        hull_points = self.frame.hull_points
        for engine in self.engines.all():
            hull_points += engine.hull_points
        for weapon in self.weapons.all():
            hull_points += weapon.hull_points
        for utility in self.utilities.all():
            hull_points += utility.hull_points
        return hull_points

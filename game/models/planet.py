from django.db import models
import random

PLANET_TYPES = (
    ('planet', 'Planet'),
    ('moon', 'Moon'),
    ('station', 'Station'),
)


class Planet(models.Model):
    name = models.CharField(max_length=80)
    owner = models.ForeignKey('Player', null=True, blank=True)
    diameter = models.IntegerField()
    min_temperature = models.IntegerField()
    max_temperature = models.IntegerField()
    fields = models.IntegerField()
    type = models.CharField(choices=PLANET_TYPES, max_length=64, default='planet')

    def __str__(self):
        return self.name

    @staticmethod
    def create_random_planet():
        diameter = random.randint(3865, 15000)
        temperature_difference = random.randint(15, 80)
        min_temperature = random.randint(-40, 10)
        max_temperature = min_temperature + temperature_difference
        fields = diameter / 60

        planet = Planet.objects.create(name='Home Planet',
                                       diameter=diameter,
                                       min_temperature=min_temperature,
                                       max_temperature=max_temperature,
                                       fields=fields,
                                       type='planet')
        return planet

from django.db import models
from .planet import Planet


class Location(models.Model):
    sector = models.IntegerField()
    system = models.IntegerField()
    orbit = models.IntegerField()
    planet = models.ForeignKey('Planet', related_name='location', null=True, blank=True)

    def __str__(self):
        return '%d-%d-%d' % (self.sector, self.system, self.orbit)

    @staticmethod
    def get_system(sector, system):
        res = Location.objects.filter(sector=sector, system=system)
        return res

    @staticmethod
    def get_planet(sector, system, orbit):
        location = Location.objects.filter(sector=sector, system=system, orbit=orbit)
        if location:
            res = location[0].planet
        else:
            res = None
        return res

    @staticmethod
    def create_locations(max_sectors, max_systems, max_planets):
        for x in range(1, max_sectors+1):
            for y in range(1, max_systems+1):
                for z in range(1, max_planets+1):
                    planet = Planet.create_random_planet()
                    Location.objects.create(sector=x, system=y, orbit=z, planet=planet)

from django.db import models


class Location(models.Model):
    sector = models.IntegerField()
    system = models.IntegerField()
    orbit = models.IntegerField()
    planet = models.ForeignKey('Planet', related_name='location', null=True, blank=True)

    def __str__(self):
        return '%d-%d-%d' % (self.sector, self.system, self.planet)

    @staticmethod
    def get_system(sector, system):
        res = Location.objects.filter(sector=sector, system=system)
        return res

    @staticmethod
    def create_locations(max_sectors, max_systems, max_planets):
        for x in range(1, max_sectors):
            for y in range(1, max_systems):
                for z in range(1, max_planets):
                    Location.objects.create(sector=x, system=y, planet=z)


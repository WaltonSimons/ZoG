from django.db import models


class BuildingLevel(models.Model):
    level = models.IntegerField()
    ticks_to_build = models.IntegerField()
    building = models.ForeignKey('Building', related_name='levels')

    def __str__(self):
        return '%s - level %d' % (self.building.name, self.level)

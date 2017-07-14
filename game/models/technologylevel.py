from django.db import models


class TechnologyLevel(models.Model):
    level = models.IntegerField()
    ticks_to_research = models.IntegerField()
    technology = models.ForeignKey('Technology', related_name='levels')

    def __str__(self):
        return '%s - level %d' % (self.technology.name, self.level)

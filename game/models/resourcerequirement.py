from django.db import models

REQUIREMENT_TYPES = (
    ('technology', 'Technology'),
    ('building', 'Building'),
)


class ResourceRequirement(models.Model):
    type = models.CharField(choices=REQUIREMENT_TYPES, max_length=64, default='technology')
    technology_level = models.ForeignKey('TechnologyLevel', related_name='resources', null=True, blank=True)
    building_level = models.ForeignKey('BuildingLevel', related_name='resources', null=True, blank=True)
    resource = models.ForeignKey('Resource')
    amount = models.IntegerField()

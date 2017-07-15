from django.db import models

EFFECT_TYPES = (
    ('change_value', 'Change by value'),
    ('change_percent', 'Change by percent'),
)

BOOST_TYPES = (
    ('resource', 'Resource'),
    ('building', 'Building speed'),
    ('research', 'Research speed'),
    ('planet_defense', 'Planet defense'),
    ('planet_attack', 'Planet attack power'),
)


class PlanetEffect(models.Model):
    type = models.CharField(choices=EFFECT_TYPES, max_length=64, default='change_value')
    value = models.IntegerField()
    percent = models.FloatField()
    boost_type = models.CharField(choices=BOOST_TYPES, max_length=64, default='resource')
    resource = models.ForeignKey('Resource', null=True, blank=True)

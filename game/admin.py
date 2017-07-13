from django.contrib import admin
from .models import resourcerequirement, resource

# Register your models here.

admin.site.register(resourcerequirement.ResourceRequirement)
admin.site.register(resource.Resource)


from game.models.location import Planet, Location
from django.http import HttpResponse
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt

# Create your views here.


@csrf_exempt
def planet(request, method):
    if method in METHODS:
        res = METHODS[method](request)
    return HttpResponse(res)


def get_by_id(request):
    planet_id = request.GET.get('id')
    try:
        planet = Planet.objects.get(pk=planet_id)
        return serializers.serialize('json', [planet])
    except Exception:
        return None


def get_by_coordinates(request):
    get = request.GET
    sector = get.get('sector')
    system = get.get('system')
    orbit = get.get('orbit')
    return serializers.serialize('json', [Location.get_planet(sector, system, orbit)])


def update(request):
    post = request.POST
    planet_id = post.get('id')
    name = post.get('name')
    owner = post.get('owner_id')
    diameter = post.get('diameter')
    min_temperature = post.get('min_temperature')
    max_temperature = post.get('max_temperature')
    fields = post.get('fields')
    planet_type = post.get('type')

    planet = Planet.objects.get(pk=planet_id)

    if name:
        planet.name = name
    if owner:
        planet.owner = owner
    if diameter:
        planet.diameter = diameter
    if min_temperature:
        planet.min_temperature = min_temperature
    if max_temperature:
        planet.max_temperature = max_temperature
    if fields:
        planet.fields = fields
    if planet_type:
        planet.type = planet_type

    planet.save()


def delete(request):
    post = request.POST
    planet_id = post.get('id')
    planet = Planet.objects.get(pk=planet_id)
    planet.delete()


METHODS = {
    'get_by_id': get_by_id,
    'get_by_coordinates': get_by_coordinates,
    'update': update,
    'delete': delete,
}

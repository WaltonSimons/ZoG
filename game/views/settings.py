from game.models.location import Planet, Location
from django.http import HttpResponse
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt

# Create your views here.


@csrf_exempt
def settings(request, method):
    if method in METHODS:
        res = METHODS[method](request)
    return HttpResponse(res)


def generate_world(request):
    post = request.POST
    planets = int(post.get('planets'))
    systems = int(post.get('systems'))
    sectors = int(post.get('sectors'))
    Location.create_locations(sectors, systems, planets)
    return HttpResponse('World generated.')

METHODS = {
    'generate_world': generate_world,
}

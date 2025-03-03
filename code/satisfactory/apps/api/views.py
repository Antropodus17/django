from django.http import HttpResponseRedirect, JsonResponse  # type:ignore

from apps.objects.models import *
from apps.objects.views import getMarkers
from apps.calculators.models import Generator


def generators(request):
    generators = Generator.objects.all()
    response = {"generators": []}
    for generator in generators:
        response["generators"].append(Generator2Json(generator))
    return JsonResponse(response)


def generatorDetails(request, pk):
    generator = Generator.objects.get(pk=pk)
    response = Generator2Json(generator)
    return JsonResponse(response)


def markers(request):
    markers = getMarkers(request)
    return JsonResponse({"markers": markers})


def all(request, object_name):
    response = {"objects": []}
    if object_name == "resources":
        resources = Resource.objects.all()
        for resource in resources:
            response["objects"].append(Resource2Json(resource))
    elif object_name == "recipes":
        recipes = Recipe.objects.all()

        for recipe in recipes:
            response["objects"].append(Recipe2Json(recipe))
    return JsonResponse(response)


def details(request, object_name, pk):
    if object_name == "resources":
        resource = Resource.objects.get(pk=pk)
        response = Resource2Json(resource)
    elif object_name == "recipes":
        recipe = Recipe.objects.get(pk=pk)
        response = Recipe2Json(recipe)
    return JsonResponse(response)


def Resource2Json(resource):
    return {
        "id": resource.id,
        "name": resource.name,
        "messure": resource.messure,
    }


def Recipe2Json(recipe):
    return {
        "id": recipe.id,
        "id_craft_resource": Resource2Json(recipe.id_craft_resource),
        "id_needed_resource": Resource2Json(recipe.id_needed_resource),
        "cuantity": recipe.cuantity,
    }


def Generator2Json(generator):
    return {
        "id": generator.id,
        "name": generator.name,
        "power": generator.power,
    }

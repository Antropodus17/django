from django.http import HttpResponseRedirect, JsonResponse

from apps.objects.models import *


def all(request, object_name):
    if object_name == "resources":
        resources = Resource.objects.all()
        response = []
        for resource in resources:
            response.append(Resource2Json(resource))
    elif object_name == "recipes":
        recipes = Recipe.objects.all()
        response = []
        for recipe in recipes:
            response.append(Recipe2Json(recipe))
    return JsonResponse(response, safe=False)


def details(request, object_name, pk):
    if object_name == "resources":
        resource = Resource.objects.get(pk=pk)
        response = Resource2Json(resource)
    elif object_name == "recipes":
        recipe = Recipe.objects.get(pk=pk)
        response = Recipe2Json(recipe)
    return JsonResponse(response)


def Resource2Json(resource):
    return {"id": resource.id, "name": resource.name, "messure": resource.messure}


def Recipe2Json(recipe):
    return {
        "id": recipe.id,
        "id_craft_resource": Resource2Json(recipe.id_craft_resource),
        "id_needed_resource": Resource2Json(recipe.id_needed_resource),
        "cuantity": recipe.cuantity,
    }

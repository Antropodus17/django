from django.shortcuts import render, get_object_or_404
from .models import Generator, Recipe, Resource

# Create your views here.


def home(request):
    return render(request, "calculator_index.html")


def energy(request):
    generators = Generator.objects.all()

    return render(request, "generators.html", context={"generators": generators})


def resources(request):

    def recursividad(objeto):
        pass

    prueba = {2: "adios"}
    objetos = Resource.objects.all()
    receta = get_object_or_404(Recipe, pk=int(request.GET.get("clave")))
    if request.GET.get("recursivo"):
        pass

    prueba = prueba
    return render(
        request,
        "resources.html",
        context={"resources": objetos, "receta": prueba},
    )

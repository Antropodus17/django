from django.shortcuts import render
from .models import Generator

# Create your views here.


def home(request):
    return render(request, "calculator_index.html")


def energy(request):
    generators = Generator.objects.all()

    return render(request, "generators.html", context={"generators": generators})

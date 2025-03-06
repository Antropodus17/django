from django.shortcuts import render
from django.views.generic import TemplateView
from django.views import View

from .models import Generator
from apps.objects.models import Resource, Recipe

# Create your views here.


class CalculatorList(View):
    def get(self, request):
        return render(request, "apps/calculator/list.html")

    def post(self, request):
        return render(request, "apps/calculator/list.html")


class EnergyCalculator(View):
    def get(self, request):
        context = {}
        context["generators"] = Generator.objects.all()
        origin = self.request.META["HTTP_HOST"]
        context["origin"] = f"{origin}"
        return render(request, "apps/calculator/energy.html", context)

    def post(self, request):
        self.get(request)


class ResourcesCalculator(TemplateView):
    def get(self, request):
        context = {}
        context["resources"] = Resource.objects.all()
        origin = self.request.META["HTTP_HOST"]
        context["origin"] = f"{origin}"
        return render(request, "apps/calculator/resource.html", context)

    def post(self, request):
        return self.get(request)

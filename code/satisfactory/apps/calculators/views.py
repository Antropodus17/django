from django.shortcuts import render
from django.views.generic import TemplateView
from django.views import View

# Create your views here.


class CalculatorList(View):
    def get(self, request):
        return render(request, "apps/calculator/list.html")

    def post(self, request):
        return render(request, "apps/calculator/list.html")


class EnergyCalculator(TemplateView):
    pass


class ResourcesCalculator(TemplateView):
    pass

from django.urls import path, include

from . import views

app_name = "calculator"

urlpatterns = [
    path("list/", views.CalculatorList.as_view(), name="list"),
    path("energy/", views.EnergyCalculator.as_view(), name="energy"),
    path("resources/", views.ResourcesCalculator.as_view(), name="resources"),
    path("recipes/", include()),
]

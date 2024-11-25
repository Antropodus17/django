from django.urls import path
from . import views

app_name = "calculator"

urlpatterns = [
    path("", views.home, name="home"),
    path("energy/", views.energy, name="energy"),
    path("resources/", views.resources, name="resources"),
]

from django.urls import path
from . import views

appname = "book"

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:id>", views.details, name="details"),
]

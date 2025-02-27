from django.urls import path, include  # type:ignore

from . import views

app_name = "api"

urlpatterns = [
    path("<str:object_name>/", views.all, name="all"),
    path("<str:object_name>/<int:pk>", views.details, name="details"),
]

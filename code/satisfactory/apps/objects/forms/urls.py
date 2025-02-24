from django.urls import path  # type:ignore

from . import views

app_name = "forms"

urlpatterns = [
    path("add/", views.ResourceCreateView.as_view(), name="create"),
    path("delete/", views.ResourceDeleteView.as_view(), name="delete"),
    path("update/", views.ResourceUpdateView.as_view(), name="update"),
]

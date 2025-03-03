from django.urls import path, include  # type:ignore

from . import views

app_name = "recipes"

urlpatterns = [
    path("create/<int:pk>", views.RecipeCreateView.as_view(), name="create"),
    path("update/<int:pk>", views.RecipeUpdateView.as_view(), name="update"),
    path("delete/<int:pk>", views.RecipeDeleteView.as_view(), name="delete"),
]

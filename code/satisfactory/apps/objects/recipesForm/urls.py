from django.urls import path, include  # type:ignore

from . import views

app_name = "recipes"

urlpatterns = [
    path("create/<int:pk>", views.RecipeCreateView.as_view(), name="create"),
    # path("update/<int:pk>", views, name="update"),
    # path("delete/<int:pk>", views, name="delete"),
]

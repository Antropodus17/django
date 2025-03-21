from django.urls import path, include  # type:ignore

from . import views
from .forms import urls
from .recipesForm import urls as rec_urls


app_name = "objects"

urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path("list/", views.ObjectsList.as_view(), name="list"),
    path("details/<int:pk>", views.DetailsView.as_view(), name="details"),
    path("process/marker/", views.ProcessMarker.as_view(), name="process_marker"),
    # I MADE AN FOLD/MODULE TO SAVE ALL THE FORMS INFORMATION, LIKE URLS AND VIEWS
    path("forms/", include(urls)),
    path("recipes/<int:pk>/", views.RecipeView.as_view(), name="recipe"),
    path("recipes/modify/", include(rec_urls)),
]

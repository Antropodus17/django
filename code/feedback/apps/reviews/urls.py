from django.urls import path
from . import views

app_name = "reviews"

urlpatterns = [
    path("", views.home, name="home"),
    path("thank-you", views.thank_you, name="thank_you"),
]

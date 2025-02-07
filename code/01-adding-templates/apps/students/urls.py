from django.contrib import admin
from django.urls import path

from . import views

app_name = "students"

urlpatterns = [
    path("", views.StudentListView.as_view(), name="list"),
    path("register/", views.StudentRegisterView.as_view()),
    path("delete/<int:pk>/", views.StudentDeleteView.as_view(), name="delete"),
    path("update/<int:pk>/", views.StudentUpdateView.as_view(), name="update"),
]

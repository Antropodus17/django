from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path("", views.StudentListView.as_view()),
    path("register/", views.StudentRegisterView.as_view()),
]

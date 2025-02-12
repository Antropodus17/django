from django.urls import path
from . import views

app_name = "courses"

urlpatterns = [
    path("", views.aplication, name="home"),
    path("courses", views.allCourses, name="allCourses"),
    path("details-<int:course_id>", views.courseDetails, name="details"),
]

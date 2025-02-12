from django.shortcuts import render, get_object_or_404
from .models import Courses

# Create your views here.


def home(request):
    return render(request, "project/index.html")


def aplication(request):
    return render(request, "apps/courses/index.html")


def allCourses(request):
    cursos = Courses.objects.all()[:1]
    return render(request, "apps/courses/allCourses.html", {"cursos": cursos})


def courseDetails(request, course_id):
    curso = get_object_or_404(Courses, pk=course_id)
    return render(request, "apps/courses/details.html", {"curso": curso})

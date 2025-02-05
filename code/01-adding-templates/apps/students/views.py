from django.shortcuts import render

from django.views.generic.edit import CreateView
from django.views.generic import ListView


from .models import Student
from .forms import StudentForm

# Create your views here.


class StudentRegisterView(CreateView):
    model = Student
    form_class = StudentForm
    template_name = "students/register.html"
    success_url = "/students"


class StudentListView(ListView):
    model = Student
    template_name = "students/list.html"

from django.shortcuts import render

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView
from django.urls import reverse_lazy

from .models import Student
from .forms import StudentForm

# Create your views here.


class StudentRegisterView(CreateView):
    model = Student
    form_class = StudentForm
    template_name = "students/register.html"
    success_url = "/students"


class StudentDeleteView(DeleteView):
    model = Student
    template_name = "students/delete.html"
    success_url = reverse_lazy("students:list")


class StudentUpdateView(UpdateView):
    model = Student
    form_class = StudentForm
    template_name = "students/update.html"
    template_name_suffix = "update_form"

    success_url = reverse_lazy("students:list")


class StudentListView(ListView):
    model = Student
    template_name = "students/list.html"
    context_object_name = "students"

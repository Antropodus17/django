from django.shortcuts import render


# Create your views here.


def home(request):
    return render(request, "index.html")


def form(request):
    return render(request, "form.html")


def validateForm(request):
    from validations import userlogin

    return userlogin.validate(request)

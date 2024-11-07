from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.


def home(request):
    return render(
        request,
        "generator/index_structure.html",
        {"password": "sdfjasuvbausbasuguxaujcbasufua894564"},
    )


def about(request):
    return render(request, "generator/about_structure.html")


def password(request):
    characters = list("abcdefghijklmnñopqrstuvwxyz")
    length = int(request.GET.get("length", 25))

    if request.GET.get("uppercase"):
        characters.extend(list("ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"))
    if request.GET.get("numbers"):
        characters.extend(list("0123456789"))
    if request.GET.get("special"):
        characters.extend(list("@#$%&=?¿!¡.,-<>:;()"))
    thepassword = ""
    for c in range(0, length):
        thepassword += random.choice(characters)
    return render(
        request, "generator/password_structure.html", {"password": thepassword}
    )

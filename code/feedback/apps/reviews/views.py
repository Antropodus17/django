from django.shortcuts import render  # type: ignore
from django.http import HttpResponseRedirect  # type: ignore
import json

# from django.views import View

from .models import Review, NovellServiceModel
from .forms import NovellServicesForm

# Create your views here.


# class HomeView(View):
#     def get(self, request):
#         form = ReviewForm()
#         return render(request, "apps/reviews/form.html", {"form": form})

#     def post(self, request):
#         form = ReviewForm(request.POST)
#         if form.is_valid():
#             # review = Review()
#             # review.user_name = form.cleaned_data["user_name"]
#             # review.review_text = form.cleaned_data["review_text"]
#             # review.rating = form.cleaned_data["rating"]
#             # print(review)
#             form.save()
#             return HttpResponseRedirect("thank-you")


# def home(request):

#     if request.method == "POST":
#         # entered_username = request.POST["username"]
#         form = ReviewForm(request.POST)
#         if form.is_valid():
#             # review = Review()
#             # review.user_name = form.cleaned_data["user_name"]
#             # review.review_text = form.cleaned_data["review_text"]
#             # review.rating = form.cleaned_data["rating"]
#             # print(review)
#             form.save()
#             return HttpResponseRedirect("thank-you")
#     else:
#         form = ReviewForm()

#     return render(request, "apps/reviews/form.html", {"form": form})


######### START EJERCICIO 5.1
######### START EJERCICIO 5.2


def home(request):
    if request.POST:
        form = NovellServicesForm(request.POST)
        if form.is_valid():
            datos = form.cleaned_data
            print(datos)
            modelo = NovellServiceModel()
            modelo.user_name = datos.get("user_name")
            modelo.password = datos.get("password")
            modelo.city = datos.get("city")
            modelo.web_server = datos.get("web_server")
            modelo.role = datos.get("role")
            modelo.sign_on = datos.get("sign_on")
            modelo.save()
    else:
        form = NovellServicesForm()

    return render(request, "apps/reviews/form.html", {"form": form})


######### END EJERCICIO 5.1
######### END EJERCICIO 5.2


def thank_you(request):
    return render(request, "apps/reviews/thank_you.html")

from django.shortcuts import render  # type: ignore
from django.http import HttpResponseRedirect  # type: ignore
from django.views import View  # type: ignore


from .models import Review
from .forms import ReviewForm, NovellServicesForm

# Create your views here.


class HomeView(View):
    def get(self, request):
        form = ReviewForm()
        return render(request, "apps/reviews/form.html", {"form": form})

    def post(self, request):
        form = ReviewForm(request.POST)
        if form.is_valid():
            # review = Review()
            # review.user_name = form.cleaned_data["user_name"]
            # review.review_text = form.cleaned_data["review_text"]
            # review.rating = form.cleaned_data["rating"]
            # print(review)
            form.save()
            return HttpResponseRedirect("thank-you")


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


######### EJERCICIO 5.1
# def home(request):
#     if request.POST:
#         form = NovellServicesForm(request.POST)
#         # print(form.cleaned_data)
#         if form.is_valid():
#             datos = form.cleaned_data
#             # for dato in datos:
#             #     form[dato] = datos[dato]

#     else:
#         form = NovellServicesForm()

#     return render(request, "apps/reviews/form.html", {"form": form})


def thank_you(request):
    return render(request, "apps/reviews/thank_you.html")

from django.shortcuts import render
from django.http import HttpResponseRedirect

from .models import Review
from .forms import ReviewForm, NovellServicesForm

# Create your views here.


# def home(request):

#     if request.method == "POST":
#         # entered_username = request.POST["username"]
#         form = ReviewForm(request.POST)
#         if form.is_valid():
#             review = Review()
#             review.user_name = form.cleaned_data["user_name"]
#             review.review_text = form.cleaned_data["review_text"]
#             review.rating = form.cleaned_data["rating"]
#             print(review)
#             return HttpResponseRedirect("thank-you")
#     else:
#         form = ReviewForm()

#     return render(request, "apps/reviews/form.html", {"form": form})


def home(request):
    if request.POST:
        form = NovellServicesForm(request.POST)
        if form.is_valid:
            # print(form.data.values)
            for k, v in form.data.items():
                print(f"{k}: {v}")
    else:
        form = NovellServicesForm()
    return render(request, "apps/reviews/form.html", {"form": form})


def thank_you(request):
    return render(request, "apps/reviews/thank_you.html")

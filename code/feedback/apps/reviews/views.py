from django.shortcuts import render
from django.http import HttpResponseRedirect

# Create your views here.


def home(request):

    if request.method == "POST":
        entered_username = request.POST["username"]
        print(entered_username)
        return HttpResponseRedirect("thank-you")

    return render(
        request,
        "apps/reviews/form.html",
    )


def thank_you(request):
    return render(request, "apps/reviews/thank_you.html")

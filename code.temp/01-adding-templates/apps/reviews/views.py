from .models import Review
from django.http import HttpResponseRedirect  # type:ignore
from django.shortcuts import render  # type:ignore
from django.views import View  # type:ignore
from django.views.generic.base import TemplateView  # type:ignore
from django.views.generic import ListView, DetailView  # type:ignore
from django.views.generic.edit import FormView  # type:ignore
from .forms import ReviewForm  # type:ignore

# Create your views here.


class ReviewView(FormView):

    form_class = ReviewForm
    template_name = "reviews/review.html"
    success_url = "/thank-you"

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


# with VIEW asecas
# def get(self, request):
# form = ReviewForm()
#
# return render(request, "reviews/review.html", {"form": form})
#
# def post(self, request):
# form = ReviewForm(request.POST)
#
# if form.is_valid():
# form.save()
# return HttpResponseRedirect("/thank-you")
#
# return render(request, "reviews/review.html", {"form": form})


def thank_you(request):
    return render(request, "reviews/thank_you.html")


class ThankYouView(TemplateView):
    template_name = "reviews/thank_you.html"

    def get_context_data(self, **kwargs) -> dict[str, any]:
        context = super().get_context_data(**kwargs)
        context["message"] = "This works!"
        return context


class ReviewListView(ListView):
    template_name = "reviews/review_list.html"
    model = Review
    context_object_name = "reviews"


class SingleReviewView(DetailView):
    template_name = "reviews/single_review.html"
    model = Review
    # context_object_name = "reviews"

from django.shortcuts import render, get_object_or_404
from django.db.models import Avg, Min
from .models import Book

# Create your views here.


def index(request):
    books = Book.objects.all().order_by("-raiting")
    num_books = books.count()
    avg_raiting = books.aggregate(Avg("raiting"), Min("raiting"))

    return render(
        request,
        "index_book.html",
        {"books": books, "total_books": num_books, "avg": avg_raiting},
    )


def details(request, slug):
    book = get_object_or_404(Book, slug=slug)
    return render(
        request,
        "details_book.html",
        {
            "title": book.title,
            "author": book.author,
            "is_bestsealing": book.is_bestsealing,
        },
    )

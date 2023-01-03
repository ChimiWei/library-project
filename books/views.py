from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Book
from .models import User
from .forms import BookForm
import datetime
import requests


def home(request):
    data = {"today": datetime.datetime.now(), "users": User.objects.all()}
    print(data)
    return render(request, "books/home.html", data)


def Booklist(request):
    data = {"books": Book.objects.all()}
    return render(request, "books/book_list.html", data)


def add(request):
    data = {}
    form = BookForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("url_list")
    data["form"] = form
    return render(request, "books/form.html", data)


def update(request, pk):
    data = {}
    book = Book.objects.get(pk=pk)
    form = BookForm(request.POST or None, instance=book)

    if form.is_valid():
        form.save()
        return redirect("url_list")

    data["form"] = form
    data["book"] = book
    return render(request, "books/form.html", data)


def delete(request, pk):
    book = Book.objects.get(pk=pk)
    book.delete()
    return redirect("url_list")

def preco_filtro(request, min, max):
    data = {"books": Book.objects.filter(price__gte=min, price__lte=max).values()}
    return render(request, "books/book_list.html", data)

def search_book(request):
    if 'searched' in request.POST:
        searched = request.POST['searched']
        return render(request, "books/search.html", searched)
    else:
        return render(request, "books/search.html", {})

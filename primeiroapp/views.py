from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Book
from .models import User
from .forms import BookForm
import datetime


def home(request):
    data = {"today": datetime.datetime.now(), "users": User.objects.all()}
    print(data)
    return render(request, "primeiroapp/home.html", data)


def Booklist(request):
    data = {"books": Book.objects.all()}
    return render(request, "primeiroapp/book_list.html", data)


def add(request):
    data = {}
    form = BookForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("url_list")
    data["form"] = form
    return render(request, "primeiroapp/form.html", data)


def update(request, pk):
    data = {}
    book = Book.objects.get(pk=pk)
    form = BookForm(request.POST or None, instance=book)

    if form.is_valid():
        form.save()
        return redirect("url_list")

    data["form"] = form
    data["book"] = book
    return render(request, "primeiroapp/form.html", data)


def delete(request, pk):
    book = Book.objects.get(pk=pk)
    book.delete()
    return redirect("url_list")
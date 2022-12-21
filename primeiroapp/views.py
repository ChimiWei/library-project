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
    dados = {}
    form = BookForm(request.POST or None)
    print(form)
    print(BookForm)
    if form.is_valid():
        form.save()
        return redirect("url_listagem")
    dados["form"] = form
    return render(request, "primeiroapp/add.html", dados)
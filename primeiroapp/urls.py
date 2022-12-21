from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("add/", views.add, name="url_add"),
    path("list/", views.Booklist, name="url_list"),

]
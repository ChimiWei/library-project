from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("form/", views.add, name="url_form"),
    path("list/", views.Booklist, name="url_list"),
    path("update/<int:pk>/", views.update, name="url_update"),
    path("delete/<int:pk>/", views.delete, name="url_delete")
]
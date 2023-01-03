from django.forms import ModelForm
from .models import Book, User


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ["username", "firstname", "secondname", "password", "email", "cell_number"]


class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = ["title", "author", "description", "isbn", "launch", "edition", "category", "genre", "publisher", "price"]
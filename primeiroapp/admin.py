from django.contrib import admin
from primeiroapp.models import Author, Book, Category, User, CartItem
# Register your models here.


@admin.register(Author)
class AutorAdmin(admin.ModelAdmin):
    ...


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    ...


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    ...


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    ...


@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    ...

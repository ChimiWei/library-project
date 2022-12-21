from django.db import models

# Create your models here.


class Author(models.Model):
        name = models.CharField("Nome Completo", max_length=200)
        email = models.CharField("Email", max_length=200, blank=True, null=True)

        def __str__(self):
            return self.name


class Category(models.Model):
    name = models.CharField("Categoria", max_length=200)
    description = models.TextField("Descricao")

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField("Titulo", max_length=200)
    author = models.ManyToManyField(Author)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Categoria", blank=True, null=True)
    isbn = models.CharField("ISBN", max_length=13, unique=True, help_text="13 Caracteres <a href='/'> ISBN number </a>", null=True)
    launch = models.DateField(blank=True, null=True)
    edition = models.CharField("Edição", max_length=200, blank=True, null=True)
    genre = models.CharField("Gênero Textual", max_length=200, blank=True, null=True)
    publisher = models.CharField("Editora", max_length=200, blank=True, null=True)
    price = models.FloatField("Valor", default=100)
    description = models.TextField(blank=True, null=True)
    # image = models.imageField(upload_to="livraria/media", blank=True)

    def __str__(self):
        return self.title


class User(models.Model):
    username = models.CharField("Usuário", max_length=15)
    firstname = models.CharField("Nome", max_length=200, null=True)
    secondname = models.CharField("Sobrenome", max_length=200, null=True)
    email = models.CharField("Email", max_length=200)
    cell_number = models.CharField("Telefone", max_length=12, null=True)
    password = models.CharField("Senha", max_length=12)
    address = models.CharField("Endereço", max_length=255, null=True)

    def __str__(self):
        return self.username


class CartItem(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE, verbose_name="Usuário", blank=True, null=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, verbose_name="Livro", blank=True, null=True)
    quantity = models.IntegerField("Quantidade")

    def __str__(self):
        return self.book.title



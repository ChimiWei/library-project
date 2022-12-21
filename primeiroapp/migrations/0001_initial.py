# Generated by Django 4.1.4 on 2022-12-16 18:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Nome Completo')),
                ('email', models.CharField(blank=True, max_length=200, null=True, verbose_name='Email')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Categoria')),
                ('description', models.TextField(verbose_name='Descricao')),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Titulo')),
                ('isbn', models.CharField(help_text="13 Caracteres <a href=''> ISBN number </ a>", max_length=13, unique=True, verbose_name='ISBN')),
                ('launch', models.DateField(blank=True, null=True)),
                ('edition', models.CharField(blank=True, max_length=200, null=True, verbose_name='Edição')),
                ('genre', models.CharField(blank=True, max_length=200, null=True, verbose_name='Gênero Textual')),
                ('publisher', models.CharField(blank=True, max_length=200, null=True, verbose_name='Editora')),
                ('price', models.FloatField(default=100, verbose_name='Valor')),
                ('description', models.TextField(blank=True, null=True)),
                ('author', models.ManyToManyField(to='primeiroapp.author')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='primeiroapp.category', verbose_name='Categoria')),
            ],
        ),
    ]

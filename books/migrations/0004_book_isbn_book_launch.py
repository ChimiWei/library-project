# Generated by Django 4.1.4 on 2022-12-16 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_remove_book_isbn'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='isbn',
            field=models.CharField(help_text="13 Caracteres <a href='/'> ISBN number </a>", max_length=13, null=True, unique=True, verbose_name='ISBN'),
        ),
        migrations.AddField(
            model_name='book',
            name='launch',
            field=models.DateField(blank=True, null=True),
        ),
    ]
# Generated by Django 4.2.18 on 2025-01-16 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_book_author_book_is_bestsealing_alter_book_raiting'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='slug',
            field=models.SlugField(default=''),
        ),
    ]
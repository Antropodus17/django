# Generated by Django 4.2.19 on 2025-02-28 11:46

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('objects', '0005_alter_recipe_cuantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resource',
            name='name',
            field=models.CharField(db_index=True, max_length=50, unique=True, validators=[django.core.validators.MinLengthValidator(3)]),
        ),
    ]

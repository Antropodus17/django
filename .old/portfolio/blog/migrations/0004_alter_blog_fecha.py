# Generated by Django 4.2.16 on 2024-11-15 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_rename_tittle_blog_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='fecha',
            field=models.DateField(auto_now_add=True),
        ),
    ]

# Generated by Django 4.2.16 on 2024-11-24 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogs',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='blogs',
            name='image',
            field=models.ImageField(upload_to='img/blog'),
        ),
    ]

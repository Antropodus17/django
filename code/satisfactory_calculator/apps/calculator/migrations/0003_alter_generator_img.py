# Generated by Django 4.2.16 on 2024-11-22 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calculator', '0002_generator_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='generator',
            name='img',
            field=models.ImageField(height_field='250', upload_to='img/', width_field='200'),
        ),
    ]

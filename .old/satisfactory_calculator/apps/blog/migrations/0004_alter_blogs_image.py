# Generated by Django 4.2.16 on 2024-11-24 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_blogs_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogs',
            name='image',
            field=models.ImageField(blank=True, upload_to='img/blog'),
        ),
    ]

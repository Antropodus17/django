# Generated by Django 4.2.16 on 2024-11-14 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField(auto_created=True)),
                ('tittle', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('url', models.URLField()),
            ],
        ),
    ]

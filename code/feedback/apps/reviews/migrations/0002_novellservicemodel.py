# Generated by Django 4.2.18 on 2025-02-03 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='NovellServiceModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('web_server', models.IntegerField()),
                ('role', models.IntegerField()),
                ('sign_on', models.CharField(max_length=8)),
            ],
        ),
    ]

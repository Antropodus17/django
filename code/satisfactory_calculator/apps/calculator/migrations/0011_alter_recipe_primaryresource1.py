# Generated by Django 4.2.16 on 2024-11-25 21:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('calculator', '0010_rename_segundos_recipe_ticks'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='primaryResource1',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, related_name='Material_1', to='calculator.resource'),
            preserve_default=False,
        ),
    ]

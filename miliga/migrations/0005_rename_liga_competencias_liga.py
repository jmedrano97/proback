# Generated by Django 4.2.13 on 2024-06-26 05:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('miliga', '0004_equiposcompetencias_unique_equipo_competencia'),
    ]

    operations = [
        migrations.RenameField(
            model_name='competencias',
            old_name='Liga',
            new_name='liga',
        ),
    ]

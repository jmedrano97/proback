# Generated by Django 4.2.13 on 2024-06-11 22:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Alumno',
            new_name='Alumnos',
        ),
        migrations.RenameModel(
            old_name='Telefono',
            new_name='Telefonos',
        ),
    ]

# Generated by Django 4.1.6 on 2023-02-04 14:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('misPeliculas', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pelicula',
            old_name='directorio',
            new_name='director',
        ),
    ]
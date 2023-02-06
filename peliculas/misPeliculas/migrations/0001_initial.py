# Generated by Django 4.1.6 on 2023-02-04 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pelicula',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('genero', models.CharField(max_length=200)),
                ('directorio', models.CharField(blank=True, max_length=200)),
                ('descargada', models.BooleanField(blank=True, default=False)),
            ],
        ),
    ]
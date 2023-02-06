from django.contrib import admin
from .models import Pelicula

# Register your models here.
class MoviesAdmin(admin.ModelAdmin):
    icon_name = 'local_movies'

admin.site.register(Pelicula, MoviesAdmin)

admin.site.site_header = "Administración de Peliculas"
admin.site.site_title = "Administración de Peliculas"

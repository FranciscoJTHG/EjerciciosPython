from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('pelicula/<int:id>', views.get_pelicula, name='pelicula'),
    path('nuevaPelicula', views.nuevaPelicula, name='nuevaPelicula')
]

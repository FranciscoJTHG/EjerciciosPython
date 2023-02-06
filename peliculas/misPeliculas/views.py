from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import Http404, HttpResponse
from .models import Pelicula
from .forms import PeliculaForm

# Create your views here.
def index(request):
    lista_peliculas = Pelicula.objects.all()
    contexto = {'lista_peliculas': lista_peliculas}

    return render(request, 'mispeliculas/index.html', contexto)

def get_pelicula(request, id):
    try:
        pelicula = Pelicula.objects.get(id=id)
    except Pelicula.DoesNotExist:
        raise Http404("La pelicula no existe")
    
    contexto = {'pelicula': pelicula}

    return render(request, 'mispeliculas/pelicula.html', contexto)

def nuevaPelicula(request):
    form = PeliculaForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        pelicula = Pelicula()
        pelicula.titulo = form.cleaned_data['titulo']
        pelicula.director = form.cleaned_data['director']
        pelicula.genero = form.cleaned_data['genero']
        pelicula.save()
        messages.success(request, 'Pelicula registrada Correctamente')
        return redirect('nuevaPelicula')
    else:
        form = PeliculaForm()
        return render(request, 'mispeliculas/nuevaPelicula.html', {'form': form})
            


from django.shortcuts import render, redirect
from .models import *
from .forms import *


def home(request):
    allMovies = Movie.objects.all()

    context = {
        "movies": allMovies
    }

    return render(request, 'main/index.html', context)


def detail(request, id):
    movie = Movie.objects.get(id=id)

    context = {
        'movie': movie,
    }

    return render(request, 'main/details.html', context)


# adding movies to database
def add_movies(request):
    if request.method == "POST":
        form = MovieForm(request.POST or None)

        # check if form is valid
        if form.is_valid():
            data = form.save(commit=False)
            data.save()
            return redirect("main:home")
    else:
        form = MovieForm()
    return render(request, 'main/addmovies.html', {'form': form, 'controller': "Add Movies"})


def edit_movies(request, id):
    movie = Movie.objects.get(id=id)

    if request.method == "POST":
        form = MovieForm(request.POST or None, instance=movie)

        if form.is_valid():
            data = form.save(commit=False)
            data.save()
            return redirect("main:detail", id)
    else:
        form = MovieForm(instance=movie)
    return render(request, "main/addmovies.html", {"form": form, "controller": "Edit Movies"})


def delete_movies(request, id):
    movie = Movie.objects.get(id=id)

    movie.delete()
    return redirect("main:home")

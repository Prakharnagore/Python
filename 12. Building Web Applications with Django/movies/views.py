from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Movie
# Create your views here.


def index(request):
    movies = Movie.objects.all()
    # output = ','.join([m.title for m in movies])
    return render(request, 'movies/index.html', {'movies': movies})
    # // return HttpResponse(output)


def details(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    return render(request, 'movies/details.html', {'movie': movie})

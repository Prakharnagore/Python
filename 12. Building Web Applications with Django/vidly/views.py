from django.shortcuts import render
from movies.models import Movie


def home(request):
    latest_movies = Movie.objects.select_related('genre').order_by('-id')[:3]
    return render(request, 'home.html', {
        'movie_count': Movie.objects.count(),
        'latest_movies': latest_movies,
    })

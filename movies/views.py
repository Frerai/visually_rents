from django.http import HttpResponse, Http404  # Importing Http response class.
from django.shortcuts import render, get_object_or_404  # Allows to get an object or raise 404 if error found
from .models import Movie


def index(request):  # Main page of "Movies" app.
    """A view of our main page."""
    movies = Movie.objects.all()  # A method to get all the movies from the database.

#    output = ', '.join([m.title for m in movies])  # List comprehension to retrieve all titles of movies. Combine with
    # a string only containing a comma, using the ".join()" method, each title is returned separated by a comma.
#    Movie.objects.filter(release_year=2000)  # A filter, can pass in arbitrary keyword arguments like "release_year=".
#    Movie.objects.get(id=2)  # Method for getting a single object - a keyword argument is needed.

    return render(request, 'movies/index.html', {'movies': movies})


def detail(request, movie_id):  # Reference for "movie_id" as 2nd argument, since each movie has its own URL id.
    """Displays relevant details of each movie, when clicked on the movie."""
    movie = get_object_or_404(Movie, id=movie_id)  # This Django function automatically raises 404 by try/exceptions
    return render(request, 'movies/detail.html', {'movie': movie})

# try:
# movie = Movie.objects.get(id=movie_id)  # Using "Movie" model with ".get()" function to get each specific movies ID
# return render(request, 'movies/detail.html', {'movie': movie})  # Context object is a dict, with key "movie" and set
# # to "movie" object found at the line above
# except Movie.DoesNotExist:  # "Movie" class inherits from "Model" class in Django, so this exception exists.
# raise Http404()

from django.db import models
from django.utils import timezone  # Used for finding my current time, to implement in dates and creations.


class Genre(models.Model):
    name = models.CharField(max_length=255)  # Characters for naming genres.

    def __str__(self):  # Displays proper genres, rather than showing "Genre object" in the admin interface.
        return self.name


class Movie(models.Model):  # Fields to fill in, when adding/registering a movie.
    title = models.CharField(max_length=255)
    release_year = models.IntegerField()
    number_in_stock = models.IntegerField()  # Available movies for rent.
    daily_rate = models.FloatField()  # Price of rental.
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)  # To establish a relationship between the "Movies"
    # and "Genre" class, we first pass in "Genre" class, then a cascading delete, to delete EVERYTHING upon deletion
    date_created = models.DateTimeField(default=timezone.now)  # Don't call on the "now()" method, or the time will be
    # a hardcoded date and time - simply pass a reference to the "now()" method by syntax of "now" and not "now()".

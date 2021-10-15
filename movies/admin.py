from django.contrib import admin
from .models import Genre, Movie


class GenreAdmin(admin.ModelAdmin):  # Inherit from "admin" which has a model from the admin interface.
    list_display = ('id', 'name')  # A tuple of all the fields to show in the "genre" admin page. Otherwise would be
    # represented as "Genre object", and no fields would be visible.


class MovieAdmin(admin.ModelAdmin):
    exclude = ('date_created', )  # Used to hide fields wished to exclude under the "Movie" admin interface.
    # this field would otherwise need to be filled out when registering/adding new entries to "Movie".
    list_display = ('title', 'number_in_stock', 'daily_rate', 'genre',)  # This attribute is a builtin, which can be
    # overwritten like this. Now these fields will be displayed rather than a "Movie objects" entry.


# This tells Django to register the "Genre" model in the administration interface. Second argument is required here.
admin.site.register(Genre, GenreAdmin)

# This tells Django to register the "Movie" model in the administration interface.
admin.site.register(Movie, MovieAdmin)

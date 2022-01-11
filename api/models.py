from django.db import models
from tastypie.resources import ModelResource  # Importing tastypie to access the ModelResource class
from movies.models import Movie


class MovieResource(ModelResource):  # Inserting the ModelResource class here to use
    class Meta:  # Tastypie looks for an inner class in MovieResource class, which is Meta (it defines metadata)
        queryset = Movie.objects.all()  # All method returns a query
        resource_name = "movies"
        excludes = ['date_created']  # Allows to hide and exclude any chosen properties from the public APIs

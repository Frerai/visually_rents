from django.urls import path
from . import views  # From current directory, import the "views" module - the one in THIS directory

app_name = 'movies'  # When provided an app name here, Django will access this name each time when retrieving URLs-
# thus whenever an URL name is provided 'index' and 'detail' is enough, rather than 'movies_index' and 'movies_detail'

urlpatterns = [
    path('', views.index, name='index'),  # Empty string is passed in, so all relevant URLs will be redirected
    path('<int:movie_id>', views.detail, name='detail'),  # Uniquely identifies URLs: 'movies/1', prefixed as int
]
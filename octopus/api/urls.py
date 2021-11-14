from django.urls import path

from .handlers.movie.movie_controller import MovieController

urlpatterns = [
    path("movie/", MovieController.as_view()),
]

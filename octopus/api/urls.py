from django.urls import path

from . import views
from .handlers.movie.movie_controller import MovieController

urlpatterns = [
    path("", views.index, name="index"),
    path("movie/", MovieController.as_view()),
]

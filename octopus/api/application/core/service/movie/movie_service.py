from datetime import datetime

from api.application.core.domain.movie.movie_entity import MovieEntity
from api.application.core.ports.repository.movie.movie_repository_interface import (
    MovieRepositoryInterface,
)


class MovieService:
    def __init__(self, movie_repository: MovieRepositoryInterface):
        self.movie_repository = movie_repository

    def create_movie(self, title: str, release_date: datetime):
        movie = MovieEntity(title=title, release_date=release_date)
        self.movie_repository.create(movie=movie)

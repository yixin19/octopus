from api.application.core.domain.movie.movie_entity import MovieEntity
from api.application.core.ports.repository.movie.movie_repository_interface import (
    MovieRepositoryInterface,
)
from api.models.movie_model import MovieModel


class MovieRepository(MovieRepositoryInterface):
    def __init__(self):
        super().__init__()

    def create(self, movie: MovieEntity):
        created_movie = MovieModel.objects.create(
            title=movie.title, release_date=movie.release_date
        )
        return MovieEntity(
            title=created_movie.title, release_date=created_movie.release_date
        )

    def get_all_movies(self) -> list[MovieEntity]:
        return []

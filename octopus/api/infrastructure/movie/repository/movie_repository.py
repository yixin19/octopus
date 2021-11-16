from api.application.core.domain.movie.movie_entity import MovieEntity
from api.application.core.ports.repository.movie.movie_repository_interface import (
    MovieRepositoryInterface,
)
from api.models.movie_mapper import MovieMapper
from api.models.movie_model import MovieModel


class MovieRepository(MovieRepositoryInterface):

    def create(self, movie: MovieEntity):
        created_movie_model = MovieModel.objects.create(
            title=movie.title, release_date=movie.release_date
        )
        return MovieMapper.map_to_entity(created_movie_model)

    def get_all_movies(self) -> list[MovieEntity]:
        return []

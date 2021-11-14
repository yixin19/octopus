from api.application.core.domain.movie.movie_entity import MovieEntity
from api.models.movie_model import MovieModel


class MovieMapper:
    @staticmethod
    def map_to_entity(movie_model: MovieModel):
        return MovieEntity(
            title=movie_model.title, release_date=movie_model.release_date
        )
